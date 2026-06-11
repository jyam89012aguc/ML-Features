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
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


# ===== folder domain primitives =====
def _f08_inventory_turnover(inventory, cor):
    return cor / inventory.replace(0, np.nan)


def _f08_inventory_freshness(inventory, revenue, w):
    inv_per_rev = inventory / revenue.replace(0, np.nan)
    m = inv_per_rev.rolling(w, min_periods=max(1, w // 2)).mean()
    return inv_per_rev - m


def _f08_inv_velocity(inventory, cor, w):
    turn = cor / inventory.replace(0, np.nan)
    return turn.pct_change(periods=w)

def f08rif_f08_retail_inventory_freshness_fresh_std_126d_base_v076_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 126)
    result = _std(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_std_189d_base_v077_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 189)
    result = _std(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_std_252d_base_v078_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 252)
    result = _std(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_std_378d_base_v079_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 378)
    result = _std(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_std_504d_base_v080_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 504)
    result = _std(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_z_5d_base_v081_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 5)
    result = _z(f, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_z_10d_base_v082_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 10)
    result = _z(f, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_z_21d_base_v083_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 21)
    result = _z(f, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_z_42d_base_v084_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 42)
    result = _z(f, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_z_63d_base_v085_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 63)
    result = _z(f, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_z_126d_base_v086_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 126)
    result = _z(f, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_z_189d_base_v087_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 189)
    result = _z(f, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_z_252d_base_v088_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 252)
    result = _z(f, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_z_378d_base_v089_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 378)
    result = _z(f, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_z_504d_base_v090_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 504)
    result = _z(f, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_ema_5d_base_v091_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 5)
    result = _ema(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_ema_10d_base_v092_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 10)
    result = _ema(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_ema_21d_base_v093_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 21)
    result = _ema(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_ema_42d_base_v094_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 42)
    result = _ema(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_ema_63d_base_v095_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 63)
    result = _ema(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_ema_126d_base_v096_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 126)
    result = _ema(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_ema_189d_base_v097_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 189)
    result = _ema(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_ema_252d_base_v098_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 252)
    result = _ema(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_ema_378d_base_v099_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 378)
    result = _ema(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_fresh_ema_504d_base_v100_signal(inventory, revenue, closeadj):
    f = _f08_inventory_freshness(inventory, revenue, 504)
    result = _ema(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_5d_base_v101_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 5)
    result = v * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_10d_base_v102_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 10)
    result = v * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_21d_base_v103_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 21)
    result = v * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_42d_base_v104_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 42)
    result = v * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_63d_base_v105_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 63)
    result = v * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_126d_base_v106_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 126)
    result = v * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_189d_base_v107_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 189)
    result = v * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_252d_base_v108_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 252)
    result = v * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_378d_base_v109_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 378)
    result = v * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_504d_base_v110_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 504)
    result = v * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_mean_5d_base_v111_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 5)
    result = _mean(v, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_mean_10d_base_v112_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 10)
    result = _mean(v, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_mean_21d_base_v113_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 21)
    result = _mean(v, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_mean_42d_base_v114_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 42)
    result = _mean(v, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_mean_63d_base_v115_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 63)
    result = _mean(v, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_mean_126d_base_v116_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 126)
    result = _mean(v, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_mean_189d_base_v117_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 189)
    result = _mean(v, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_mean_252d_base_v118_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 252)
    result = _mean(v, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_mean_378d_base_v119_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 378)
    result = _mean(v, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_mean_504d_base_v120_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 504)
    result = _mean(v, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_std_5d_base_v121_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 5)
    result = _std(v, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_std_10d_base_v122_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 10)
    result = _std(v, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_std_21d_base_v123_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 21)
    result = _std(v, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_std_42d_base_v124_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 42)
    result = _std(v, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_std_63d_base_v125_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 63)
    result = _std(v, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_std_126d_base_v126_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 126)
    result = _std(v, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_std_189d_base_v127_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 189)
    result = _std(v, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_std_252d_base_v128_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 252)
    result = _std(v, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_std_378d_base_v129_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 378)
    result = _std(v, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_std_504d_base_v130_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 504)
    result = _std(v, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xrev_5d_base_v131_signal(inventory, cor, revenue, closeadj):
    v = _f08_inv_velocity(inventory, cor, 5)
    result = v * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xrev_10d_base_v132_signal(inventory, cor, revenue, closeadj):
    v = _f08_inv_velocity(inventory, cor, 10)
    result = v * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xrev_21d_base_v133_signal(inventory, cor, revenue, closeadj):
    v = _f08_inv_velocity(inventory, cor, 21)
    result = v * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xrev_42d_base_v134_signal(inventory, cor, revenue, closeadj):
    v = _f08_inv_velocity(inventory, cor, 42)
    result = v * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xrev_63d_base_v135_signal(inventory, cor, revenue, closeadj):
    v = _f08_inv_velocity(inventory, cor, 63)
    result = v * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xrev_126d_base_v136_signal(inventory, cor, revenue, closeadj):
    v = _f08_inv_velocity(inventory, cor, 126)
    result = v * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xrev_189d_base_v137_signal(inventory, cor, revenue, closeadj):
    v = _f08_inv_velocity(inventory, cor, 189)
    result = v * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xrev_252d_base_v138_signal(inventory, cor, revenue, closeadj):
    v = _f08_inv_velocity(inventory, cor, 252)
    result = v * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xrev_378d_base_v139_signal(inventory, cor, revenue, closeadj):
    v = _f08_inv_velocity(inventory, cor, 378)
    result = v * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xrev_504d_base_v140_signal(inventory, cor, revenue, closeadj):
    v = _f08_inv_velocity(inventory, cor, 504)
    result = v * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xinv_5d_base_v141_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 5)
    result = v * (inventory / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xinv_10d_base_v142_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 10)
    result = v * (inventory / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xinv_21d_base_v143_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 21)
    result = v * (inventory / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xinv_42d_base_v144_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 42)
    result = v * (inventory / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xinv_63d_base_v145_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 63)
    result = v * (inventory / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xinv_126d_base_v146_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 126)
    result = v * (inventory / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xinv_189d_base_v147_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 189)
    result = v * (inventory / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xinv_252d_base_v148_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 252)
    result = v * (inventory / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xinv_378d_base_v149_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 378)
    result = v * (inventory / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08rif_f08_retail_inventory_freshness_velo_xinv_504d_base_v150_signal(inventory, cor, closeadj):
    v = _f08_inv_velocity(inventory, cor, 504)
    result = v * (inventory / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f08rif_f08_retail_inventory_freshness_fresh_std_126d_base_v076_signal,
    f08rif_f08_retail_inventory_freshness_fresh_std_189d_base_v077_signal,
    f08rif_f08_retail_inventory_freshness_fresh_std_252d_base_v078_signal,
    f08rif_f08_retail_inventory_freshness_fresh_std_378d_base_v079_signal,
    f08rif_f08_retail_inventory_freshness_fresh_std_504d_base_v080_signal,
    f08rif_f08_retail_inventory_freshness_fresh_z_5d_base_v081_signal,
    f08rif_f08_retail_inventory_freshness_fresh_z_10d_base_v082_signal,
    f08rif_f08_retail_inventory_freshness_fresh_z_21d_base_v083_signal,
    f08rif_f08_retail_inventory_freshness_fresh_z_42d_base_v084_signal,
    f08rif_f08_retail_inventory_freshness_fresh_z_63d_base_v085_signal,
    f08rif_f08_retail_inventory_freshness_fresh_z_126d_base_v086_signal,
    f08rif_f08_retail_inventory_freshness_fresh_z_189d_base_v087_signal,
    f08rif_f08_retail_inventory_freshness_fresh_z_252d_base_v088_signal,
    f08rif_f08_retail_inventory_freshness_fresh_z_378d_base_v089_signal,
    f08rif_f08_retail_inventory_freshness_fresh_z_504d_base_v090_signal,
    f08rif_f08_retail_inventory_freshness_fresh_ema_5d_base_v091_signal,
    f08rif_f08_retail_inventory_freshness_fresh_ema_10d_base_v092_signal,
    f08rif_f08_retail_inventory_freshness_fresh_ema_21d_base_v093_signal,
    f08rif_f08_retail_inventory_freshness_fresh_ema_42d_base_v094_signal,
    f08rif_f08_retail_inventory_freshness_fresh_ema_63d_base_v095_signal,
    f08rif_f08_retail_inventory_freshness_fresh_ema_126d_base_v096_signal,
    f08rif_f08_retail_inventory_freshness_fresh_ema_189d_base_v097_signal,
    f08rif_f08_retail_inventory_freshness_fresh_ema_252d_base_v098_signal,
    f08rif_f08_retail_inventory_freshness_fresh_ema_378d_base_v099_signal,
    f08rif_f08_retail_inventory_freshness_fresh_ema_504d_base_v100_signal,
    f08rif_f08_retail_inventory_freshness_velo_5d_base_v101_signal,
    f08rif_f08_retail_inventory_freshness_velo_10d_base_v102_signal,
    f08rif_f08_retail_inventory_freshness_velo_21d_base_v103_signal,
    f08rif_f08_retail_inventory_freshness_velo_42d_base_v104_signal,
    f08rif_f08_retail_inventory_freshness_velo_63d_base_v105_signal,
    f08rif_f08_retail_inventory_freshness_velo_126d_base_v106_signal,
    f08rif_f08_retail_inventory_freshness_velo_189d_base_v107_signal,
    f08rif_f08_retail_inventory_freshness_velo_252d_base_v108_signal,
    f08rif_f08_retail_inventory_freshness_velo_378d_base_v109_signal,
    f08rif_f08_retail_inventory_freshness_velo_504d_base_v110_signal,
    f08rif_f08_retail_inventory_freshness_velo_mean_5d_base_v111_signal,
    f08rif_f08_retail_inventory_freshness_velo_mean_10d_base_v112_signal,
    f08rif_f08_retail_inventory_freshness_velo_mean_21d_base_v113_signal,
    f08rif_f08_retail_inventory_freshness_velo_mean_42d_base_v114_signal,
    f08rif_f08_retail_inventory_freshness_velo_mean_63d_base_v115_signal,
    f08rif_f08_retail_inventory_freshness_velo_mean_126d_base_v116_signal,
    f08rif_f08_retail_inventory_freshness_velo_mean_189d_base_v117_signal,
    f08rif_f08_retail_inventory_freshness_velo_mean_252d_base_v118_signal,
    f08rif_f08_retail_inventory_freshness_velo_mean_378d_base_v119_signal,
    f08rif_f08_retail_inventory_freshness_velo_mean_504d_base_v120_signal,
    f08rif_f08_retail_inventory_freshness_velo_std_5d_base_v121_signal,
    f08rif_f08_retail_inventory_freshness_velo_std_10d_base_v122_signal,
    f08rif_f08_retail_inventory_freshness_velo_std_21d_base_v123_signal,
    f08rif_f08_retail_inventory_freshness_velo_std_42d_base_v124_signal,
    f08rif_f08_retail_inventory_freshness_velo_std_63d_base_v125_signal,
    f08rif_f08_retail_inventory_freshness_velo_std_126d_base_v126_signal,
    f08rif_f08_retail_inventory_freshness_velo_std_189d_base_v127_signal,
    f08rif_f08_retail_inventory_freshness_velo_std_252d_base_v128_signal,
    f08rif_f08_retail_inventory_freshness_velo_std_378d_base_v129_signal,
    f08rif_f08_retail_inventory_freshness_velo_std_504d_base_v130_signal,
    f08rif_f08_retail_inventory_freshness_velo_xrev_5d_base_v131_signal,
    f08rif_f08_retail_inventory_freshness_velo_xrev_10d_base_v132_signal,
    f08rif_f08_retail_inventory_freshness_velo_xrev_21d_base_v133_signal,
    f08rif_f08_retail_inventory_freshness_velo_xrev_42d_base_v134_signal,
    f08rif_f08_retail_inventory_freshness_velo_xrev_63d_base_v135_signal,
    f08rif_f08_retail_inventory_freshness_velo_xrev_126d_base_v136_signal,
    f08rif_f08_retail_inventory_freshness_velo_xrev_189d_base_v137_signal,
    f08rif_f08_retail_inventory_freshness_velo_xrev_252d_base_v138_signal,
    f08rif_f08_retail_inventory_freshness_velo_xrev_378d_base_v139_signal,
    f08rif_f08_retail_inventory_freshness_velo_xrev_504d_base_v140_signal,
    f08rif_f08_retail_inventory_freshness_velo_xinv_5d_base_v141_signal,
    f08rif_f08_retail_inventory_freshness_velo_xinv_10d_base_v142_signal,
    f08rif_f08_retail_inventory_freshness_velo_xinv_21d_base_v143_signal,
    f08rif_f08_retail_inventory_freshness_velo_xinv_42d_base_v144_signal,
    f08rif_f08_retail_inventory_freshness_velo_xinv_63d_base_v145_signal,
    f08rif_f08_retail_inventory_freshness_velo_xinv_126d_base_v146_signal,
    f08rif_f08_retail_inventory_freshness_velo_xinv_189d_base_v147_signal,
    f08rif_f08_retail_inventory_freshness_velo_xinv_252d_base_v148_signal,
    f08rif_f08_retail_inventory_freshness_velo_xinv_378d_base_v149_signal,
    f08rif_f08_retail_inventory_freshness_velo_xinv_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_RETAIL_INVENTORY_FRESHNESS_REGISTRY_076_150 = REGISTRY


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
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "inventory": inventory, "ppnenet": ppnenet,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f08_inventory_turnover", "_f08_inventory_freshness", "_f08_inv_velocity")
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
    print(f"OK f08_retail_inventory_freshness_076_150_claude: {n_features} features pass")
