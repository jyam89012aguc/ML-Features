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
def _f07_capex_intensity(capex, revenue):
    return capex / revenue.replace(0, np.nan)


def _f07_rollout_pulse(capex, w):
    m = capex.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = capex.rolling(w, min_periods=max(1, w // 2)).std()
    return (capex - m) / sd.replace(0, np.nan)


def _f07_capex_revenue_dynamics(capex, revenue, w):
    intensity = capex / revenue.replace(0, np.nan)
    rev_g = revenue.pct_change(periods=w)
    return intensity * rev_g

def f07srs_f07_store_rollout_signature_pulse_std_126d_base_v076_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 126)
    result = _std(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_std_189d_base_v077_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 189)
    result = _std(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_std_252d_base_v078_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 252)
    result = _std(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_std_378d_base_v079_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 378)
    result = _std(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_std_504d_base_v080_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 504)
    result = _std(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_ema_5d_base_v081_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 5)
    result = _ema(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_ema_10d_base_v082_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 10)
    result = _ema(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_ema_21d_base_v083_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 21)
    result = _ema(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_ema_42d_base_v084_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 42)
    result = _ema(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_ema_63d_base_v085_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 63)
    result = _ema(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_ema_126d_base_v086_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 126)
    result = _ema(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_ema_189d_base_v087_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 189)
    result = _ema(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_ema_252d_base_v088_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 252)
    result = _ema(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_ema_378d_base_v089_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 378)
    result = _ema(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_ema_504d_base_v090_signal(capex, closeadj):
    p = _f07_rollout_pulse(capex, 504)
    result = _ema(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_xppe_5d_base_v091_signal(capex, closeadj, ppnenet):
    p = _f07_rollout_pulse(capex, 5)
    result = p * closeadj * (capex / ppnenet.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_xppe_10d_base_v092_signal(capex, closeadj, ppnenet):
    p = _f07_rollout_pulse(capex, 10)
    result = p * closeadj * (capex / ppnenet.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_xppe_21d_base_v093_signal(capex, closeadj, ppnenet):
    p = _f07_rollout_pulse(capex, 21)
    result = p * closeadj * (capex / ppnenet.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_xppe_42d_base_v094_signal(capex, closeadj, ppnenet):
    p = _f07_rollout_pulse(capex, 42)
    result = p * closeadj * (capex / ppnenet.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_xppe_63d_base_v095_signal(capex, closeadj, ppnenet):
    p = _f07_rollout_pulse(capex, 63)
    result = p * closeadj * (capex / ppnenet.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_xppe_126d_base_v096_signal(capex, closeadj, ppnenet):
    p = _f07_rollout_pulse(capex, 126)
    result = p * closeadj * (capex / ppnenet.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_xppe_189d_base_v097_signal(capex, closeadj, ppnenet):
    p = _f07_rollout_pulse(capex, 189)
    result = p * closeadj * (capex / ppnenet.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_xppe_252d_base_v098_signal(capex, closeadj, ppnenet):
    p = _f07_rollout_pulse(capex, 252)
    result = p * closeadj * (capex / ppnenet.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_xppe_378d_base_v099_signal(capex, closeadj, ppnenet):
    p = _f07_rollout_pulse(capex, 378)
    result = p * closeadj * (capex / ppnenet.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_pulse_xppe_504d_base_v100_signal(capex, closeadj, ppnenet):
    p = _f07_rollout_pulse(capex, 504)
    result = p * closeadj * (capex / ppnenet.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_5d_base_v101_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 5)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_10d_base_v102_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 10)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_21d_base_v103_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 21)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_42d_base_v104_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 42)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_63d_base_v105_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 63)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_126d_base_v106_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 126)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_189d_base_v107_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 189)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_252d_base_v108_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 252)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_378d_base_v109_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 378)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_504d_base_v110_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 504)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_mean_5d_base_v111_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 5)
    result = _mean(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_mean_10d_base_v112_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 10)
    result = _mean(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_mean_21d_base_v113_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 21)
    result = _mean(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_mean_42d_base_v114_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 42)
    result = _mean(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_mean_63d_base_v115_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 63)
    result = _mean(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_mean_126d_base_v116_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 126)
    result = _mean(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_mean_189d_base_v117_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 189)
    result = _mean(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_mean_252d_base_v118_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 252)
    result = _mean(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_mean_378d_base_v119_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 378)
    result = _mean(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_mean_504d_base_v120_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 504)
    result = _mean(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_std_5d_base_v121_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 5)
    result = _std(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_std_10d_base_v122_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 10)
    result = _std(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_std_21d_base_v123_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 21)
    result = _std(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_std_42d_base_v124_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 42)
    result = _std(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_std_63d_base_v125_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 63)
    result = _std(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_std_126d_base_v126_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 126)
    result = _std(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_std_189d_base_v127_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 189)
    result = _std(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_std_252d_base_v128_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 252)
    result = _std(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_std_378d_base_v129_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 378)
    result = _std(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_std_504d_base_v130_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 504)
    result = _std(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_z_5d_base_v131_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 5)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_z_10d_base_v132_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 10)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_z_21d_base_v133_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 21)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_z_42d_base_v134_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 42)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_z_63d_base_v135_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 63)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_z_126d_base_v136_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 126)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_z_189d_base_v137_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 189)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_z_252d_base_v138_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 252)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_z_378d_base_v139_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 378)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_z_504d_base_v140_signal(capex, revenue, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 504)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_xppe_5d_base_v141_signal(capex, revenue, ppnenet, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 5)
    result = d * (ppnenet / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_xppe_10d_base_v142_signal(capex, revenue, ppnenet, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 10)
    result = d * (ppnenet / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_xppe_21d_base_v143_signal(capex, revenue, ppnenet, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 21)
    result = d * (ppnenet / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_xppe_42d_base_v144_signal(capex, revenue, ppnenet, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 42)
    result = d * (ppnenet / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_xppe_63d_base_v145_signal(capex, revenue, ppnenet, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 63)
    result = d * (ppnenet / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_xppe_126d_base_v146_signal(capex, revenue, ppnenet, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 126)
    result = d * (ppnenet / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_xppe_189d_base_v147_signal(capex, revenue, ppnenet, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 189)
    result = d * (ppnenet / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_xppe_252d_base_v148_signal(capex, revenue, ppnenet, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 252)
    result = d * (ppnenet / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_xppe_378d_base_v149_signal(capex, revenue, ppnenet, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 378)
    result = d * (ppnenet / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f07srs_f07_store_rollout_signature_dyn_xppe_504d_base_v150_signal(capex, revenue, ppnenet, closeadj):
    d = _f07_capex_revenue_dynamics(capex, revenue, 504)
    result = d * (ppnenet / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f07srs_f07_store_rollout_signature_pulse_std_126d_base_v076_signal,
    f07srs_f07_store_rollout_signature_pulse_std_189d_base_v077_signal,
    f07srs_f07_store_rollout_signature_pulse_std_252d_base_v078_signal,
    f07srs_f07_store_rollout_signature_pulse_std_378d_base_v079_signal,
    f07srs_f07_store_rollout_signature_pulse_std_504d_base_v080_signal,
    f07srs_f07_store_rollout_signature_pulse_ema_5d_base_v081_signal,
    f07srs_f07_store_rollout_signature_pulse_ema_10d_base_v082_signal,
    f07srs_f07_store_rollout_signature_pulse_ema_21d_base_v083_signal,
    f07srs_f07_store_rollout_signature_pulse_ema_42d_base_v084_signal,
    f07srs_f07_store_rollout_signature_pulse_ema_63d_base_v085_signal,
    f07srs_f07_store_rollout_signature_pulse_ema_126d_base_v086_signal,
    f07srs_f07_store_rollout_signature_pulse_ema_189d_base_v087_signal,
    f07srs_f07_store_rollout_signature_pulse_ema_252d_base_v088_signal,
    f07srs_f07_store_rollout_signature_pulse_ema_378d_base_v089_signal,
    f07srs_f07_store_rollout_signature_pulse_ema_504d_base_v090_signal,
    f07srs_f07_store_rollout_signature_pulse_xppe_5d_base_v091_signal,
    f07srs_f07_store_rollout_signature_pulse_xppe_10d_base_v092_signal,
    f07srs_f07_store_rollout_signature_pulse_xppe_21d_base_v093_signal,
    f07srs_f07_store_rollout_signature_pulse_xppe_42d_base_v094_signal,
    f07srs_f07_store_rollout_signature_pulse_xppe_63d_base_v095_signal,
    f07srs_f07_store_rollout_signature_pulse_xppe_126d_base_v096_signal,
    f07srs_f07_store_rollout_signature_pulse_xppe_189d_base_v097_signal,
    f07srs_f07_store_rollout_signature_pulse_xppe_252d_base_v098_signal,
    f07srs_f07_store_rollout_signature_pulse_xppe_378d_base_v099_signal,
    f07srs_f07_store_rollout_signature_pulse_xppe_504d_base_v100_signal,
    f07srs_f07_store_rollout_signature_dyn_5d_base_v101_signal,
    f07srs_f07_store_rollout_signature_dyn_10d_base_v102_signal,
    f07srs_f07_store_rollout_signature_dyn_21d_base_v103_signal,
    f07srs_f07_store_rollout_signature_dyn_42d_base_v104_signal,
    f07srs_f07_store_rollout_signature_dyn_63d_base_v105_signal,
    f07srs_f07_store_rollout_signature_dyn_126d_base_v106_signal,
    f07srs_f07_store_rollout_signature_dyn_189d_base_v107_signal,
    f07srs_f07_store_rollout_signature_dyn_252d_base_v108_signal,
    f07srs_f07_store_rollout_signature_dyn_378d_base_v109_signal,
    f07srs_f07_store_rollout_signature_dyn_504d_base_v110_signal,
    f07srs_f07_store_rollout_signature_dyn_mean_5d_base_v111_signal,
    f07srs_f07_store_rollout_signature_dyn_mean_10d_base_v112_signal,
    f07srs_f07_store_rollout_signature_dyn_mean_21d_base_v113_signal,
    f07srs_f07_store_rollout_signature_dyn_mean_42d_base_v114_signal,
    f07srs_f07_store_rollout_signature_dyn_mean_63d_base_v115_signal,
    f07srs_f07_store_rollout_signature_dyn_mean_126d_base_v116_signal,
    f07srs_f07_store_rollout_signature_dyn_mean_189d_base_v117_signal,
    f07srs_f07_store_rollout_signature_dyn_mean_252d_base_v118_signal,
    f07srs_f07_store_rollout_signature_dyn_mean_378d_base_v119_signal,
    f07srs_f07_store_rollout_signature_dyn_mean_504d_base_v120_signal,
    f07srs_f07_store_rollout_signature_dyn_std_5d_base_v121_signal,
    f07srs_f07_store_rollout_signature_dyn_std_10d_base_v122_signal,
    f07srs_f07_store_rollout_signature_dyn_std_21d_base_v123_signal,
    f07srs_f07_store_rollout_signature_dyn_std_42d_base_v124_signal,
    f07srs_f07_store_rollout_signature_dyn_std_63d_base_v125_signal,
    f07srs_f07_store_rollout_signature_dyn_std_126d_base_v126_signal,
    f07srs_f07_store_rollout_signature_dyn_std_189d_base_v127_signal,
    f07srs_f07_store_rollout_signature_dyn_std_252d_base_v128_signal,
    f07srs_f07_store_rollout_signature_dyn_std_378d_base_v129_signal,
    f07srs_f07_store_rollout_signature_dyn_std_504d_base_v130_signal,
    f07srs_f07_store_rollout_signature_dyn_z_5d_base_v131_signal,
    f07srs_f07_store_rollout_signature_dyn_z_10d_base_v132_signal,
    f07srs_f07_store_rollout_signature_dyn_z_21d_base_v133_signal,
    f07srs_f07_store_rollout_signature_dyn_z_42d_base_v134_signal,
    f07srs_f07_store_rollout_signature_dyn_z_63d_base_v135_signal,
    f07srs_f07_store_rollout_signature_dyn_z_126d_base_v136_signal,
    f07srs_f07_store_rollout_signature_dyn_z_189d_base_v137_signal,
    f07srs_f07_store_rollout_signature_dyn_z_252d_base_v138_signal,
    f07srs_f07_store_rollout_signature_dyn_z_378d_base_v139_signal,
    f07srs_f07_store_rollout_signature_dyn_z_504d_base_v140_signal,
    f07srs_f07_store_rollout_signature_dyn_xppe_5d_base_v141_signal,
    f07srs_f07_store_rollout_signature_dyn_xppe_10d_base_v142_signal,
    f07srs_f07_store_rollout_signature_dyn_xppe_21d_base_v143_signal,
    f07srs_f07_store_rollout_signature_dyn_xppe_42d_base_v144_signal,
    f07srs_f07_store_rollout_signature_dyn_xppe_63d_base_v145_signal,
    f07srs_f07_store_rollout_signature_dyn_xppe_126d_base_v146_signal,
    f07srs_f07_store_rollout_signature_dyn_xppe_189d_base_v147_signal,
    f07srs_f07_store_rollout_signature_dyn_xppe_252d_base_v148_signal,
    f07srs_f07_store_rollout_signature_dyn_xppe_378d_base_v149_signal,
    f07srs_f07_store_rollout_signature_dyn_xppe_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_STORE_ROLLOUT_SIGNATURE_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f07_capex_intensity", "_f07_rollout_pulse", "_f07_capex_revenue_dynamics")
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
    print(f"OK f07_store_rollout_signature_076_150_claude: {n_features} features pass")
