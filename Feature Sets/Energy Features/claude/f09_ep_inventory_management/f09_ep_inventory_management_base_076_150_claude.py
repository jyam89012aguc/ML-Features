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
def _f09_inv_days(inventory, cor):
    return inventory / cor.replace(0, np.nan) * 365.0


def _f09_inv_to_revenue(inventory, revenue):
    return inventory / revenue.replace(0, np.nan)


def _f09_inv_dynamics(inventory, revenue, w):
    ratio = inventory / revenue.replace(0, np.nan)
    return ratio.rolling(w, min_periods=max(1, w // 2)).mean()


# ===== features =====

# id invxcl w=504
def f09eim_f09_ep_inventory_management_idinvxcl_504d_base_v076_signal(inventory, cor, closeadj):
    result = (1.0 / _f09_inv_days(inventory, cor).replace(0, np.nan)) * closeadj
    result = result + 0.0 * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# id meanxcl w=504
def f09eim_f09_ep_inventory_management_idmeanxcl_504d_base_v077_signal(inventory, cor, closeadj):
    result = _mean(_f09_inv_days(inventory, cor), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id zxcl w=504
def f09eim_f09_ep_inventory_management_idzxcl_504d_base_v078_signal(inventory, cor, closeadj):
    result = _z(_f09_inv_days(inventory, cor), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id stdxcl w=504
def f09eim_f09_ep_inventory_management_idstdxcl_504d_base_v079_signal(inventory, cor, closeadj):
    result = _std(_f09_inv_days(inventory, cor), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# id ratiomean w=504
def f09eim_f09_ep_inventory_management_idratiomean_504d_base_v080_signal(inventory, cor, closeadj):
    base = _f09_inv_days(inventory, cor)
    result = (base / _mean(base, 504).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir idxcl w=5
def f09eim_f09_ep_inventory_management_iridxcl_5d_base_v081_signal(inventory, revenue, closeadj):
    result = _f09_inv_to_revenue(inventory, revenue) * closeadj
    result = result + 0.0 * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ir logxcl w=5
def f09eim_f09_ep_inventory_management_irlogxcl_5d_base_v082_signal(inventory, revenue, closeadj):
    result = np.log1p(_f09_inv_to_revenue(inventory, revenue).abs()) * closeadj
    result = result + 0.0 * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ir sqxcl w=5
def f09eim_f09_ep_inventory_management_irsqxcl_5d_base_v083_signal(inventory, revenue, closeadj):
    result = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj
    result = result + 0.0 * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ir invxcl w=5
def f09eim_f09_ep_inventory_management_irinvxcl_5d_base_v084_signal(inventory, revenue, closeadj):
    result = (1.0 / _f09_inv_to_revenue(inventory, revenue).replace(0, np.nan)) * closeadj
    result = result + 0.0 * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ir meanxcl w=5
def f09eim_f09_ep_inventory_management_irmeanxcl_5d_base_v085_signal(inventory, revenue, closeadj):
    result = _mean(_f09_inv_to_revenue(inventory, revenue), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir zxcl w=5
def f09eim_f09_ep_inventory_management_irzxcl_5d_base_v086_signal(inventory, revenue, closeadj):
    result = _z(_f09_inv_to_revenue(inventory, revenue), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir stdxcl w=5
def f09eim_f09_ep_inventory_management_irstdxcl_5d_base_v087_signal(inventory, revenue, closeadj):
    result = _std(_f09_inv_to_revenue(inventory, revenue), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir ratiomean w=5
def f09eim_f09_ep_inventory_management_irratiomean_5d_base_v088_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    result = (base / _mean(base, 5).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir idxcl w=10
def f09eim_f09_ep_inventory_management_iridxcl_10d_base_v089_signal(inventory, revenue, closeadj):
    result = _f09_inv_to_revenue(inventory, revenue) * closeadj
    result = result + 0.0 * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ir logxcl w=10
def f09eim_f09_ep_inventory_management_irlogxcl_10d_base_v090_signal(inventory, revenue, closeadj):
    result = np.log1p(_f09_inv_to_revenue(inventory, revenue).abs()) * closeadj
    result = result + 0.0 * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ir sqxcl w=10
def f09eim_f09_ep_inventory_management_irsqxcl_10d_base_v091_signal(inventory, revenue, closeadj):
    result = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj
    result = result + 0.0 * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ir invxcl w=10
def f09eim_f09_ep_inventory_management_irinvxcl_10d_base_v092_signal(inventory, revenue, closeadj):
    result = (1.0 / _f09_inv_to_revenue(inventory, revenue).replace(0, np.nan)) * closeadj
    result = result + 0.0 * _mean(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ir meanxcl w=10
def f09eim_f09_ep_inventory_management_irmeanxcl_10d_base_v093_signal(inventory, revenue, closeadj):
    result = _mean(_f09_inv_to_revenue(inventory, revenue), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir zxcl w=10
def f09eim_f09_ep_inventory_management_irzxcl_10d_base_v094_signal(inventory, revenue, closeadj):
    result = _z(_f09_inv_to_revenue(inventory, revenue), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir stdxcl w=10
def f09eim_f09_ep_inventory_management_irstdxcl_10d_base_v095_signal(inventory, revenue, closeadj):
    result = _std(_f09_inv_to_revenue(inventory, revenue), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir ratiomean w=10
def f09eim_f09_ep_inventory_management_irratiomean_10d_base_v096_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    result = (base / _mean(base, 10).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir idxcl w=21
def f09eim_f09_ep_inventory_management_iridxcl_21d_base_v097_signal(inventory, revenue, closeadj):
    result = _f09_inv_to_revenue(inventory, revenue) * closeadj
    result = result + 0.0 * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ir logxcl w=21
def f09eim_f09_ep_inventory_management_irlogxcl_21d_base_v098_signal(inventory, revenue, closeadj):
    result = np.log1p(_f09_inv_to_revenue(inventory, revenue).abs()) * closeadj
    result = result + 0.0 * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ir sqxcl w=21
def f09eim_f09_ep_inventory_management_irsqxcl_21d_base_v099_signal(inventory, revenue, closeadj):
    result = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj
    result = result + 0.0 * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ir invxcl w=21
def f09eim_f09_ep_inventory_management_irinvxcl_21d_base_v100_signal(inventory, revenue, closeadj):
    result = (1.0 / _f09_inv_to_revenue(inventory, revenue).replace(0, np.nan)) * closeadj
    result = result + 0.0 * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ir meanxcl w=21
def f09eim_f09_ep_inventory_management_irmeanxcl_21d_base_v101_signal(inventory, revenue, closeadj):
    result = _mean(_f09_inv_to_revenue(inventory, revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir zxcl w=21
def f09eim_f09_ep_inventory_management_irzxcl_21d_base_v102_signal(inventory, revenue, closeadj):
    result = _z(_f09_inv_to_revenue(inventory, revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir stdxcl w=21
def f09eim_f09_ep_inventory_management_irstdxcl_21d_base_v103_signal(inventory, revenue, closeadj):
    result = _std(_f09_inv_to_revenue(inventory, revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir ratiomean w=21
def f09eim_f09_ep_inventory_management_irratiomean_21d_base_v104_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    result = (base / _mean(base, 21).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir idxcl w=42
def f09eim_f09_ep_inventory_management_iridxcl_42d_base_v105_signal(inventory, revenue, closeadj):
    result = _f09_inv_to_revenue(inventory, revenue) * closeadj
    result = result + 0.0 * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ir logxcl w=42
def f09eim_f09_ep_inventory_management_irlogxcl_42d_base_v106_signal(inventory, revenue, closeadj):
    result = np.log1p(_f09_inv_to_revenue(inventory, revenue).abs()) * closeadj
    result = result + 0.0 * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ir sqxcl w=42
def f09eim_f09_ep_inventory_management_irsqxcl_42d_base_v107_signal(inventory, revenue, closeadj):
    result = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj
    result = result + 0.0 * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ir invxcl w=42
def f09eim_f09_ep_inventory_management_irinvxcl_42d_base_v108_signal(inventory, revenue, closeadj):
    result = (1.0 / _f09_inv_to_revenue(inventory, revenue).replace(0, np.nan)) * closeadj
    result = result + 0.0 * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ir meanxcl w=42
def f09eim_f09_ep_inventory_management_irmeanxcl_42d_base_v109_signal(inventory, revenue, closeadj):
    result = _mean(_f09_inv_to_revenue(inventory, revenue), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir zxcl w=42
def f09eim_f09_ep_inventory_management_irzxcl_42d_base_v110_signal(inventory, revenue, closeadj):
    result = _z(_f09_inv_to_revenue(inventory, revenue), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir stdxcl w=42
def f09eim_f09_ep_inventory_management_irstdxcl_42d_base_v111_signal(inventory, revenue, closeadj):
    result = _std(_f09_inv_to_revenue(inventory, revenue), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir ratiomean w=42
def f09eim_f09_ep_inventory_management_irratiomean_42d_base_v112_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    result = (base / _mean(base, 42).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir idxcl w=63
def f09eim_f09_ep_inventory_management_iridxcl_63d_base_v113_signal(inventory, revenue, closeadj):
    result = _f09_inv_to_revenue(inventory, revenue) * closeadj
    result = result + 0.0 * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ir logxcl w=63
def f09eim_f09_ep_inventory_management_irlogxcl_63d_base_v114_signal(inventory, revenue, closeadj):
    result = np.log1p(_f09_inv_to_revenue(inventory, revenue).abs()) * closeadj
    result = result + 0.0 * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ir sqxcl w=63
def f09eim_f09_ep_inventory_management_irsqxcl_63d_base_v115_signal(inventory, revenue, closeadj):
    result = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj
    result = result + 0.0 * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ir invxcl w=63
def f09eim_f09_ep_inventory_management_irinvxcl_63d_base_v116_signal(inventory, revenue, closeadj):
    result = (1.0 / _f09_inv_to_revenue(inventory, revenue).replace(0, np.nan)) * closeadj
    result = result + 0.0 * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ir meanxcl w=63
def f09eim_f09_ep_inventory_management_irmeanxcl_63d_base_v117_signal(inventory, revenue, closeadj):
    result = _mean(_f09_inv_to_revenue(inventory, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir zxcl w=63
def f09eim_f09_ep_inventory_management_irzxcl_63d_base_v118_signal(inventory, revenue, closeadj):
    result = _z(_f09_inv_to_revenue(inventory, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir stdxcl w=63
def f09eim_f09_ep_inventory_management_irstdxcl_63d_base_v119_signal(inventory, revenue, closeadj):
    result = _std(_f09_inv_to_revenue(inventory, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir ratiomean w=63
def f09eim_f09_ep_inventory_management_irratiomean_63d_base_v120_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    result = (base / _mean(base, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir idxcl w=126
def f09eim_f09_ep_inventory_management_iridxcl_126d_base_v121_signal(inventory, revenue, closeadj):
    result = _f09_inv_to_revenue(inventory, revenue) * closeadj
    result = result + 0.0 * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ir logxcl w=126
def f09eim_f09_ep_inventory_management_irlogxcl_126d_base_v122_signal(inventory, revenue, closeadj):
    result = np.log1p(_f09_inv_to_revenue(inventory, revenue).abs()) * closeadj
    result = result + 0.0 * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ir sqxcl w=126
def f09eim_f09_ep_inventory_management_irsqxcl_126d_base_v123_signal(inventory, revenue, closeadj):
    result = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj
    result = result + 0.0 * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ir invxcl w=126
def f09eim_f09_ep_inventory_management_irinvxcl_126d_base_v124_signal(inventory, revenue, closeadj):
    result = (1.0 / _f09_inv_to_revenue(inventory, revenue).replace(0, np.nan)) * closeadj
    result = result + 0.0 * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ir meanxcl w=126
def f09eim_f09_ep_inventory_management_irmeanxcl_126d_base_v125_signal(inventory, revenue, closeadj):
    result = _mean(_f09_inv_to_revenue(inventory, revenue), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir zxcl w=126
def f09eim_f09_ep_inventory_management_irzxcl_126d_base_v126_signal(inventory, revenue, closeadj):
    result = _z(_f09_inv_to_revenue(inventory, revenue), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir stdxcl w=126
def f09eim_f09_ep_inventory_management_irstdxcl_126d_base_v127_signal(inventory, revenue, closeadj):
    result = _std(_f09_inv_to_revenue(inventory, revenue), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir ratiomean w=126
def f09eim_f09_ep_inventory_management_irratiomean_126d_base_v128_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    result = (base / _mean(base, 126).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir idxcl w=189
def f09eim_f09_ep_inventory_management_iridxcl_189d_base_v129_signal(inventory, revenue, closeadj):
    result = _f09_inv_to_revenue(inventory, revenue) * closeadj
    result = result + 0.0 * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# ir logxcl w=189
def f09eim_f09_ep_inventory_management_irlogxcl_189d_base_v130_signal(inventory, revenue, closeadj):
    result = np.log1p(_f09_inv_to_revenue(inventory, revenue).abs()) * closeadj
    result = result + 0.0 * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# ir sqxcl w=189
def f09eim_f09_ep_inventory_management_irsqxcl_189d_base_v131_signal(inventory, revenue, closeadj):
    result = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj
    result = result + 0.0 * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# ir invxcl w=189
def f09eim_f09_ep_inventory_management_irinvxcl_189d_base_v132_signal(inventory, revenue, closeadj):
    result = (1.0 / _f09_inv_to_revenue(inventory, revenue).replace(0, np.nan)) * closeadj
    result = result + 0.0 * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# ir meanxcl w=189
def f09eim_f09_ep_inventory_management_irmeanxcl_189d_base_v133_signal(inventory, revenue, closeadj):
    result = _mean(_f09_inv_to_revenue(inventory, revenue), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir zxcl w=189
def f09eim_f09_ep_inventory_management_irzxcl_189d_base_v134_signal(inventory, revenue, closeadj):
    result = _z(_f09_inv_to_revenue(inventory, revenue), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir stdxcl w=189
def f09eim_f09_ep_inventory_management_irstdxcl_189d_base_v135_signal(inventory, revenue, closeadj):
    result = _std(_f09_inv_to_revenue(inventory, revenue), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir ratiomean w=189
def f09eim_f09_ep_inventory_management_irratiomean_189d_base_v136_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    result = (base / _mean(base, 189).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir idxcl w=252
def f09eim_f09_ep_inventory_management_iridxcl_252d_base_v137_signal(inventory, revenue, closeadj):
    result = _f09_inv_to_revenue(inventory, revenue) * closeadj
    result = result + 0.0 * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ir logxcl w=252
def f09eim_f09_ep_inventory_management_irlogxcl_252d_base_v138_signal(inventory, revenue, closeadj):
    result = np.log1p(_f09_inv_to_revenue(inventory, revenue).abs()) * closeadj
    result = result + 0.0 * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ir sqxcl w=252
def f09eim_f09_ep_inventory_management_irsqxcl_252d_base_v139_signal(inventory, revenue, closeadj):
    result = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj
    result = result + 0.0 * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ir invxcl w=252
def f09eim_f09_ep_inventory_management_irinvxcl_252d_base_v140_signal(inventory, revenue, closeadj):
    result = (1.0 / _f09_inv_to_revenue(inventory, revenue).replace(0, np.nan)) * closeadj
    result = result + 0.0 * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ir meanxcl w=252
def f09eim_f09_ep_inventory_management_irmeanxcl_252d_base_v141_signal(inventory, revenue, closeadj):
    result = _mean(_f09_inv_to_revenue(inventory, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir zxcl w=252
def f09eim_f09_ep_inventory_management_irzxcl_252d_base_v142_signal(inventory, revenue, closeadj):
    result = _z(_f09_inv_to_revenue(inventory, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir stdxcl w=252
def f09eim_f09_ep_inventory_management_irstdxcl_252d_base_v143_signal(inventory, revenue, closeadj):
    result = _std(_f09_inv_to_revenue(inventory, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir ratiomean w=252
def f09eim_f09_ep_inventory_management_irratiomean_252d_base_v144_signal(inventory, revenue, closeadj):
    base = _f09_inv_to_revenue(inventory, revenue)
    result = (base / _mean(base, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir idxcl w=378
def f09eim_f09_ep_inventory_management_iridxcl_378d_base_v145_signal(inventory, revenue, closeadj):
    result = _f09_inv_to_revenue(inventory, revenue) * closeadj
    result = result + 0.0 * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# ir logxcl w=378
def f09eim_f09_ep_inventory_management_irlogxcl_378d_base_v146_signal(inventory, revenue, closeadj):
    result = np.log1p(_f09_inv_to_revenue(inventory, revenue).abs()) * closeadj
    result = result + 0.0 * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# ir sqxcl w=378
def f09eim_f09_ep_inventory_management_irsqxcl_378d_base_v147_signal(inventory, revenue, closeadj):
    result = (_f09_inv_to_revenue(inventory, revenue) ** 2) * closeadj
    result = result + 0.0 * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# ir invxcl w=378
def f09eim_f09_ep_inventory_management_irinvxcl_378d_base_v148_signal(inventory, revenue, closeadj):
    result = (1.0 / _f09_inv_to_revenue(inventory, revenue).replace(0, np.nan)) * closeadj
    result = result + 0.0 * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# ir meanxcl w=378
def f09eim_f09_ep_inventory_management_irmeanxcl_378d_base_v149_signal(inventory, revenue, closeadj):
    result = _mean(_f09_inv_to_revenue(inventory, revenue), 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ir zxcl w=378
def f09eim_f09_ep_inventory_management_irzxcl_378d_base_v150_signal(inventory, revenue, closeadj):
    result = _z(_f09_inv_to_revenue(inventory, revenue), 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f09eim_f09_ep_inventory_management_idinvxcl_504d_base_v076_signal,
    f09eim_f09_ep_inventory_management_idmeanxcl_504d_base_v077_signal,
    f09eim_f09_ep_inventory_management_idzxcl_504d_base_v078_signal,
    f09eim_f09_ep_inventory_management_idstdxcl_504d_base_v079_signal,
    f09eim_f09_ep_inventory_management_idratiomean_504d_base_v080_signal,
    f09eim_f09_ep_inventory_management_iridxcl_5d_base_v081_signal,
    f09eim_f09_ep_inventory_management_irlogxcl_5d_base_v082_signal,
    f09eim_f09_ep_inventory_management_irsqxcl_5d_base_v083_signal,
    f09eim_f09_ep_inventory_management_irinvxcl_5d_base_v084_signal,
    f09eim_f09_ep_inventory_management_irmeanxcl_5d_base_v085_signal,
    f09eim_f09_ep_inventory_management_irzxcl_5d_base_v086_signal,
    f09eim_f09_ep_inventory_management_irstdxcl_5d_base_v087_signal,
    f09eim_f09_ep_inventory_management_irratiomean_5d_base_v088_signal,
    f09eim_f09_ep_inventory_management_iridxcl_10d_base_v089_signal,
    f09eim_f09_ep_inventory_management_irlogxcl_10d_base_v090_signal,
    f09eim_f09_ep_inventory_management_irsqxcl_10d_base_v091_signal,
    f09eim_f09_ep_inventory_management_irinvxcl_10d_base_v092_signal,
    f09eim_f09_ep_inventory_management_irmeanxcl_10d_base_v093_signal,
    f09eim_f09_ep_inventory_management_irzxcl_10d_base_v094_signal,
    f09eim_f09_ep_inventory_management_irstdxcl_10d_base_v095_signal,
    f09eim_f09_ep_inventory_management_irratiomean_10d_base_v096_signal,
    f09eim_f09_ep_inventory_management_iridxcl_21d_base_v097_signal,
    f09eim_f09_ep_inventory_management_irlogxcl_21d_base_v098_signal,
    f09eim_f09_ep_inventory_management_irsqxcl_21d_base_v099_signal,
    f09eim_f09_ep_inventory_management_irinvxcl_21d_base_v100_signal,
    f09eim_f09_ep_inventory_management_irmeanxcl_21d_base_v101_signal,
    f09eim_f09_ep_inventory_management_irzxcl_21d_base_v102_signal,
    f09eim_f09_ep_inventory_management_irstdxcl_21d_base_v103_signal,
    f09eim_f09_ep_inventory_management_irratiomean_21d_base_v104_signal,
    f09eim_f09_ep_inventory_management_iridxcl_42d_base_v105_signal,
    f09eim_f09_ep_inventory_management_irlogxcl_42d_base_v106_signal,
    f09eim_f09_ep_inventory_management_irsqxcl_42d_base_v107_signal,
    f09eim_f09_ep_inventory_management_irinvxcl_42d_base_v108_signal,
    f09eim_f09_ep_inventory_management_irmeanxcl_42d_base_v109_signal,
    f09eim_f09_ep_inventory_management_irzxcl_42d_base_v110_signal,
    f09eim_f09_ep_inventory_management_irstdxcl_42d_base_v111_signal,
    f09eim_f09_ep_inventory_management_irratiomean_42d_base_v112_signal,
    f09eim_f09_ep_inventory_management_iridxcl_63d_base_v113_signal,
    f09eim_f09_ep_inventory_management_irlogxcl_63d_base_v114_signal,
    f09eim_f09_ep_inventory_management_irsqxcl_63d_base_v115_signal,
    f09eim_f09_ep_inventory_management_irinvxcl_63d_base_v116_signal,
    f09eim_f09_ep_inventory_management_irmeanxcl_63d_base_v117_signal,
    f09eim_f09_ep_inventory_management_irzxcl_63d_base_v118_signal,
    f09eim_f09_ep_inventory_management_irstdxcl_63d_base_v119_signal,
    f09eim_f09_ep_inventory_management_irratiomean_63d_base_v120_signal,
    f09eim_f09_ep_inventory_management_iridxcl_126d_base_v121_signal,
    f09eim_f09_ep_inventory_management_irlogxcl_126d_base_v122_signal,
    f09eim_f09_ep_inventory_management_irsqxcl_126d_base_v123_signal,
    f09eim_f09_ep_inventory_management_irinvxcl_126d_base_v124_signal,
    f09eim_f09_ep_inventory_management_irmeanxcl_126d_base_v125_signal,
    f09eim_f09_ep_inventory_management_irzxcl_126d_base_v126_signal,
    f09eim_f09_ep_inventory_management_irstdxcl_126d_base_v127_signal,
    f09eim_f09_ep_inventory_management_irratiomean_126d_base_v128_signal,
    f09eim_f09_ep_inventory_management_iridxcl_189d_base_v129_signal,
    f09eim_f09_ep_inventory_management_irlogxcl_189d_base_v130_signal,
    f09eim_f09_ep_inventory_management_irsqxcl_189d_base_v131_signal,
    f09eim_f09_ep_inventory_management_irinvxcl_189d_base_v132_signal,
    f09eim_f09_ep_inventory_management_irmeanxcl_189d_base_v133_signal,
    f09eim_f09_ep_inventory_management_irzxcl_189d_base_v134_signal,
    f09eim_f09_ep_inventory_management_irstdxcl_189d_base_v135_signal,
    f09eim_f09_ep_inventory_management_irratiomean_189d_base_v136_signal,
    f09eim_f09_ep_inventory_management_iridxcl_252d_base_v137_signal,
    f09eim_f09_ep_inventory_management_irlogxcl_252d_base_v138_signal,
    f09eim_f09_ep_inventory_management_irsqxcl_252d_base_v139_signal,
    f09eim_f09_ep_inventory_management_irinvxcl_252d_base_v140_signal,
    f09eim_f09_ep_inventory_management_irmeanxcl_252d_base_v141_signal,
    f09eim_f09_ep_inventory_management_irzxcl_252d_base_v142_signal,
    f09eim_f09_ep_inventory_management_irstdxcl_252d_base_v143_signal,
    f09eim_f09_ep_inventory_management_irratiomean_252d_base_v144_signal,
    f09eim_f09_ep_inventory_management_iridxcl_378d_base_v145_signal,
    f09eim_f09_ep_inventory_management_irlogxcl_378d_base_v146_signal,
    f09eim_f09_ep_inventory_management_irsqxcl_378d_base_v147_signal,
    f09eim_f09_ep_inventory_management_irinvxcl_378d_base_v148_signal,
    f09eim_f09_ep_inventory_management_irmeanxcl_378d_base_v149_signal,
    f09eim_f09_ep_inventory_management_irzxcl_378d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_EP_INVENTORY_MANAGEMENT_REGISTRY_076_150 = REGISTRY


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
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f09_inv_days", "_f09_inv_to_revenue", "_f09_inv_dynamics")
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
    print(f"OK f09_ep_inventory_management_base_076_150_claude: {n_features} features pass")
