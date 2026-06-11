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
def _f23_inv_to_revenue(inventory, revenue):
    return inventory / revenue.replace(0, np.nan).abs()


def _f23_inv_cycle(inventory, w):
    m = inventory.rolling(w, min_periods=max(1, w // 2)).mean()
    return (inventory - m) / m.replace(0, np.nan).abs()


def _f23_inv_dynamics(inventory, cor, w):
    inv_g = inventory.pct_change(periods=w)
    cor_g = cor.pct_change(periods=w)
    return inv_g - cor_g


def f23uic_f23_uranium_inventory_cycle_invrevz_252d_base_v076_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 252) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_252d_base_v077_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 252) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_252d_base_v078_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 252) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_252d_base_v079_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 252) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_252d_base_v080_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 252) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_378d_base_v081_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_378d_base_v082_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 378) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_378d_base_v083_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 378) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_378d_base_v084_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 378) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_378d_base_v085_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 378) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_378d_base_v086_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 378) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_378d_base_v087_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 378) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_378d_base_v088_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 378) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_504d_base_v089_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_504d_base_v090_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 504) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_504d_base_v091_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 504) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_504d_base_v092_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 504) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_504d_base_v093_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 504) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_504d_base_v094_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 504) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_504d_base_v095_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 504) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_504d_base_v096_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 504) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_5d_base_v097_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_5d_base_v098_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_5d_base_v099_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_5d_base_v100_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_5d_base_v101_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 5) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_5d_base_v102_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 5) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_5d_base_v103_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 5) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_5d_base_v104_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 5) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_10d_base_v105_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_10d_base_v106_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 10) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_10d_base_v107_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_10d_base_v108_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_10d_base_v109_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 10) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_10d_base_v110_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 10) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_10d_base_v111_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 10) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_10d_base_v112_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 10) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_21d_base_v113_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_21d_base_v114_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_21d_base_v115_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_21d_base_v116_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_21d_base_v117_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 21) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_21d_base_v118_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 21) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_21d_base_v119_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 21) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_21d_base_v120_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 21) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_42d_base_v121_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_42d_base_v122_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 42) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_42d_base_v123_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_42d_base_v124_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_42d_base_v125_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 42) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_42d_base_v126_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 42) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_42d_base_v127_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 42) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_42d_base_v128_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 42) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_63d_base_v129_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_63d_base_v130_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_63d_base_v131_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_63d_base_v132_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_63d_base_v133_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 63) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_63d_base_v134_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 63) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_63d_base_v135_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 63) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_63d_base_v136_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 63) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_126d_base_v137_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_126d_base_v138_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 126) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_126d_base_v139_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 126) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_126d_base_v140_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_126d_base_v141_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 126) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_126d_base_v142_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 126) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_126d_base_v143_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 126) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_126d_base_v144_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 126) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_189d_base_v145_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_189d_base_v146_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 189) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_189d_base_v147_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 189) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_189d_base_v148_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 189) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_189d_base_v149_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 189) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevmean_189d_base_v150_signal(inventory, revenue, closeadj):
    result = _mean(_f23_inv_to_revenue(inventory, revenue), 189) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f23uic_f23_uranium_inventory_cycle_invrevz_252d_base_v076_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_252d_base_v077_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_252d_base_v078_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_252d_base_v079_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_252d_base_v080_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_378d_base_v081_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_378d_base_v082_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_378d_base_v083_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_378d_base_v084_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_378d_base_v085_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_378d_base_v086_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_378d_base_v087_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_378d_base_v088_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_504d_base_v089_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_504d_base_v090_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_504d_base_v091_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_504d_base_v092_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_504d_base_v093_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_504d_base_v094_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_504d_base_v095_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_504d_base_v096_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_5d_base_v097_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_5d_base_v098_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_5d_base_v099_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_5d_base_v100_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_5d_base_v101_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_5d_base_v102_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_5d_base_v103_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_5d_base_v104_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_10d_base_v105_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_10d_base_v106_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_10d_base_v107_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_10d_base_v108_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_10d_base_v109_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_10d_base_v110_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_10d_base_v111_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_10d_base_v112_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_21d_base_v113_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_21d_base_v114_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_21d_base_v115_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_21d_base_v116_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_21d_base_v117_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_21d_base_v118_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_21d_base_v119_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_21d_base_v120_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_42d_base_v121_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_42d_base_v122_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_42d_base_v123_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_42d_base_v124_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_42d_base_v125_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_42d_base_v126_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_42d_base_v127_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_42d_base_v128_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_63d_base_v129_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_63d_base_v130_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_63d_base_v131_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_63d_base_v132_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_63d_base_v133_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_63d_base_v134_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_63d_base_v135_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_63d_base_v136_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_126d_base_v137_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_126d_base_v138_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_126d_base_v139_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_126d_base_v140_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_126d_base_v141_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_126d_base_v142_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_126d_base_v143_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_126d_base_v144_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_189d_base_v145_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_189d_base_v146_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_189d_base_v147_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_189d_base_v148_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_189d_base_v149_signal,
    f23uic_f23_uranium_inventory_cycle_invrevmean_189d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F23_URANIUM_INVENTORY_CYCLE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    assets  = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    inventory = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue,
        "ebitda": ebitda,
        "capex": capex,
        "depamor": depamor,
        "cor": cor,
        "assets": assets,
        "inventory": inventory,
        "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f23_inv_to_revenue', '_f23_inv_cycle', '_f23_inv_dynamics')
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
    print(f"OK f23_uranium_inventory_cycle_base_076_150_claude: {n_features} features pass")
