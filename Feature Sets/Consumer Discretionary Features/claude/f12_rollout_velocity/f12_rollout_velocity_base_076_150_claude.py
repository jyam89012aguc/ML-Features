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

def _f12_capex_acceleration(capex, w):
    g = capex.pct_change(periods=w)
    return g - g.shift(w)


def _f12_revenue_capex_dynamics(revenue, capex, w):
    rg = revenue.pct_change(periods=w)
    cg = capex.pct_change(periods=w)
    return rg * cg


def _f12_rollout_signature(capex, revenue, w):
    cg = capex.pct_change(periods=w)
    rg = revenue.pct_change(periods=w)
    cap_acc = cg - cg.shift(w)
    return cap_acc + rg


# ===== features =====

def f12rov_f12_rollout_velocity_rcd_sclose_378d_base_v076_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 378) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_xclose_504d_base_v077_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_zclose_504d_base_v078_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 504) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_mclose_504d_base_v079_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 504) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_sclose_504d_base_v080_signal(revenue, capex, closeadj):
    result = _f12_revenue_capex_dynamics(revenue, capex, 504) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_xclose_5d_base_v081_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_zclose_5d_base_v082_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_mclose_5d_base_v083_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_sclose_5d_base_v084_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_xclose_10d_base_v085_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_zclose_10d_base_v086_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_mclose_10d_base_v087_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_sclose_10d_base_v088_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_xclose_21d_base_v089_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_zclose_21d_base_v090_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_mclose_21d_base_v091_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_sclose_21d_base_v092_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_xclose_42d_base_v093_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_zclose_42d_base_v094_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_mclose_42d_base_v095_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_sclose_42d_base_v096_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_xclose_63d_base_v097_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_zclose_63d_base_v098_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_mclose_63d_base_v099_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_sclose_63d_base_v100_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_xclose_126d_base_v101_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_zclose_126d_base_v102_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 126) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_mclose_126d_base_v103_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 126) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_sclose_126d_base_v104_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_xclose_189d_base_v105_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_zclose_189d_base_v106_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 189) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_mclose_189d_base_v107_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 189) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_sclose_189d_base_v108_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 189) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_xclose_252d_base_v109_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_zclose_252d_base_v110_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 252) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_mclose_252d_base_v111_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 252) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_sclose_252d_base_v112_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 252) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_xclose_378d_base_v113_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_zclose_378d_base_v114_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 378) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_mclose_378d_base_v115_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 378) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_sclose_378d_base_v116_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 378) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_xclose_504d_base_v117_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_zclose_504d_base_v118_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 504) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_mclose_504d_base_v119_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 504) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_sclose_504d_base_v120_signal(capex, revenue, closeadj):
    result = _f12_rollout_signature(capex, revenue, 504) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_capm0_21d_base_v121_signal(capex, closeadj):
    result = _mean(_f12_capex_acceleration(capex, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_capm1_42d_base_v122_signal(capex, closeadj):
    result = _mean(_f12_capex_acceleration(capex, 42), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_capm2_63d_base_v123_signal(capex, closeadj):
    result = _mean(_f12_capex_acceleration(capex, 63), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_capm3_126d_base_v124_signal(capex, closeadj):
    result = _mean(_f12_capex_acceleration(capex, 126), 21) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_capm4_189d_base_v125_signal(capex, closeadj):
    result = _mean(_f12_capex_acceleration(capex, 189), 21) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_capm5_252d_base_v126_signal(capex, closeadj):
    result = _mean(_f12_capex_acceleration(capex, 252), 21) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_capm6_378d_base_v127_signal(capex, closeadj):
    result = _mean(_f12_capex_acceleration(capex, 378), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_capm7_504d_base_v128_signal(capex, closeadj):
    result = _mean(_f12_capex_acceleration(capex, 504), 21) * (closeadj - _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_capm8_10d_base_v129_signal(capex, closeadj):
    result = _mean(_f12_capex_acceleration(capex, 10), 21) * (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_capm9_5d_base_v130_signal(capex, closeadj):
    result = _mean(_f12_capex_acceleration(capex, 5), 21) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcdm0_21d_base_v131_signal(revenue, capex, closeadj):
    result = _mean(_f12_revenue_capex_dynamics(revenue, capex, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcdm1_42d_base_v132_signal(revenue, capex, closeadj):
    result = _mean(_f12_revenue_capex_dynamics(revenue, capex, 42), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcdm2_63d_base_v133_signal(revenue, capex, closeadj):
    result = _mean(_f12_revenue_capex_dynamics(revenue, capex, 63), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcdm3_126d_base_v134_signal(revenue, capex, closeadj):
    result = _mean(_f12_revenue_capex_dynamics(revenue, capex, 126), 21) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcdm4_189d_base_v135_signal(revenue, capex, closeadj):
    result = _mean(_f12_revenue_capex_dynamics(revenue, capex, 189), 21) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcdm5_252d_base_v136_signal(revenue, capex, closeadj):
    result = _mean(_f12_revenue_capex_dynamics(revenue, capex, 252), 21) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcdm6_378d_base_v137_signal(revenue, capex, closeadj):
    result = _mean(_f12_revenue_capex_dynamics(revenue, capex, 378), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcdm7_504d_base_v138_signal(revenue, capex, closeadj):
    result = _mean(_f12_revenue_capex_dynamics(revenue, capex, 504), 21) * (closeadj - _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcdm8_10d_base_v139_signal(revenue, capex, closeadj):
    result = _mean(_f12_revenue_capex_dynamics(revenue, capex, 10), 21) * (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcdm9_5d_base_v140_signal(revenue, capex, closeadj):
    result = _mean(_f12_revenue_capex_dynamics(revenue, capex, 5), 21) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sigz0_21d_base_v141_signal(capex, revenue, closeadj):
    result = _z(_f12_rollout_signature(capex, revenue, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sigz1_42d_base_v142_signal(capex, revenue, closeadj):
    result = _z(_f12_rollout_signature(capex, revenue, 42), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sigz2_63d_base_v143_signal(capex, revenue, closeadj):
    result = _z(_f12_rollout_signature(capex, revenue, 63), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sigz3_126d_base_v144_signal(capex, revenue, closeadj):
    result = _z(_f12_rollout_signature(capex, revenue, 126), 63) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sigz4_189d_base_v145_signal(capex, revenue, closeadj):
    result = _z(_f12_rollout_signature(capex, revenue, 189), 63) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sigz5_252d_base_v146_signal(capex, revenue, closeadj):
    result = _z(_f12_rollout_signature(capex, revenue, 252), 63) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sigz6_378d_base_v147_signal(capex, revenue, closeadj):
    result = _z(_f12_rollout_signature(capex, revenue, 378), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sigz7_504d_base_v148_signal(capex, revenue, closeadj):
    result = _z(_f12_rollout_signature(capex, revenue, 504), 63) * (closeadj - _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sigz8_10d_base_v149_signal(capex, revenue, closeadj):
    result = _z(_f12_rollout_signature(capex, revenue, 10), 63) * (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sigz9_5d_base_v150_signal(capex, revenue, closeadj):
    result = _z(_f12_rollout_signature(capex, revenue, 5), 63) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f12rov_f12_rollout_velocity_rcd_sclose_378d_base_v076_signal,
    f12rov_f12_rollout_velocity_rcd_xclose_504d_base_v077_signal,
    f12rov_f12_rollout_velocity_rcd_zclose_504d_base_v078_signal,
    f12rov_f12_rollout_velocity_rcd_mclose_504d_base_v079_signal,
    f12rov_f12_rollout_velocity_rcd_sclose_504d_base_v080_signal,
    f12rov_f12_rollout_velocity_sig_xclose_5d_base_v081_signal,
    f12rov_f12_rollout_velocity_sig_zclose_5d_base_v082_signal,
    f12rov_f12_rollout_velocity_sig_mclose_5d_base_v083_signal,
    f12rov_f12_rollout_velocity_sig_sclose_5d_base_v084_signal,
    f12rov_f12_rollout_velocity_sig_xclose_10d_base_v085_signal,
    f12rov_f12_rollout_velocity_sig_zclose_10d_base_v086_signal,
    f12rov_f12_rollout_velocity_sig_mclose_10d_base_v087_signal,
    f12rov_f12_rollout_velocity_sig_sclose_10d_base_v088_signal,
    f12rov_f12_rollout_velocity_sig_xclose_21d_base_v089_signal,
    f12rov_f12_rollout_velocity_sig_zclose_21d_base_v090_signal,
    f12rov_f12_rollout_velocity_sig_mclose_21d_base_v091_signal,
    f12rov_f12_rollout_velocity_sig_sclose_21d_base_v092_signal,
    f12rov_f12_rollout_velocity_sig_xclose_42d_base_v093_signal,
    f12rov_f12_rollout_velocity_sig_zclose_42d_base_v094_signal,
    f12rov_f12_rollout_velocity_sig_mclose_42d_base_v095_signal,
    f12rov_f12_rollout_velocity_sig_sclose_42d_base_v096_signal,
    f12rov_f12_rollout_velocity_sig_xclose_63d_base_v097_signal,
    f12rov_f12_rollout_velocity_sig_zclose_63d_base_v098_signal,
    f12rov_f12_rollout_velocity_sig_mclose_63d_base_v099_signal,
    f12rov_f12_rollout_velocity_sig_sclose_63d_base_v100_signal,
    f12rov_f12_rollout_velocity_sig_xclose_126d_base_v101_signal,
    f12rov_f12_rollout_velocity_sig_zclose_126d_base_v102_signal,
    f12rov_f12_rollout_velocity_sig_mclose_126d_base_v103_signal,
    f12rov_f12_rollout_velocity_sig_sclose_126d_base_v104_signal,
    f12rov_f12_rollout_velocity_sig_xclose_189d_base_v105_signal,
    f12rov_f12_rollout_velocity_sig_zclose_189d_base_v106_signal,
    f12rov_f12_rollout_velocity_sig_mclose_189d_base_v107_signal,
    f12rov_f12_rollout_velocity_sig_sclose_189d_base_v108_signal,
    f12rov_f12_rollout_velocity_sig_xclose_252d_base_v109_signal,
    f12rov_f12_rollout_velocity_sig_zclose_252d_base_v110_signal,
    f12rov_f12_rollout_velocity_sig_mclose_252d_base_v111_signal,
    f12rov_f12_rollout_velocity_sig_sclose_252d_base_v112_signal,
    f12rov_f12_rollout_velocity_sig_xclose_378d_base_v113_signal,
    f12rov_f12_rollout_velocity_sig_zclose_378d_base_v114_signal,
    f12rov_f12_rollout_velocity_sig_mclose_378d_base_v115_signal,
    f12rov_f12_rollout_velocity_sig_sclose_378d_base_v116_signal,
    f12rov_f12_rollout_velocity_sig_xclose_504d_base_v117_signal,
    f12rov_f12_rollout_velocity_sig_zclose_504d_base_v118_signal,
    f12rov_f12_rollout_velocity_sig_mclose_504d_base_v119_signal,
    f12rov_f12_rollout_velocity_sig_sclose_504d_base_v120_signal,
    f12rov_f12_rollout_velocity_capm0_21d_base_v121_signal,
    f12rov_f12_rollout_velocity_capm1_42d_base_v122_signal,
    f12rov_f12_rollout_velocity_capm2_63d_base_v123_signal,
    f12rov_f12_rollout_velocity_capm3_126d_base_v124_signal,
    f12rov_f12_rollout_velocity_capm4_189d_base_v125_signal,
    f12rov_f12_rollout_velocity_capm5_252d_base_v126_signal,
    f12rov_f12_rollout_velocity_capm6_378d_base_v127_signal,
    f12rov_f12_rollout_velocity_capm7_504d_base_v128_signal,
    f12rov_f12_rollout_velocity_capm8_10d_base_v129_signal,
    f12rov_f12_rollout_velocity_capm9_5d_base_v130_signal,
    f12rov_f12_rollout_velocity_rcdm0_21d_base_v131_signal,
    f12rov_f12_rollout_velocity_rcdm1_42d_base_v132_signal,
    f12rov_f12_rollout_velocity_rcdm2_63d_base_v133_signal,
    f12rov_f12_rollout_velocity_rcdm3_126d_base_v134_signal,
    f12rov_f12_rollout_velocity_rcdm4_189d_base_v135_signal,
    f12rov_f12_rollout_velocity_rcdm5_252d_base_v136_signal,
    f12rov_f12_rollout_velocity_rcdm6_378d_base_v137_signal,
    f12rov_f12_rollout_velocity_rcdm7_504d_base_v138_signal,
    f12rov_f12_rollout_velocity_rcdm8_10d_base_v139_signal,
    f12rov_f12_rollout_velocity_rcdm9_5d_base_v140_signal,
    f12rov_f12_rollout_velocity_sigz0_21d_base_v141_signal,
    f12rov_f12_rollout_velocity_sigz1_42d_base_v142_signal,
    f12rov_f12_rollout_velocity_sigz2_63d_base_v143_signal,
    f12rov_f12_rollout_velocity_sigz3_126d_base_v144_signal,
    f12rov_f12_rollout_velocity_sigz4_189d_base_v145_signal,
    f12rov_f12_rollout_velocity_sigz5_252d_base_v146_signal,
    f12rov_f12_rollout_velocity_sigz6_378d_base_v147_signal,
    f12rov_f12_rollout_velocity_sigz7_504d_base_v148_signal,
    f12rov_f12_rollout_velocity_sigz8_10d_base_v149_signal,
    f12rov_f12_rollout_velocity_sigz9_5d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F12_ROLLOUT_VELOCITY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":

    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    assets  = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "ebitda": ebitda, "capex": capex,
        "assets": assets, "ppnenet": ppnenet,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f12_capex_acceleration", "_f12_revenue_capex_dynamics", "_f12_rollout_signature")
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
    print(f"OK f12_rollout_velocity_base_076_150_claude: {n_features} features pass")
