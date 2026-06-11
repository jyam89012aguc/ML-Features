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


def _f039_price_progress(close, w):
    return close.pct_change(periods=w)


def _f039_volume_effort(volume, w):
    return volume.rolling(w, min_periods=max(1, w // 2)).sum()


def _f039_effort_result_ratio(close, volume, w):
    progress = close.pct_change(periods=w)
    effort = volume.rolling(w, min_periods=max(1, w // 2)).sum()
    return progress / (effort + 1.0).replace(0, np.nan)


def f039evr_f039_effort_vs_result_pprogxvm_5d_base_v076_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 5) * _mean(volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxstd_5d_base_v077_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 5) * _std(volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxvz_5d_base_v078_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 5) * _z(volume, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxvm_10d_base_v079_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 10) * _mean(volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxstd_10d_base_v080_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 10) * _std(volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxvz_10d_base_v081_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 10) * _z(volume, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxvm_21d_base_v082_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 21) * _mean(volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxstd_21d_base_v083_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 21) * _std(volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxvz_21d_base_v084_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 21) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxvm_42d_base_v085_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 42) * _mean(volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxstd_42d_base_v086_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 42) * _std(volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxvz_42d_base_v087_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 42) * _z(volume, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxvm_63d_base_v088_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 63) * _mean(volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxstd_63d_base_v089_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 63) * _std(volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxvz_63d_base_v090_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxvm_126d_base_v091_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 126) * _mean(volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxstd_126d_base_v092_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 126) * _std(volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxvz_126d_base_v093_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 126) * _z(volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxvm_189d_base_v094_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 189) * _mean(volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxstd_189d_base_v095_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 189) * _std(volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxvz_189d_base_v096_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 189) * _z(volume, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxvm_252d_base_v097_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 252) * _mean(volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxstd_252d_base_v098_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 252) * _std(volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxvz_252d_base_v099_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 252) * _z(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxvm_378d_base_v100_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 378) * _mean(volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxstd_378d_base_v101_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 378) * _std(volume, 21) / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_pprogxvz_378d_base_v102_signal(closeadj, volume):
    result = _f039_price_progress(closeadj, 378) * _z(volume, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxzcl_5d_base_v103_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 5) * _z(closeadj, 63) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxstdcl_5d_base_v104_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 5) * _std(closeadj, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxcumcl_5d_base_v105_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 5) * _mean(closeadj, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxzcl_10d_base_v106_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 10) * _z(closeadj, 63) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxstdcl_10d_base_v107_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 10) * _std(closeadj, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxcumcl_10d_base_v108_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 10) * _mean(closeadj, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxzcl_21d_base_v109_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 21) * _z(closeadj, 63) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxstdcl_21d_base_v110_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 21) * _std(closeadj, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxcumcl_21d_base_v111_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 21) * _mean(closeadj, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxzcl_42d_base_v112_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 42) * _z(closeadj, 63) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxstdcl_42d_base_v113_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 42) * _std(closeadj, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxcumcl_42d_base_v114_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 42) * _mean(closeadj, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxzcl_63d_base_v115_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 63) * _z(closeadj, 63) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxstdcl_63d_base_v116_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 63) * _std(closeadj, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxcumcl_63d_base_v117_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 63) * _mean(closeadj, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxzcl_126d_base_v118_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 126) * _z(closeadj, 63) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxstdcl_126d_base_v119_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 126) * _std(closeadj, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxcumcl_126d_base_v120_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 126) * _mean(closeadj, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxzcl_189d_base_v121_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 189) * _z(closeadj, 63) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxstdcl_189d_base_v122_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 189) * _std(closeadj, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxcumcl_189d_base_v123_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 189) * _mean(closeadj, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxzcl_252d_base_v124_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 252) * _z(closeadj, 63) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxstdcl_252d_base_v125_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 252) * _std(closeadj, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxcumcl_252d_base_v126_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 252) * _mean(closeadj, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxzcl_378d_base_v127_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 378) * _z(closeadj, 63) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxstdcl_378d_base_v128_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 378) * _std(closeadj, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_veffxcumcl_378d_base_v129_signal(closeadj, volume):
    result = _f039_volume_effort(volume, 378) * _mean(closeadj, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrxvm_5d_base_v130_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 5) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrxstdv_5d_base_v131_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 5) * _std(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrxclmn_5d_base_v132_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrxvm_10d_base_v133_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 10) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrxstdv_10d_base_v134_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 10) * _std(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrxclmn_10d_base_v135_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrxvm_21d_base_v136_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 21) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrxstdv_21d_base_v137_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 21) * _std(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrxclmn_21d_base_v138_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrxvm_42d_base_v139_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 42) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrxstdv_42d_base_v140_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 42) * _std(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrxclmn_42d_base_v141_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrxvm_63d_base_v142_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 63) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrxstdv_63d_base_v143_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 63) * _std(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrxclmn_63d_base_v144_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrxvm_126d_base_v145_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 126) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrxstdv_126d_base_v146_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 126) * _std(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrxclmn_126d_base_v147_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 126) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrxvm_189d_base_v148_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 189) * _mean(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrxstdv_189d_base_v149_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 189) * _std(volume, 21) * closeadj / 1e3
    return result.replace([np.inf, -np.inf], np.nan)


def f039evr_f039_effort_vs_result_evrxclmn_189d_base_v150_signal(closeadj, volume):
    result = _f039_effort_result_ratio(closeadj, volume, 189) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f039evr_f039_effort_vs_result_pprogxvm_5d_base_v076_signal,
    f039evr_f039_effort_vs_result_pprogxstd_5d_base_v077_signal,
    f039evr_f039_effort_vs_result_pprogxvz_5d_base_v078_signal,
    f039evr_f039_effort_vs_result_pprogxvm_10d_base_v079_signal,
    f039evr_f039_effort_vs_result_pprogxstd_10d_base_v080_signal,
    f039evr_f039_effort_vs_result_pprogxvz_10d_base_v081_signal,
    f039evr_f039_effort_vs_result_pprogxvm_21d_base_v082_signal,
    f039evr_f039_effort_vs_result_pprogxstd_21d_base_v083_signal,
    f039evr_f039_effort_vs_result_pprogxvz_21d_base_v084_signal,
    f039evr_f039_effort_vs_result_pprogxvm_42d_base_v085_signal,
    f039evr_f039_effort_vs_result_pprogxstd_42d_base_v086_signal,
    f039evr_f039_effort_vs_result_pprogxvz_42d_base_v087_signal,
    f039evr_f039_effort_vs_result_pprogxvm_63d_base_v088_signal,
    f039evr_f039_effort_vs_result_pprogxstd_63d_base_v089_signal,
    f039evr_f039_effort_vs_result_pprogxvz_63d_base_v090_signal,
    f039evr_f039_effort_vs_result_pprogxvm_126d_base_v091_signal,
    f039evr_f039_effort_vs_result_pprogxstd_126d_base_v092_signal,
    f039evr_f039_effort_vs_result_pprogxvz_126d_base_v093_signal,
    f039evr_f039_effort_vs_result_pprogxvm_189d_base_v094_signal,
    f039evr_f039_effort_vs_result_pprogxstd_189d_base_v095_signal,
    f039evr_f039_effort_vs_result_pprogxvz_189d_base_v096_signal,
    f039evr_f039_effort_vs_result_pprogxvm_252d_base_v097_signal,
    f039evr_f039_effort_vs_result_pprogxstd_252d_base_v098_signal,
    f039evr_f039_effort_vs_result_pprogxvz_252d_base_v099_signal,
    f039evr_f039_effort_vs_result_pprogxvm_378d_base_v100_signal,
    f039evr_f039_effort_vs_result_pprogxstd_378d_base_v101_signal,
    f039evr_f039_effort_vs_result_pprogxvz_378d_base_v102_signal,
    f039evr_f039_effort_vs_result_veffxzcl_5d_base_v103_signal,
    f039evr_f039_effort_vs_result_veffxstdcl_5d_base_v104_signal,
    f039evr_f039_effort_vs_result_veffxcumcl_5d_base_v105_signal,
    f039evr_f039_effort_vs_result_veffxzcl_10d_base_v106_signal,
    f039evr_f039_effort_vs_result_veffxstdcl_10d_base_v107_signal,
    f039evr_f039_effort_vs_result_veffxcumcl_10d_base_v108_signal,
    f039evr_f039_effort_vs_result_veffxzcl_21d_base_v109_signal,
    f039evr_f039_effort_vs_result_veffxstdcl_21d_base_v110_signal,
    f039evr_f039_effort_vs_result_veffxcumcl_21d_base_v111_signal,
    f039evr_f039_effort_vs_result_veffxzcl_42d_base_v112_signal,
    f039evr_f039_effort_vs_result_veffxstdcl_42d_base_v113_signal,
    f039evr_f039_effort_vs_result_veffxcumcl_42d_base_v114_signal,
    f039evr_f039_effort_vs_result_veffxzcl_63d_base_v115_signal,
    f039evr_f039_effort_vs_result_veffxstdcl_63d_base_v116_signal,
    f039evr_f039_effort_vs_result_veffxcumcl_63d_base_v117_signal,
    f039evr_f039_effort_vs_result_veffxzcl_126d_base_v118_signal,
    f039evr_f039_effort_vs_result_veffxstdcl_126d_base_v119_signal,
    f039evr_f039_effort_vs_result_veffxcumcl_126d_base_v120_signal,
    f039evr_f039_effort_vs_result_veffxzcl_189d_base_v121_signal,
    f039evr_f039_effort_vs_result_veffxstdcl_189d_base_v122_signal,
    f039evr_f039_effort_vs_result_veffxcumcl_189d_base_v123_signal,
    f039evr_f039_effort_vs_result_veffxzcl_252d_base_v124_signal,
    f039evr_f039_effort_vs_result_veffxstdcl_252d_base_v125_signal,
    f039evr_f039_effort_vs_result_veffxcumcl_252d_base_v126_signal,
    f039evr_f039_effort_vs_result_veffxzcl_378d_base_v127_signal,
    f039evr_f039_effort_vs_result_veffxstdcl_378d_base_v128_signal,
    f039evr_f039_effort_vs_result_veffxcumcl_378d_base_v129_signal,
    f039evr_f039_effort_vs_result_evrxvm_5d_base_v130_signal,
    f039evr_f039_effort_vs_result_evrxstdv_5d_base_v131_signal,
    f039evr_f039_effort_vs_result_evrxclmn_5d_base_v132_signal,
    f039evr_f039_effort_vs_result_evrxvm_10d_base_v133_signal,
    f039evr_f039_effort_vs_result_evrxstdv_10d_base_v134_signal,
    f039evr_f039_effort_vs_result_evrxclmn_10d_base_v135_signal,
    f039evr_f039_effort_vs_result_evrxvm_21d_base_v136_signal,
    f039evr_f039_effort_vs_result_evrxstdv_21d_base_v137_signal,
    f039evr_f039_effort_vs_result_evrxclmn_21d_base_v138_signal,
    f039evr_f039_effort_vs_result_evrxvm_42d_base_v139_signal,
    f039evr_f039_effort_vs_result_evrxstdv_42d_base_v140_signal,
    f039evr_f039_effort_vs_result_evrxclmn_42d_base_v141_signal,
    f039evr_f039_effort_vs_result_evrxvm_63d_base_v142_signal,
    f039evr_f039_effort_vs_result_evrxstdv_63d_base_v143_signal,
    f039evr_f039_effort_vs_result_evrxclmn_63d_base_v144_signal,
    f039evr_f039_effort_vs_result_evrxvm_126d_base_v145_signal,
    f039evr_f039_effort_vs_result_evrxstdv_126d_base_v146_signal,
    f039evr_f039_effort_vs_result_evrxclmn_126d_base_v147_signal,
    f039evr_f039_effort_vs_result_evrxvm_189d_base_v148_signal,
    f039evr_f039_effort_vs_result_evrxstdv_189d_base_v149_signal,
    f039evr_f039_effort_vs_result_evrxclmn_189d_base_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F039_EFFORT_VS_RESULT_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f039_price_progress", "_f039_volume_effort", "_f039_effort_result_ratio")
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
    print(f"OK f039_effort_vs_result_base_076_150_claude: {n_features} features pass")
