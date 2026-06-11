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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _logabs(s):
    return np.log1p(s.abs())


# ===== folder domain primitives =====
def _f02_revenue_smoothness(revenue, w):
    g = revenue.pct_change(periods=w)
    return -g.rolling(w, min_periods=max(1, w // 2)).std()


def _f02_recurring_signature(revenue, w):
    floor = revenue.rolling(w, min_periods=max(1, w // 2)).min()
    return (revenue - floor) / revenue.replace(0, np.nan).abs() - 0.5


def _f02_replacement_score(revenue, grossmargin, w):
    g = revenue.pct_change(periods=w)
    return g * (grossmargin - grossmargin.rolling(w, min_periods=max(1, w // 2)).mean())


# v076: 21d revenue acceleration EMA 63d * closeadj
def f02drc_f02_device_replacement_cycle_accelema_21d_base_v076_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 21)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v077: 63d revenue acceleration EMA 126d * closeadj
def f02drc_f02_device_replacement_cycle_accelema_63d_base_v077_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 63)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v078: 21d launch pulse EMA 63d * closeadj
def f02drc_f02_device_replacement_cycle_pulseema_21d_base_v078_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 21)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v079: 63d launch pulse EMA 252d * closeadj
def f02drc_f02_device_replacement_cycle_pulseema_63d_base_v079_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 63)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v080: 21d signature EMA 63d * closeadj
def f02drc_f02_device_replacement_cycle_sigema_21d_base_v080_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v081: 63d signature EMA 252d * closeadj
def f02drc_f02_device_replacement_cycle_sigema_63d_base_v081_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 63)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v082: 21d revenue acceleration rank 252d * closeadj
def f02drc_f02_device_replacement_cycle_accelrank_21d_base_v082_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 21)
    result = _rank(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v083: 63d revenue acceleration rank 504d * closeadj
def f02drc_f02_device_replacement_cycle_accelrank_63d_base_v083_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 63)
    result = _rank(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v084: 21d launch pulse rank 252d * closeadj
def f02drc_f02_device_replacement_cycle_pulserank_21d_base_v084_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 21)
    result = _rank(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v085: 63d launch pulse rank 504d * closeadj
def f02drc_f02_device_replacement_cycle_pulserank_63d_base_v085_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 63)
    result = _rank(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v086: 21d signature rank 252d * closeadj
def f02drc_f02_device_replacement_cycle_sigrank_21d_base_v086_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21)
    result = _rank(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v087: 63d signature rank 504d * closeadj
def f02drc_f02_device_replacement_cycle_sigrank_63d_base_v087_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 63)
    result = _rank(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v088: 21d revenue acceleration log magnitude * closeadj * sign
def f02drc_f02_device_replacement_cycle_accellog_21d_base_v088_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 21)
    result = _logabs(base) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v089: 63d revenue acceleration log magnitude * closeadj * sign
def f02drc_f02_device_replacement_cycle_accellog_63d_base_v089_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 63)
    result = _logabs(base) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v090: 21d pulse log magnitude * closeadj * sign
def f02drc_f02_device_replacement_cycle_pulselog_21d_base_v090_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 21)
    result = _logabs(base) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v091: 63d pulse log magnitude * closeadj * sign
def f02drc_f02_device_replacement_cycle_pulselog_63d_base_v091_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 63)
    result = _logabs(base) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v092: 21d signature log magnitude * closeadj * sign
def f02drc_f02_device_replacement_cycle_siglog_21d_base_v092_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21)
    result = _logabs(base) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v093: 63d signature log magnitude * closeadj * sign
def f02drc_f02_device_replacement_cycle_siglog_63d_base_v093_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 63)
    result = _logabs(base) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v094: 21d accel × 21d pulse interaction * closeadj
def f02drc_f02_device_replacement_cycle_accelxpulse_21d_base_v094_signal(revenue, closeadj):
    a = _f02_revenue_smoothness(revenue, 21)
    p = _f02_recurring_signature(revenue, 21)
    result = a * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v095: 63d accel × 63d pulse interaction * closeadj
def f02drc_f02_device_replacement_cycle_accelxpulse_63d_base_v095_signal(revenue, closeadj):
    a = _f02_revenue_smoothness(revenue, 63)
    p = _f02_recurring_signature(revenue, 63)
    result = a * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v096: 21d accel × 21d signature interaction * closeadj
def f02drc_f02_device_replacement_cycle_accelxsig_21d_base_v096_signal(revenue, grossmargin, closeadj):
    a = _f02_revenue_smoothness(revenue, 21)
    s = _f02_replacement_score(revenue, grossmargin, 21)
    result = a * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v097: 63d accel × 63d signature interaction * closeadj
def f02drc_f02_device_replacement_cycle_accelxsig_63d_base_v097_signal(revenue, grossmargin, closeadj):
    a = _f02_revenue_smoothness(revenue, 63)
    s = _f02_replacement_score(revenue, grossmargin, 63)
    result = a * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v098: 21d pulse × 21d signature interaction * closeadj
def f02drc_f02_device_replacement_cycle_pulsexsig_21d_base_v098_signal(revenue, grossmargin, closeadj):
    p = _f02_recurring_signature(revenue, 21)
    s = _f02_replacement_score(revenue, grossmargin, 21)
    result = p * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v099: 63d pulse × 63d signature interaction * closeadj
def f02drc_f02_device_replacement_cycle_pulsexsig_63d_base_v099_signal(revenue, grossmargin, closeadj):
    p = _f02_recurring_signature(revenue, 63)
    s = _f02_replacement_score(revenue, grossmargin, 63)
    result = p * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v100: 21d accel - 63d accel (short minus long) * closeadj
def f02drc_f02_device_replacement_cycle_accelxshortlong_21d_base_v100_signal(revenue, closeadj):
    a_s = _f02_revenue_smoothness(revenue, 21)
    a_l = _f02_revenue_smoothness(revenue, 63)
    result = (a_s - a_l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v101: 63d accel - 252d accel * closeadj
def f02drc_f02_device_replacement_cycle_accelxshortlong_63d_base_v101_signal(revenue, closeadj):
    a_s = _f02_revenue_smoothness(revenue, 63)
    a_l = _f02_revenue_smoothness(revenue, 252)
    result = (a_s - a_l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v102: 21d pulse - 63d pulse * closeadj
def f02drc_f02_device_replacement_cycle_pulsexshortlong_21d_base_v102_signal(revenue, closeadj):
    p_s = _f02_recurring_signature(revenue, 21)
    p_l = _f02_recurring_signature(revenue, 63)
    result = (p_s - p_l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v103: 63d pulse - 252d pulse * closeadj
def f02drc_f02_device_replacement_cycle_pulsexshortlong_63d_base_v103_signal(revenue, closeadj):
    p_s = _f02_recurring_signature(revenue, 63)
    p_l = _f02_recurring_signature(revenue, 252)
    result = (p_s - p_l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v104: 21d sig - 63d sig * closeadj
def f02drc_f02_device_replacement_cycle_sigxshortlong_21d_base_v104_signal(revenue, grossmargin, closeadj):
    s_s = _f02_replacement_score(revenue, grossmargin, 21)
    s_l = _f02_replacement_score(revenue, grossmargin, 63)
    result = (s_s - s_l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v105: 63d sig - 252d sig * closeadj
def f02drc_f02_device_replacement_cycle_sigxshortlong_63d_base_v105_signal(revenue, grossmargin, closeadj):
    s_s = _f02_replacement_score(revenue, grossmargin, 63)
    s_l = _f02_replacement_score(revenue, grossmargin, 252)
    result = (s_s - s_l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v106: 21d accel rolling max 63d * closeadj
def f02drc_f02_device_replacement_cycle_accelmax_21d_base_v106_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 21)
    result = base.rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v107: 63d accel rolling max 252d * closeadj
def f02drc_f02_device_replacement_cycle_accelmax_63d_base_v107_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v108: 21d pulse rolling max 63d * closeadj
def f02drc_f02_device_replacement_cycle_pulsemax_21d_base_v108_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 21)
    result = base.rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v109: 63d pulse rolling max 252d * closeadj
def f02drc_f02_device_replacement_cycle_pulsemax_63d_base_v109_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v110: 21d sig rolling max 63d * closeadj
def f02drc_f02_device_replacement_cycle_sigmax_21d_base_v110_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21)
    result = base.rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v111: 63d sig rolling max 252d * closeadj
def f02drc_f02_device_replacement_cycle_sigmax_63d_base_v111_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v112: 21d accel rolling min 63d * closeadj
def f02drc_f02_device_replacement_cycle_accelmin_21d_base_v112_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 21)
    result = base.rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v113: 63d accel rolling min 252d * closeadj
def f02drc_f02_device_replacement_cycle_accelmin_63d_base_v113_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 63)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v114: 21d pulse rolling min 63d * closeadj
def f02drc_f02_device_replacement_cycle_pulsemin_21d_base_v114_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 21)
    result = base.rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v115: 63d pulse rolling min 252d * closeadj
def f02drc_f02_device_replacement_cycle_pulsemin_63d_base_v115_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 63)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v116: 21d sig rolling min 63d * closeadj
def f02drc_f02_device_replacement_cycle_sigmin_21d_base_v116_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21)
    result = base.rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v117: 63d sig rolling min 252d * closeadj
def f02drc_f02_device_replacement_cycle_sigmin_63d_base_v117_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 63)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v118: 21d accel × closeadj momentum (closeadj 63d return)
def f02drc_f02_device_replacement_cycle_accelxmomp_21d_base_v118_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 21)
    mom = closeadj.pct_change(63)
    result = base * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v119: 63d accel × closeadj momentum 252d
def f02drc_f02_device_replacement_cycle_accelxmomp_63d_base_v119_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 63)
    mom = closeadj.pct_change(252)
    result = base * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v120: 21d pulse × closeadj momentum
def f02drc_f02_device_replacement_cycle_pulsexmomp_21d_base_v120_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 21)
    mom = closeadj.pct_change(63)
    result = base * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v121: 63d pulse × closeadj momentum 252d
def f02drc_f02_device_replacement_cycle_pulsexmomp_63d_base_v121_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 63)
    mom = closeadj.pct_change(252)
    result = base * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v122: 21d sig × closeadj momentum
def f02drc_f02_device_replacement_cycle_sigxmomp_21d_base_v122_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21)
    mom = closeadj.pct_change(63)
    result = base * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v123: 63d sig × closeadj momentum 252d
def f02drc_f02_device_replacement_cycle_sigxmomp_63d_base_v123_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 63)
    mom = closeadj.pct_change(252)
    result = base * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v124: 21d accel cumulative sum 63d * closeadj
def f02drc_f02_device_replacement_cycle_accelcum_21d_base_v124_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 21)
    result = base.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v125: 63d accel cumulative sum 252d * closeadj
def f02drc_f02_device_replacement_cycle_accelcum_63d_base_v125_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 63)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v126: 21d pulse cum sum 63d * closeadj
def f02drc_f02_device_replacement_cycle_pulsecum_21d_base_v126_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 21)
    result = base.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v127: 63d pulse cum sum 252d * closeadj
def f02drc_f02_device_replacement_cycle_pulsecum_63d_base_v127_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 63)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v128: 21d sig cum sum 63d * closeadj
def f02drc_f02_device_replacement_cycle_sigcum_21d_base_v128_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21)
    result = base.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v129: 63d sig cum sum 252d * closeadj
def f02drc_f02_device_replacement_cycle_sigcum_63d_base_v129_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 63)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v130: 21d accel × grossmargin growth 252d * closeadj
def f02drc_f02_device_replacement_cycle_accelxinstg_21d_base_v130_signal(revenue, grossmargin, closeadj):
    base = _f02_revenue_smoothness(revenue, 21)
    inst_g = (grossmargin * 100.0).pct_change(252)
    result = base * inst_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v131: 63d accel × grossmargin growth 252d * closeadj
def f02drc_f02_device_replacement_cycle_accelxinstg_63d_base_v131_signal(revenue, grossmargin, closeadj):
    base = _f02_revenue_smoothness(revenue, 63)
    inst_g = (grossmargin * 100.0).pct_change(252)
    result = base * inst_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v132: 21d pulse × grossmargin growth 252d * closeadj
def f02drc_f02_device_replacement_cycle_pulsexinstg_21d_base_v132_signal(revenue, grossmargin, closeadj):
    base = _f02_recurring_signature(revenue, 21)
    inst_g = (grossmargin * 100.0).pct_change(252)
    result = base * inst_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v133: 63d pulse × grossmargin growth 252d * closeadj
def f02drc_f02_device_replacement_cycle_pulsexinstg_63d_base_v133_signal(revenue, grossmargin, closeadj):
    base = _f02_recurring_signature(revenue, 63)
    inst_g = (grossmargin * 100.0).pct_change(252)
    result = base * inst_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v134: 21d sig × grossmargin growth 252d * closeadj
def f02drc_f02_device_replacement_cycle_sigxinstg_21d_base_v134_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21)
    inst_g = (grossmargin * 100.0).pct_change(252)
    result = base * inst_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v135: 63d sig × grossmargin growth 252d * closeadj
def f02drc_f02_device_replacement_cycle_sigxinstg_63d_base_v135_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 63)
    inst_g = (grossmargin * 100.0).pct_change(252)
    result = base * inst_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v136: 21d accel × log(revenue) * closeadj
def f02drc_f02_device_replacement_cycle_accelxlogrev_21d_base_v136_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 21)
    result = base * np.log(revenue.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v137: 63d accel × log(revenue) * closeadj
def f02drc_f02_device_replacement_cycle_accelxlogrev_63d_base_v137_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 63)
    result = base * np.log(revenue.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v138: 21d pulse × log(revenue) * closeadj
def f02drc_f02_device_replacement_cycle_pulsexlogrev_21d_base_v138_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 21)
    result = base * np.log(revenue.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v139: 63d pulse × log(revenue) * closeadj
def f02drc_f02_device_replacement_cycle_pulsexlogrev_63d_base_v139_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 63)
    result = base * np.log(revenue.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v140: 21d sig × log(revenue) * closeadj
def f02drc_f02_device_replacement_cycle_sigxlogrev_21d_base_v140_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21)
    result = base * np.log(revenue.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v141: 63d sig × log(revenue) * closeadj
def f02drc_f02_device_replacement_cycle_sigxlogrev_63d_base_v141_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 63)
    result = base * np.log(revenue.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v142: 21d accel × log(grossmargin) * closeadj
def f02drc_f02_device_replacement_cycle_accelxlogcap_21d_base_v142_signal(revenue, grossmargin, closeadj):
    base = _f02_revenue_smoothness(revenue, 21)
    result = base * np.log(grossmargin.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v143: 63d accel × log(grossmargin) * closeadj
def f02drc_f02_device_replacement_cycle_accelxlogcap_63d_base_v143_signal(revenue, grossmargin, closeadj):
    base = _f02_revenue_smoothness(revenue, 63)
    result = base * np.log(grossmargin.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v144: 21d pulse × log(grossmargin) * closeadj
def f02drc_f02_device_replacement_cycle_pulsexlogcap_21d_base_v144_signal(revenue, grossmargin, closeadj):
    base = _f02_recurring_signature(revenue, 21)
    result = base * np.log(grossmargin.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v145: 63d pulse × log(grossmargin) * closeadj
def f02drc_f02_device_replacement_cycle_pulsexlogcap_63d_base_v145_signal(revenue, grossmargin, closeadj):
    base = _f02_recurring_signature(revenue, 63)
    result = base * np.log(grossmargin.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v146: 21d accel mean 126d * closeadj
def f02drc_f02_device_replacement_cycle_accelmean_126d_base_v146_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v147: 63d accel mean 504d * closeadj
def f02drc_f02_device_replacement_cycle_accelmean_504d_base_v147_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v148: 21d pulse mean 126d * closeadj
def f02drc_f02_device_replacement_cycle_pulsemean_126dshort_base_v148_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v149: 63d pulse mean 504d * closeadj
def f02drc_f02_device_replacement_cycle_pulsemean_504d_base_v149_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v150: 21d sig mean 504d * closeadj
def f02drc_f02_device_replacement_cycle_sigmean_504d_base_v150_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f02drc_f02_device_replacement_cycle_accelema_21d_base_v076_signal,
    f02drc_f02_device_replacement_cycle_accelema_63d_base_v077_signal,
    f02drc_f02_device_replacement_cycle_pulseema_21d_base_v078_signal,
    f02drc_f02_device_replacement_cycle_pulseema_63d_base_v079_signal,
    f02drc_f02_device_replacement_cycle_sigema_21d_base_v080_signal,
    f02drc_f02_device_replacement_cycle_sigema_63d_base_v081_signal,
    f02drc_f02_device_replacement_cycle_accelrank_21d_base_v082_signal,
    f02drc_f02_device_replacement_cycle_accelrank_63d_base_v083_signal,
    f02drc_f02_device_replacement_cycle_pulserank_21d_base_v084_signal,
    f02drc_f02_device_replacement_cycle_pulserank_63d_base_v085_signal,
    f02drc_f02_device_replacement_cycle_sigrank_21d_base_v086_signal,
    f02drc_f02_device_replacement_cycle_sigrank_63d_base_v087_signal,
    f02drc_f02_device_replacement_cycle_accellog_21d_base_v088_signal,
    f02drc_f02_device_replacement_cycle_accellog_63d_base_v089_signal,
    f02drc_f02_device_replacement_cycle_pulselog_21d_base_v090_signal,
    f02drc_f02_device_replacement_cycle_pulselog_63d_base_v091_signal,
    f02drc_f02_device_replacement_cycle_siglog_21d_base_v092_signal,
    f02drc_f02_device_replacement_cycle_siglog_63d_base_v093_signal,
    f02drc_f02_device_replacement_cycle_accelxpulse_21d_base_v094_signal,
    f02drc_f02_device_replacement_cycle_accelxpulse_63d_base_v095_signal,
    f02drc_f02_device_replacement_cycle_accelxsig_21d_base_v096_signal,
    f02drc_f02_device_replacement_cycle_accelxsig_63d_base_v097_signal,
    f02drc_f02_device_replacement_cycle_pulsexsig_21d_base_v098_signal,
    f02drc_f02_device_replacement_cycle_pulsexsig_63d_base_v099_signal,
    f02drc_f02_device_replacement_cycle_accelxshortlong_21d_base_v100_signal,
    f02drc_f02_device_replacement_cycle_accelxshortlong_63d_base_v101_signal,
    f02drc_f02_device_replacement_cycle_pulsexshortlong_21d_base_v102_signal,
    f02drc_f02_device_replacement_cycle_pulsexshortlong_63d_base_v103_signal,
    f02drc_f02_device_replacement_cycle_sigxshortlong_21d_base_v104_signal,
    f02drc_f02_device_replacement_cycle_sigxshortlong_63d_base_v105_signal,
    f02drc_f02_device_replacement_cycle_accelmax_21d_base_v106_signal,
    f02drc_f02_device_replacement_cycle_accelmax_63d_base_v107_signal,
    f02drc_f02_device_replacement_cycle_pulsemax_21d_base_v108_signal,
    f02drc_f02_device_replacement_cycle_pulsemax_63d_base_v109_signal,
    f02drc_f02_device_replacement_cycle_sigmax_21d_base_v110_signal,
    f02drc_f02_device_replacement_cycle_sigmax_63d_base_v111_signal,
    f02drc_f02_device_replacement_cycle_accelmin_21d_base_v112_signal,
    f02drc_f02_device_replacement_cycle_accelmin_63d_base_v113_signal,
    f02drc_f02_device_replacement_cycle_pulsemin_21d_base_v114_signal,
    f02drc_f02_device_replacement_cycle_pulsemin_63d_base_v115_signal,
    f02drc_f02_device_replacement_cycle_sigmin_21d_base_v116_signal,
    f02drc_f02_device_replacement_cycle_sigmin_63d_base_v117_signal,
    f02drc_f02_device_replacement_cycle_accelxmomp_21d_base_v118_signal,
    f02drc_f02_device_replacement_cycle_accelxmomp_63d_base_v119_signal,
    f02drc_f02_device_replacement_cycle_pulsexmomp_21d_base_v120_signal,
    f02drc_f02_device_replacement_cycle_pulsexmomp_63d_base_v121_signal,
    f02drc_f02_device_replacement_cycle_sigxmomp_21d_base_v122_signal,
    f02drc_f02_device_replacement_cycle_sigxmomp_63d_base_v123_signal,
    f02drc_f02_device_replacement_cycle_accelcum_21d_base_v124_signal,
    f02drc_f02_device_replacement_cycle_accelcum_63d_base_v125_signal,
    f02drc_f02_device_replacement_cycle_pulsecum_21d_base_v126_signal,
    f02drc_f02_device_replacement_cycle_pulsecum_63d_base_v127_signal,
    f02drc_f02_device_replacement_cycle_sigcum_21d_base_v128_signal,
    f02drc_f02_device_replacement_cycle_sigcum_63d_base_v129_signal,
    f02drc_f02_device_replacement_cycle_accelxinstg_21d_base_v130_signal,
    f02drc_f02_device_replacement_cycle_accelxinstg_63d_base_v131_signal,
    f02drc_f02_device_replacement_cycle_pulsexinstg_21d_base_v132_signal,
    f02drc_f02_device_replacement_cycle_pulsexinstg_63d_base_v133_signal,
    f02drc_f02_device_replacement_cycle_sigxinstg_21d_base_v134_signal,
    f02drc_f02_device_replacement_cycle_sigxinstg_63d_base_v135_signal,
    f02drc_f02_device_replacement_cycle_accelxlogrev_21d_base_v136_signal,
    f02drc_f02_device_replacement_cycle_accelxlogrev_63d_base_v137_signal,
    f02drc_f02_device_replacement_cycle_pulsexlogrev_21d_base_v138_signal,
    f02drc_f02_device_replacement_cycle_pulsexlogrev_63d_base_v139_signal,
    f02drc_f02_device_replacement_cycle_sigxlogrev_21d_base_v140_signal,
    f02drc_f02_device_replacement_cycle_sigxlogrev_63d_base_v141_signal,
    f02drc_f02_device_replacement_cycle_accelxlogcap_21d_base_v142_signal,
    f02drc_f02_device_replacement_cycle_accelxlogcap_63d_base_v143_signal,
    f02drc_f02_device_replacement_cycle_pulsexlogcap_21d_base_v144_signal,
    f02drc_f02_device_replacement_cycle_pulsexlogcap_63d_base_v145_signal,
    f02drc_f02_device_replacement_cycle_accelmean_126d_base_v146_signal,
    f02drc_f02_device_replacement_cycle_accelmean_504d_base_v147_signal,
    f02drc_f02_device_replacement_cycle_pulsemean_126dshort_base_v148_signal,
    f02drc_f02_device_replacement_cycle_pulsemean_504d_base_v149_signal,
    f02drc_f02_device_replacement_cycle_sigmean_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F02_DEVICE_REPLACEMENT_CYCLE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    grossmargin = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")

    cols = {"closeadj": closeadj, "revenue": revenue, "grossmargin": grossmargin}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f02_revenue_smoothness", "_f02_recurring_signature", "_f02_replacement_score")
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
    print(f"OK f02_device_replacement_cycle_base_076_150_claude: {n_features} features pass")
