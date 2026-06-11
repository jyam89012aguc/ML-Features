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
def _f10_comp_growth_durability(revenue, ppnenet, w):
    rpp = revenue / ppnenet.replace(0, np.nan)
    g = rpp.pct_change(periods=w)
    return g.rolling(w, min_periods=max(1, w // 2)).mean()


def _f10_comp_floor(revenue, ppnenet, w):
    rpp = revenue / ppnenet.replace(0, np.nan)
    g = rpp.pct_change(periods=w)
    return g.rolling(w, min_periods=max(1, w // 2)).min()


def _f10_comp_stability(revenue, w):
    g = revenue.pct_change(periods=w)
    m = g.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = g.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)

def f10rcd_f10_retail_comp_dynamics_floor_std_84d_base_v076_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 84)
    result = _std(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_std_105d_base_v077_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 105)
    result = _std(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_std_126d_base_v078_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 126)
    result = _std(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_std_168d_base_v079_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 168)
    result = _std(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_std_189d_base_v080_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 189)
    result = _std(f, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_z_5d_base_v081_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 5)
    result = _z(f, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_z_10d_base_v082_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 10)
    result = _z(f, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_z_21d_base_v083_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 21)
    result = _z(f, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_z_42d_base_v084_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 42)
    result = _z(f, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_z_63d_base_v085_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 63)
    result = _z(f, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_z_84d_base_v086_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 84)
    result = _z(f, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_z_105d_base_v087_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 105)
    result = _z(f, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_z_126d_base_v088_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 126)
    result = _z(f, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_z_168d_base_v089_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 168)
    result = _z(f, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_z_189d_base_v090_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 189)
    result = _z(f, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_diff_5d_base_v091_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 5)
    result = (f - f.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_diff_10d_base_v092_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 10)
    result = (f - f.shift(10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_diff_21d_base_v093_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 21)
    result = (f - f.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_diff_42d_base_v094_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 42)
    result = (f - f.shift(42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_diff_63d_base_v095_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 63)
    result = (f - f.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_diff_84d_base_v096_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 84)
    result = (f - f.shift(84)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_diff_105d_base_v097_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 105)
    result = (f - f.shift(105)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_diff_126d_base_v098_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 126)
    result = (f - f.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_diff_168d_base_v099_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 168)
    result = (f - f.shift(168)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_floor_diff_189d_base_v100_signal(revenue, ppnenet, closeadj):
    f = _f10_comp_floor(revenue, ppnenet, 189)
    result = (f - f.shift(189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_5d_base_v101_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 5)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_10d_base_v102_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 10)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_21d_base_v103_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 21)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_42d_base_v104_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 42)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_63d_base_v105_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 63)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_126d_base_v106_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 126)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_189d_base_v107_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 189)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_252d_base_v108_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 252)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_378d_base_v109_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 378)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_504d_base_v110_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 504)
    result = s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_mean_5d_base_v111_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 5)
    result = _mean(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_mean_10d_base_v112_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 10)
    result = _mean(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_mean_21d_base_v113_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 21)
    result = _mean(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_mean_42d_base_v114_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 42)
    result = _mean(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_mean_63d_base_v115_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 63)
    result = _mean(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_mean_126d_base_v116_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 126)
    result = _mean(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_mean_189d_base_v117_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 189)
    result = _mean(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_mean_252d_base_v118_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 252)
    result = _mean(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_mean_378d_base_v119_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 378)
    result = _mean(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_mean_504d_base_v120_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 504)
    result = _mean(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_std_5d_base_v121_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 5)
    result = _std(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_std_10d_base_v122_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 10)
    result = _std(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_std_21d_base_v123_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 21)
    result = _std(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_std_42d_base_v124_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 42)
    result = _std(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_std_63d_base_v125_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 63)
    result = _std(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_std_126d_base_v126_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 126)
    result = _std(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_std_189d_base_v127_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 189)
    result = _std(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_std_252d_base_v128_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 252)
    result = _std(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_std_378d_base_v129_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 378)
    result = _std(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_std_504d_base_v130_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 504)
    result = _std(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_z_5d_base_v131_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 5)
    result = _z(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_z_10d_base_v132_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 10)
    result = _z(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_z_21d_base_v133_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 21)
    result = _z(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_z_42d_base_v134_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 42)
    result = _z(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_z_63d_base_v135_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 63)
    result = _z(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_z_126d_base_v136_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 126)
    result = _z(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_z_189d_base_v137_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 189)
    result = _z(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_z_252d_base_v138_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 252)
    result = _z(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_z_378d_base_v139_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 378)
    result = _z(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_z_504d_base_v140_signal(revenue, closeadj):
    s = _f10_comp_stability(revenue, 504)
    result = _z(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_xppe_5d_base_v141_signal(revenue, ppnenet, closeadj):
    s = _f10_comp_stability(revenue, 5)
    result = s * (ppnenet / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_xppe_10d_base_v142_signal(revenue, ppnenet, closeadj):
    s = _f10_comp_stability(revenue, 10)
    result = s * (ppnenet / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_xppe_21d_base_v143_signal(revenue, ppnenet, closeadj):
    s = _f10_comp_stability(revenue, 21)
    result = s * (ppnenet / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_xppe_42d_base_v144_signal(revenue, ppnenet, closeadj):
    s = _f10_comp_stability(revenue, 42)
    result = s * (ppnenet / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_xppe_63d_base_v145_signal(revenue, ppnenet, closeadj):
    s = _f10_comp_stability(revenue, 63)
    result = s * (ppnenet / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_xppe_126d_base_v146_signal(revenue, ppnenet, closeadj):
    s = _f10_comp_stability(revenue, 126)
    result = s * (ppnenet / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_xppe_189d_base_v147_signal(revenue, ppnenet, closeadj):
    s = _f10_comp_stability(revenue, 189)
    result = s * (ppnenet / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_xppe_252d_base_v148_signal(revenue, ppnenet, closeadj):
    s = _f10_comp_stability(revenue, 252)
    result = s * (ppnenet / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_xppe_378d_base_v149_signal(revenue, ppnenet, closeadj):
    s = _f10_comp_stability(revenue, 378)
    result = s * (ppnenet / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f10rcd_f10_retail_comp_dynamics_stab_xppe_504d_base_v150_signal(revenue, ppnenet, closeadj):
    s = _f10_comp_stability(revenue, 504)
    result = s * (ppnenet / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f10rcd_f10_retail_comp_dynamics_floor_std_84d_base_v076_signal,
    f10rcd_f10_retail_comp_dynamics_floor_std_105d_base_v077_signal,
    f10rcd_f10_retail_comp_dynamics_floor_std_126d_base_v078_signal,
    f10rcd_f10_retail_comp_dynamics_floor_std_168d_base_v079_signal,
    f10rcd_f10_retail_comp_dynamics_floor_std_189d_base_v080_signal,
    f10rcd_f10_retail_comp_dynamics_floor_z_5d_base_v081_signal,
    f10rcd_f10_retail_comp_dynamics_floor_z_10d_base_v082_signal,
    f10rcd_f10_retail_comp_dynamics_floor_z_21d_base_v083_signal,
    f10rcd_f10_retail_comp_dynamics_floor_z_42d_base_v084_signal,
    f10rcd_f10_retail_comp_dynamics_floor_z_63d_base_v085_signal,
    f10rcd_f10_retail_comp_dynamics_floor_z_84d_base_v086_signal,
    f10rcd_f10_retail_comp_dynamics_floor_z_105d_base_v087_signal,
    f10rcd_f10_retail_comp_dynamics_floor_z_126d_base_v088_signal,
    f10rcd_f10_retail_comp_dynamics_floor_z_168d_base_v089_signal,
    f10rcd_f10_retail_comp_dynamics_floor_z_189d_base_v090_signal,
    f10rcd_f10_retail_comp_dynamics_floor_diff_5d_base_v091_signal,
    f10rcd_f10_retail_comp_dynamics_floor_diff_10d_base_v092_signal,
    f10rcd_f10_retail_comp_dynamics_floor_diff_21d_base_v093_signal,
    f10rcd_f10_retail_comp_dynamics_floor_diff_42d_base_v094_signal,
    f10rcd_f10_retail_comp_dynamics_floor_diff_63d_base_v095_signal,
    f10rcd_f10_retail_comp_dynamics_floor_diff_84d_base_v096_signal,
    f10rcd_f10_retail_comp_dynamics_floor_diff_105d_base_v097_signal,
    f10rcd_f10_retail_comp_dynamics_floor_diff_126d_base_v098_signal,
    f10rcd_f10_retail_comp_dynamics_floor_diff_168d_base_v099_signal,
    f10rcd_f10_retail_comp_dynamics_floor_diff_189d_base_v100_signal,
    f10rcd_f10_retail_comp_dynamics_stab_5d_base_v101_signal,
    f10rcd_f10_retail_comp_dynamics_stab_10d_base_v102_signal,
    f10rcd_f10_retail_comp_dynamics_stab_21d_base_v103_signal,
    f10rcd_f10_retail_comp_dynamics_stab_42d_base_v104_signal,
    f10rcd_f10_retail_comp_dynamics_stab_63d_base_v105_signal,
    f10rcd_f10_retail_comp_dynamics_stab_126d_base_v106_signal,
    f10rcd_f10_retail_comp_dynamics_stab_189d_base_v107_signal,
    f10rcd_f10_retail_comp_dynamics_stab_252d_base_v108_signal,
    f10rcd_f10_retail_comp_dynamics_stab_378d_base_v109_signal,
    f10rcd_f10_retail_comp_dynamics_stab_504d_base_v110_signal,
    f10rcd_f10_retail_comp_dynamics_stab_mean_5d_base_v111_signal,
    f10rcd_f10_retail_comp_dynamics_stab_mean_10d_base_v112_signal,
    f10rcd_f10_retail_comp_dynamics_stab_mean_21d_base_v113_signal,
    f10rcd_f10_retail_comp_dynamics_stab_mean_42d_base_v114_signal,
    f10rcd_f10_retail_comp_dynamics_stab_mean_63d_base_v115_signal,
    f10rcd_f10_retail_comp_dynamics_stab_mean_126d_base_v116_signal,
    f10rcd_f10_retail_comp_dynamics_stab_mean_189d_base_v117_signal,
    f10rcd_f10_retail_comp_dynamics_stab_mean_252d_base_v118_signal,
    f10rcd_f10_retail_comp_dynamics_stab_mean_378d_base_v119_signal,
    f10rcd_f10_retail_comp_dynamics_stab_mean_504d_base_v120_signal,
    f10rcd_f10_retail_comp_dynamics_stab_std_5d_base_v121_signal,
    f10rcd_f10_retail_comp_dynamics_stab_std_10d_base_v122_signal,
    f10rcd_f10_retail_comp_dynamics_stab_std_21d_base_v123_signal,
    f10rcd_f10_retail_comp_dynamics_stab_std_42d_base_v124_signal,
    f10rcd_f10_retail_comp_dynamics_stab_std_63d_base_v125_signal,
    f10rcd_f10_retail_comp_dynamics_stab_std_126d_base_v126_signal,
    f10rcd_f10_retail_comp_dynamics_stab_std_189d_base_v127_signal,
    f10rcd_f10_retail_comp_dynamics_stab_std_252d_base_v128_signal,
    f10rcd_f10_retail_comp_dynamics_stab_std_378d_base_v129_signal,
    f10rcd_f10_retail_comp_dynamics_stab_std_504d_base_v130_signal,
    f10rcd_f10_retail_comp_dynamics_stab_z_5d_base_v131_signal,
    f10rcd_f10_retail_comp_dynamics_stab_z_10d_base_v132_signal,
    f10rcd_f10_retail_comp_dynamics_stab_z_21d_base_v133_signal,
    f10rcd_f10_retail_comp_dynamics_stab_z_42d_base_v134_signal,
    f10rcd_f10_retail_comp_dynamics_stab_z_63d_base_v135_signal,
    f10rcd_f10_retail_comp_dynamics_stab_z_126d_base_v136_signal,
    f10rcd_f10_retail_comp_dynamics_stab_z_189d_base_v137_signal,
    f10rcd_f10_retail_comp_dynamics_stab_z_252d_base_v138_signal,
    f10rcd_f10_retail_comp_dynamics_stab_z_378d_base_v139_signal,
    f10rcd_f10_retail_comp_dynamics_stab_z_504d_base_v140_signal,
    f10rcd_f10_retail_comp_dynamics_stab_xppe_5d_base_v141_signal,
    f10rcd_f10_retail_comp_dynamics_stab_xppe_10d_base_v142_signal,
    f10rcd_f10_retail_comp_dynamics_stab_xppe_21d_base_v143_signal,
    f10rcd_f10_retail_comp_dynamics_stab_xppe_42d_base_v144_signal,
    f10rcd_f10_retail_comp_dynamics_stab_xppe_63d_base_v145_signal,
    f10rcd_f10_retail_comp_dynamics_stab_xppe_126d_base_v146_signal,
    f10rcd_f10_retail_comp_dynamics_stab_xppe_189d_base_v147_signal,
    f10rcd_f10_retail_comp_dynamics_stab_xppe_252d_base_v148_signal,
    f10rcd_f10_retail_comp_dynamics_stab_xppe_378d_base_v149_signal,
    f10rcd_f10_retail_comp_dynamics_stab_xppe_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_RETAIL_COMP_DYNAMICS_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f10_comp_growth_durability", "_f10_comp_floor", "_f10_comp_stability")
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
    print(f"OK f10_retail_comp_dynamics_076_150_claude: {n_features} features pass")
