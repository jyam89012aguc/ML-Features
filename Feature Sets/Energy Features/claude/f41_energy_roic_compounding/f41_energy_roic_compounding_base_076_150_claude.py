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
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()

# ===== folder domain primitives =====
def _f41_roic_trajectory(roic, w):
    base = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    return base - roic.rolling(w * 2, min_periods=max(1, w)).mean()


def _f41_roic_persistence(roic, w):
    above = (roic > roic.rolling(w, min_periods=max(1, w // 2)).median()).astype(float)
    return above.rolling(w, min_periods=max(1, w // 2)).mean()


def _f41_roic_quality(roic, roa, w):
    quality = (roic - roa) / roa.replace(0, np.nan).abs()
    return quality.rolling(w, min_periods=max(1, w // 2)).mean()

# ===== features =====
def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t378_std_xc_rmean_base_v076_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _std(base, 378) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t504_std_xc_base_v077_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t504_std_xc2_base_v078_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _std(base, 504) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t504_std_logc_base_v079_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _std(base, 504) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t504_std_xc_rmean_base_v080_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _std(base, 504) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t5_z_xc_base_v081_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t5_z_xc2_base_v082_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 5) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t5_z_logc_base_v083_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 5) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t5_z_xc_rmean_base_v084_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 5) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t10_z_xc_base_v085_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t10_z_xc2_base_v086_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 10) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t10_z_logc_base_v087_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 10) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t10_z_xc_rmean_base_v088_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 10) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t21_z_xc_base_v089_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t21_z_xc2_base_v090_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t21_z_logc_base_v091_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 21) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t21_z_xc_rmean_base_v092_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 21) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t42_z_xc_base_v093_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t42_z_xc2_base_v094_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t42_z_logc_base_v095_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 42) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t42_z_xc_rmean_base_v096_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 42) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t63_z_xc_base_v097_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t63_z_xc2_base_v098_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t63_z_logc_base_v099_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 63) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t63_z_xc_rmean_base_v100_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 63) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t126_z_xc_base_v101_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t126_z_xc2_base_v102_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t126_z_logc_base_v103_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 126) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t126_z_xc_rmean_base_v104_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 126) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t189_z_xc_base_v105_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t189_z_xc2_base_v106_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 189) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t189_z_logc_base_v107_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 189) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t189_z_xc_rmean_base_v108_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 189) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t252_z_xc_base_v109_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t252_z_xc2_base_v110_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t252_z_logc_base_v111_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 252) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t252_z_xc_rmean_base_v112_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 252) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t378_z_xc_base_v113_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t378_z_xc2_base_v114_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 378) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t378_z_logc_base_v115_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 378) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t378_z_xc_rmean_base_v116_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 378) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t504_z_xc_base_v117_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t504_z_xc2_base_v118_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 504) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t504_z_logc_base_v119_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 504) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t504_z_xc_rmean_base_v120_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _z(base, 504) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t5_ema_xc_base_v121_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t5_ema_xc2_base_v122_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 5) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t5_ema_logc_base_v123_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 5) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t5_ema_xc_rmean_base_v124_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 5) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t10_ema_xc_base_v125_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t10_ema_xc2_base_v126_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 10) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t10_ema_logc_base_v127_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 10) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t10_ema_xc_rmean_base_v128_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 10) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t21_ema_xc_base_v129_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t21_ema_xc2_base_v130_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t21_ema_logc_base_v131_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 21) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t21_ema_xc_rmean_base_v132_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 21) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t42_ema_xc_base_v133_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t42_ema_xc2_base_v134_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t42_ema_logc_base_v135_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 42) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t42_ema_xc_rmean_base_v136_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 42) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t63_ema_xc_base_v137_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t63_ema_xc2_base_v138_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t63_ema_logc_base_v139_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 63) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t63_ema_xc_rmean_base_v140_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 63) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t126_ema_xc_base_v141_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t126_ema_xc2_base_v142_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t126_ema_logc_base_v143_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 126) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t126_ema_xc_rmean_base_v144_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 126) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t189_ema_xc_base_v145_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t189_ema_xc2_base_v146_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 189) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t189_ema_logc_base_v147_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 189) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t189_ema_xc_rmean_base_v148_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 189) * closeadj * _mean(closeadj, 21) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t252_ema_xc_base_v149_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t252_ema_xc2_base_v150_signal(roic, closeadj):
    base = _f41_roic_trajectory(roic, 5)
    result = _ema(base, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t378_std_xc_rmean_base_v076_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t504_std_xc_base_v077_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t504_std_xc2_base_v078_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t504_std_logc_base_v079_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t504_std_xc_rmean_base_v080_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t5_z_xc_base_v081_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t5_z_xc2_base_v082_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t5_z_logc_base_v083_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t5_z_xc_rmean_base_v084_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t10_z_xc_base_v085_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t10_z_xc2_base_v086_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t10_z_logc_base_v087_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t10_z_xc_rmean_base_v088_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t21_z_xc_base_v089_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t21_z_xc2_base_v090_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t21_z_logc_base_v091_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t21_z_xc_rmean_base_v092_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t42_z_xc_base_v093_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t42_z_xc2_base_v094_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t42_z_logc_base_v095_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t42_z_xc_rmean_base_v096_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t63_z_xc_base_v097_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t63_z_xc2_base_v098_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t63_z_logc_base_v099_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t63_z_xc_rmean_base_v100_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t126_z_xc_base_v101_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t126_z_xc2_base_v102_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t126_z_logc_base_v103_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t126_z_xc_rmean_base_v104_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t189_z_xc_base_v105_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t189_z_xc2_base_v106_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t189_z_logc_base_v107_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t189_z_xc_rmean_base_v108_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t252_z_xc_base_v109_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t252_z_xc2_base_v110_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t252_z_logc_base_v111_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t252_z_xc_rmean_base_v112_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t378_z_xc_base_v113_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t378_z_xc2_base_v114_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t378_z_logc_base_v115_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t378_z_xc_rmean_base_v116_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t504_z_xc_base_v117_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t504_z_xc2_base_v118_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t504_z_logc_base_v119_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t504_z_xc_rmean_base_v120_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t5_ema_xc_base_v121_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t5_ema_xc2_base_v122_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t5_ema_logc_base_v123_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t5_ema_xc_rmean_base_v124_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t10_ema_xc_base_v125_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t10_ema_xc2_base_v126_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t10_ema_logc_base_v127_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t10_ema_xc_rmean_base_v128_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t21_ema_xc_base_v129_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t21_ema_xc2_base_v130_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t21_ema_logc_base_v131_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t21_ema_xc_rmean_base_v132_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t42_ema_xc_base_v133_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t42_ema_xc2_base_v134_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t42_ema_logc_base_v135_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t42_ema_xc_rmean_base_v136_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t63_ema_xc_base_v137_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t63_ema_xc2_base_v138_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t63_ema_logc_base_v139_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t63_ema_xc_rmean_base_v140_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t126_ema_xc_base_v141_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t126_ema_xc2_base_v142_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t126_ema_logc_base_v143_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t126_ema_xc_rmean_base_v144_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t189_ema_xc_base_v145_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t189_ema_xc2_base_v146_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t189_ema_logc_base_v147_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t189_ema_xc_rmean_base_v148_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t252_ema_xc_base_v149_signal,
    f41erc_f41_energy_roic_compounding_roic_trajectory_5d_t252_ema_xc2_base_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]

REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F41_ENERGY_ROIC_COMPOUNDING_REGISTRY_076_150 = REGISTRY


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
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor,
        "assets": assets, "liabilities": liabilities, "equity": equity,
        "debt": debt, "cashneq": cashneq, "ppnenet": ppnenet,
        "marketcap": marketcap, "ev": ev,
        "roa": roa, "roe": roe, "roic": roic,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f41_roic_trajectory", "_f41_roic_persistence", "_f41_roic_quality")
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
    print(f"OK f41_energy_roic_compounding_base_076_150_claude: {n_features} features pass")
