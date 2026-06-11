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
def _f05_sga_to_revenue(sgna, revenue, w):
    ratio = sgna / revenue.replace(0, np.nan).abs()
    base = ratio.rolling(w * 4, min_periods=max(1, w)).mean()
    return (ratio - base) / base.replace(0, np.nan).abs()


def _f05_sga_growth_gap(sgna, revenue, w):
    s_g = sgna.pct_change(periods=w)
    r_g = revenue.pct_change(periods=w)
    return s_g - r_g


def _f05_sga_leverage_score(sgna, revenue, w):
    s_g = sgna.pct_change(periods=w)
    r_g = revenue.pct_change(periods=w)
    return r_g - 0.5 * s_g


# v076: 21d sgna acceleration EMA 63d * closeadj
def f05dsf_f05_device_sales_force_scaling_accelema_21d_base_v076_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 21)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v077: 63d sgna acceleration EMA 126d * closeadj
def f05dsf_f05_device_sales_force_scaling_accelema_63d_base_v077_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 63)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v078: 21d launch pulse EMA 63d * closeadj
def f05dsf_f05_device_sales_force_scaling_pulseema_21d_base_v078_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 21)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v079: 63d launch pulse EMA 252d * closeadj
def f05dsf_f05_device_sales_force_scaling_pulseema_63d_base_v079_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 63)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v080: 21d signature EMA 63d * closeadj
def f05dsf_f05_device_sales_force_scaling_sigema_21d_base_v080_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 21)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v081: 63d signature EMA 252d * closeadj
def f05dsf_f05_device_sales_force_scaling_sigema_63d_base_v081_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 63)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v082: 21d sgna acceleration rank 252d * closeadj
def f05dsf_f05_device_sales_force_scaling_accelrank_21d_base_v082_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 21)
    result = _rank(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v083: 63d sgna acceleration rank 504d * closeadj
def f05dsf_f05_device_sales_force_scaling_accelrank_63d_base_v083_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 63)
    result = _rank(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v084: 21d launch pulse rank 252d * closeadj
def f05dsf_f05_device_sales_force_scaling_pulserank_21d_base_v084_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 21)
    result = _rank(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v085: 63d launch pulse rank 504d * closeadj
def f05dsf_f05_device_sales_force_scaling_pulserank_63d_base_v085_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 63)
    result = _rank(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v086: 21d signature rank 252d * closeadj
def f05dsf_f05_device_sales_force_scaling_sigrank_21d_base_v086_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 21)
    result = _rank(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v087: 63d signature rank 504d * closeadj
def f05dsf_f05_device_sales_force_scaling_sigrank_63d_base_v087_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 63)
    result = _rank(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v088: 21d sgna acceleration log magnitude * closeadj * sign
def f05dsf_f05_device_sales_force_scaling_accellog_21d_base_v088_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 21)
    result = _logabs(base) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v089: 63d sgna acceleration log magnitude * closeadj * sign
def f05dsf_f05_device_sales_force_scaling_accellog_63d_base_v089_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 63)
    result = _logabs(base) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v090: 21d pulse log magnitude * closeadj * sign
def f05dsf_f05_device_sales_force_scaling_pulselog_21d_base_v090_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 21)
    result = _logabs(base) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v091: 63d pulse log magnitude * closeadj * sign
def f05dsf_f05_device_sales_force_scaling_pulselog_63d_base_v091_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 63)
    result = _logabs(base) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v092: 21d signature log magnitude * closeadj * sign
def f05dsf_f05_device_sales_force_scaling_siglog_21d_base_v092_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 21)
    result = _logabs(base) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v093: 63d signature log magnitude * closeadj * sign
def f05dsf_f05_device_sales_force_scaling_siglog_63d_base_v093_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 63)
    result = _logabs(base) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v094: 21d accel × 21d pulse interaction * closeadj
def f05dsf_f05_device_sales_force_scaling_accelxpulse_21d_base_v094_signal(sgna, revenue, closeadj):
    a = _f05_sga_growth_gap(sgna, revenue, 21)
    p = _f05_sga_to_revenue(sgna, revenue, 21)
    result = a * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v095: 63d accel × 63d pulse interaction * closeadj
def f05dsf_f05_device_sales_force_scaling_accelxpulse_63d_base_v095_signal(sgna, revenue, closeadj):
    a = _f05_sga_growth_gap(sgna, revenue, 63)
    p = _f05_sga_to_revenue(sgna, revenue, 63)
    result = a * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v096: 21d accel × 21d signature interaction * closeadj
def f05dsf_f05_device_sales_force_scaling_accelxsig_21d_base_v096_signal(sgna, revenue, closeadj):
    a = _f05_sga_growth_gap(sgna, revenue, 21)
    s = _f05_sga_leverage_score(sgna, sgna, 21)
    result = a * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v097: 63d accel × 63d signature interaction * closeadj
def f05dsf_f05_device_sales_force_scaling_accelxsig_63d_base_v097_signal(sgna, revenue, closeadj):
    a = _f05_sga_growth_gap(sgna, revenue, 63)
    s = _f05_sga_leverage_score(sgna, sgna, 63)
    result = a * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v098: 21d pulse × 21d signature interaction * closeadj
def f05dsf_f05_device_sales_force_scaling_pulsexsig_21d_base_v098_signal(sgna, revenue, closeadj):
    p = _f05_sga_to_revenue(sgna, revenue, 21)
    s = _f05_sga_leverage_score(sgna, sgna, 21)
    result = p * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v099: 63d pulse × 63d signature interaction * closeadj
def f05dsf_f05_device_sales_force_scaling_pulsexsig_63d_base_v099_signal(sgna, revenue, closeadj):
    p = _f05_sga_to_revenue(sgna, revenue, 63)
    s = _f05_sga_leverage_score(sgna, sgna, 63)
    result = p * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v100: 21d accel - 63d accel (short minus long) * closeadj
def f05dsf_f05_device_sales_force_scaling_accelxshortlong_21d_base_v100_signal(sgna, revenue, closeadj):
    a_s = _f05_sga_growth_gap(sgna, revenue, 21)
    a_l = _f05_sga_growth_gap(sgna, revenue, 63)
    result = (a_s - a_l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v101: 63d accel - 252d accel * closeadj
def f05dsf_f05_device_sales_force_scaling_accelxshortlong_63d_base_v101_signal(sgna, revenue, closeadj):
    a_s = _f05_sga_growth_gap(sgna, revenue, 63)
    a_l = _f05_sga_growth_gap(sgna, revenue, 252)
    result = (a_s - a_l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v102: 21d pulse - 63d pulse * closeadj
def f05dsf_f05_device_sales_force_scaling_pulsexshortlong_21d_base_v102_signal(sgna, revenue, closeadj):
    p_s = _f05_sga_to_revenue(sgna, revenue, 21)
    p_l = _f05_sga_to_revenue(sgna, revenue, 63)
    result = (p_s - p_l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v103: 63d pulse - 252d pulse * closeadj
def f05dsf_f05_device_sales_force_scaling_pulsexshortlong_63d_base_v103_signal(sgna, revenue, closeadj):
    p_s = _f05_sga_to_revenue(sgna, revenue, 63)
    p_l = _f05_sga_to_revenue(sgna, revenue, 252)
    result = (p_s - p_l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v104: 21d sig - 63d sig * closeadj
def f05dsf_f05_device_sales_force_scaling_sigxshortlong_21d_base_v104_signal(sgna, closeadj):
    s_s = _f05_sga_leverage_score(sgna, sgna, 21)
    s_l = _f05_sga_leverage_score(sgna, sgna, 63)
    result = (s_s - s_l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v105: 63d sig - 252d sig * closeadj
def f05dsf_f05_device_sales_force_scaling_sigxshortlong_63d_base_v105_signal(sgna, closeadj):
    s_s = _f05_sga_leverage_score(sgna, sgna, 63)
    s_l = _f05_sga_leverage_score(sgna, sgna, 252)
    result = (s_s - s_l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v106: 21d accel rolling max 63d * closeadj
def f05dsf_f05_device_sales_force_scaling_accelmax_21d_base_v106_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 21)
    result = base.rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v107: 63d accel rolling max 252d * closeadj
def f05dsf_f05_device_sales_force_scaling_accelmax_63d_base_v107_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v108: 21d pulse rolling max 63d * closeadj
def f05dsf_f05_device_sales_force_scaling_pulsemax_21d_base_v108_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 21)
    result = base.rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v109: 63d pulse rolling max 252d * closeadj
def f05dsf_f05_device_sales_force_scaling_pulsemax_63d_base_v109_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v110: 21d sig rolling max 63d * closeadj
def f05dsf_f05_device_sales_force_scaling_sigmax_21d_base_v110_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 21)
    result = base.rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v111: 63d sig rolling max 252d * closeadj
def f05dsf_f05_device_sales_force_scaling_sigmax_63d_base_v111_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v112: 21d accel rolling min 63d * closeadj
def f05dsf_f05_device_sales_force_scaling_accelmin_21d_base_v112_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 21)
    result = base.rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v113: 63d accel rolling min 252d * closeadj
def f05dsf_f05_device_sales_force_scaling_accelmin_63d_base_v113_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 63)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v114: 21d pulse rolling min 63d * closeadj
def f05dsf_f05_device_sales_force_scaling_pulsemin_21d_base_v114_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 21)
    result = base.rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v115: 63d pulse rolling min 252d * closeadj
def f05dsf_f05_device_sales_force_scaling_pulsemin_63d_base_v115_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 63)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v116: 21d sig rolling min 63d * closeadj
def f05dsf_f05_device_sales_force_scaling_sigmin_21d_base_v116_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 21)
    result = base.rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v117: 63d sig rolling min 252d * closeadj
def f05dsf_f05_device_sales_force_scaling_sigmin_63d_base_v117_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 63)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v118: 21d accel × closeadj momentum (closeadj 63d return)
def f05dsf_f05_device_sales_force_scaling_accelxmomp_21d_base_v118_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 21)
    mom = closeadj.pct_change(63)
    result = base * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v119: 63d accel × closeadj momentum 252d
def f05dsf_f05_device_sales_force_scaling_accelxmomp_63d_base_v119_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 63)
    mom = closeadj.pct_change(252)
    result = base * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v120: 21d pulse × closeadj momentum
def f05dsf_f05_device_sales_force_scaling_pulsexmomp_21d_base_v120_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 21)
    mom = closeadj.pct_change(63)
    result = base * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v121: 63d pulse × closeadj momentum 252d
def f05dsf_f05_device_sales_force_scaling_pulsexmomp_63d_base_v121_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 63)
    mom = closeadj.pct_change(252)
    result = base * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v122: 21d sig × closeadj momentum
def f05dsf_f05_device_sales_force_scaling_sigxmomp_21d_base_v122_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 21)
    mom = closeadj.pct_change(63)
    result = base * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v123: 63d sig × closeadj momentum 252d
def f05dsf_f05_device_sales_force_scaling_sigxmomp_63d_base_v123_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 63)
    mom = closeadj.pct_change(252)
    result = base * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v124: 21d accel cumulative sum 63d * closeadj
def f05dsf_f05_device_sales_force_scaling_accelcum_21d_base_v124_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 21)
    result = base.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v125: 63d accel cumulative sum 252d * closeadj
def f05dsf_f05_device_sales_force_scaling_accelcum_63d_base_v125_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 63)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v126: 21d pulse cum sum 63d * closeadj
def f05dsf_f05_device_sales_force_scaling_pulsecum_21d_base_v126_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 21)
    result = base.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v127: 63d pulse cum sum 252d * closeadj
def f05dsf_f05_device_sales_force_scaling_pulsecum_63d_base_v127_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 63)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v128: 21d sig cum sum 63d * closeadj
def f05dsf_f05_device_sales_force_scaling_sigcum_21d_base_v128_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 21)
    result = base.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v129: 63d sig cum sum 252d * closeadj
def f05dsf_f05_device_sales_force_scaling_sigcum_63d_base_v129_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 63)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v130: 21d accel × opex growth 252d * closeadj
def f05dsf_f05_device_sales_force_scaling_accelxinstg_21d_base_v130_signal(sgna, revenue, opex, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 21)
    inst_g = opex.pct_change(252)
    result = base * inst_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v131: 63d accel × opex growth 252d * closeadj
def f05dsf_f05_device_sales_force_scaling_accelxinstg_63d_base_v131_signal(sgna, revenue, opex, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 63)
    inst_g = opex.pct_change(252)
    result = base * inst_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v132: 21d pulse × opex growth 252d * closeadj
def f05dsf_f05_device_sales_force_scaling_pulsexinstg_21d_base_v132_signal(sgna, revenue, opex, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 21)
    inst_g = opex.pct_change(252)
    result = base * inst_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v133: 63d pulse × opex growth 252d * closeadj
def f05dsf_f05_device_sales_force_scaling_pulsexinstg_63d_base_v133_signal(sgna, revenue, opex, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 63)
    inst_g = opex.pct_change(252)
    result = base * inst_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v134: 21d sig × opex growth 252d * closeadj
def f05dsf_f05_device_sales_force_scaling_sigxinstg_21d_base_v134_signal(sgna, opex, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 21)
    inst_g = opex.pct_change(252)
    result = base * inst_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v135: 63d sig × opex growth 252d * closeadj
def f05dsf_f05_device_sales_force_scaling_sigxinstg_63d_base_v135_signal(sgna, opex, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 63)
    inst_g = opex.pct_change(252)
    result = base * inst_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v136: 21d accel × log(sgna) * closeadj
def f05dsf_f05_device_sales_force_scaling_accelxlogrev_21d_base_v136_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 21)
    result = base * np.log((sgna * 10.0).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v137: 63d accel × log(sgna) * closeadj
def f05dsf_f05_device_sales_force_scaling_accelxlogrev_63d_base_v137_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 63)
    result = base * np.log((sgna * 10.0).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v138: 21d pulse × log(sgna) * closeadj
def f05dsf_f05_device_sales_force_scaling_pulsexlogrev_21d_base_v138_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 21)
    result = base * np.log((sgna * 10.0).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v139: 63d pulse × log(sgna) * closeadj
def f05dsf_f05_device_sales_force_scaling_pulsexlogrev_63d_base_v139_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 63)
    result = base * np.log((sgna * 10.0).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v140: 21d sig × log(sgna) * closeadj
def f05dsf_f05_device_sales_force_scaling_sigxlogrev_21d_base_v140_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 21)
    result = base * np.log((sgna * 10.0).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v141: 63d sig × log(sgna) * closeadj
def f05dsf_f05_device_sales_force_scaling_sigxlogrev_63d_base_v141_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 63)
    result = base * np.log((sgna * 10.0).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v142: 21d accel × log(sgna) * closeadj
def f05dsf_f05_device_sales_force_scaling_accelxlogcap_21d_base_v142_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 21)
    result = base * np.log((sgna * 5.0).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v143: 63d accel × log(sgna) * closeadj
def f05dsf_f05_device_sales_force_scaling_accelxlogcap_63d_base_v143_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 63)
    result = base * np.log((sgna * 5.0).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v144: 21d pulse × log(sgna) * closeadj
def f05dsf_f05_device_sales_force_scaling_pulsexlogcap_21d_base_v144_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 21)
    result = base * np.log((sgna * 5.0).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v145: 63d pulse × log(sgna) * closeadj
def f05dsf_f05_device_sales_force_scaling_pulsexlogcap_63d_base_v145_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 63)
    result = base * np.log((sgna * 5.0).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v146: 21d accel mean 126d * closeadj
def f05dsf_f05_device_sales_force_scaling_accelmean_126d_base_v146_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v147: 63d accel mean 504d * closeadj
def f05dsf_f05_device_sales_force_scaling_accelmean_504d_base_v147_signal(sgna, revenue, closeadj):
    base = _f05_sga_growth_gap(sgna, revenue, 63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v148: 21d pulse mean 126d * closeadj
def f05dsf_f05_device_sales_force_scaling_pulsemean_126dshort_base_v148_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v149: 63d pulse mean 504d * closeadj
def f05dsf_f05_device_sales_force_scaling_pulsemean_504d_base_v149_signal(sgna, revenue, closeadj):
    base = _f05_sga_to_revenue(sgna, revenue, 63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v150: 21d sig mean 504d * closeadj
def f05dsf_f05_device_sales_force_scaling_sigmean_504d_base_v150_signal(sgna, closeadj):
    base = _f05_sga_leverage_score(sgna, sgna, 21)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f05dsf_f05_device_sales_force_scaling_accelema_21d_base_v076_signal,
    f05dsf_f05_device_sales_force_scaling_accelema_63d_base_v077_signal,
    f05dsf_f05_device_sales_force_scaling_pulseema_21d_base_v078_signal,
    f05dsf_f05_device_sales_force_scaling_pulseema_63d_base_v079_signal,
    f05dsf_f05_device_sales_force_scaling_sigema_21d_base_v080_signal,
    f05dsf_f05_device_sales_force_scaling_sigema_63d_base_v081_signal,
    f05dsf_f05_device_sales_force_scaling_accelrank_21d_base_v082_signal,
    f05dsf_f05_device_sales_force_scaling_accelrank_63d_base_v083_signal,
    f05dsf_f05_device_sales_force_scaling_pulserank_21d_base_v084_signal,
    f05dsf_f05_device_sales_force_scaling_pulserank_63d_base_v085_signal,
    f05dsf_f05_device_sales_force_scaling_sigrank_21d_base_v086_signal,
    f05dsf_f05_device_sales_force_scaling_sigrank_63d_base_v087_signal,
    f05dsf_f05_device_sales_force_scaling_accellog_21d_base_v088_signal,
    f05dsf_f05_device_sales_force_scaling_accellog_63d_base_v089_signal,
    f05dsf_f05_device_sales_force_scaling_pulselog_21d_base_v090_signal,
    f05dsf_f05_device_sales_force_scaling_pulselog_63d_base_v091_signal,
    f05dsf_f05_device_sales_force_scaling_siglog_21d_base_v092_signal,
    f05dsf_f05_device_sales_force_scaling_siglog_63d_base_v093_signal,
    f05dsf_f05_device_sales_force_scaling_accelxpulse_21d_base_v094_signal,
    f05dsf_f05_device_sales_force_scaling_accelxpulse_63d_base_v095_signal,
    f05dsf_f05_device_sales_force_scaling_accelxsig_21d_base_v096_signal,
    f05dsf_f05_device_sales_force_scaling_accelxsig_63d_base_v097_signal,
    f05dsf_f05_device_sales_force_scaling_pulsexsig_21d_base_v098_signal,
    f05dsf_f05_device_sales_force_scaling_pulsexsig_63d_base_v099_signal,
    f05dsf_f05_device_sales_force_scaling_accelxshortlong_21d_base_v100_signal,
    f05dsf_f05_device_sales_force_scaling_accelxshortlong_63d_base_v101_signal,
    f05dsf_f05_device_sales_force_scaling_pulsexshortlong_21d_base_v102_signal,
    f05dsf_f05_device_sales_force_scaling_pulsexshortlong_63d_base_v103_signal,
    f05dsf_f05_device_sales_force_scaling_sigxshortlong_21d_base_v104_signal,
    f05dsf_f05_device_sales_force_scaling_sigxshortlong_63d_base_v105_signal,
    f05dsf_f05_device_sales_force_scaling_accelmax_21d_base_v106_signal,
    f05dsf_f05_device_sales_force_scaling_accelmax_63d_base_v107_signal,
    f05dsf_f05_device_sales_force_scaling_pulsemax_21d_base_v108_signal,
    f05dsf_f05_device_sales_force_scaling_pulsemax_63d_base_v109_signal,
    f05dsf_f05_device_sales_force_scaling_sigmax_21d_base_v110_signal,
    f05dsf_f05_device_sales_force_scaling_sigmax_63d_base_v111_signal,
    f05dsf_f05_device_sales_force_scaling_accelmin_21d_base_v112_signal,
    f05dsf_f05_device_sales_force_scaling_accelmin_63d_base_v113_signal,
    f05dsf_f05_device_sales_force_scaling_pulsemin_21d_base_v114_signal,
    f05dsf_f05_device_sales_force_scaling_pulsemin_63d_base_v115_signal,
    f05dsf_f05_device_sales_force_scaling_sigmin_21d_base_v116_signal,
    f05dsf_f05_device_sales_force_scaling_sigmin_63d_base_v117_signal,
    f05dsf_f05_device_sales_force_scaling_accelxmomp_21d_base_v118_signal,
    f05dsf_f05_device_sales_force_scaling_accelxmomp_63d_base_v119_signal,
    f05dsf_f05_device_sales_force_scaling_pulsexmomp_21d_base_v120_signal,
    f05dsf_f05_device_sales_force_scaling_pulsexmomp_63d_base_v121_signal,
    f05dsf_f05_device_sales_force_scaling_sigxmomp_21d_base_v122_signal,
    f05dsf_f05_device_sales_force_scaling_sigxmomp_63d_base_v123_signal,
    f05dsf_f05_device_sales_force_scaling_accelcum_21d_base_v124_signal,
    f05dsf_f05_device_sales_force_scaling_accelcum_63d_base_v125_signal,
    f05dsf_f05_device_sales_force_scaling_pulsecum_21d_base_v126_signal,
    f05dsf_f05_device_sales_force_scaling_pulsecum_63d_base_v127_signal,
    f05dsf_f05_device_sales_force_scaling_sigcum_21d_base_v128_signal,
    f05dsf_f05_device_sales_force_scaling_sigcum_63d_base_v129_signal,
    f05dsf_f05_device_sales_force_scaling_accelxinstg_21d_base_v130_signal,
    f05dsf_f05_device_sales_force_scaling_accelxinstg_63d_base_v131_signal,
    f05dsf_f05_device_sales_force_scaling_pulsexinstg_21d_base_v132_signal,
    f05dsf_f05_device_sales_force_scaling_pulsexinstg_63d_base_v133_signal,
    f05dsf_f05_device_sales_force_scaling_sigxinstg_21d_base_v134_signal,
    f05dsf_f05_device_sales_force_scaling_sigxinstg_63d_base_v135_signal,
    f05dsf_f05_device_sales_force_scaling_accelxlogrev_21d_base_v136_signal,
    f05dsf_f05_device_sales_force_scaling_accelxlogrev_63d_base_v137_signal,
    f05dsf_f05_device_sales_force_scaling_pulsexlogrev_21d_base_v138_signal,
    f05dsf_f05_device_sales_force_scaling_pulsexlogrev_63d_base_v139_signal,
    f05dsf_f05_device_sales_force_scaling_sigxlogrev_21d_base_v140_signal,
    f05dsf_f05_device_sales_force_scaling_sigxlogrev_63d_base_v141_signal,
    f05dsf_f05_device_sales_force_scaling_accelxlogcap_21d_base_v142_signal,
    f05dsf_f05_device_sales_force_scaling_accelxlogcap_63d_base_v143_signal,
    f05dsf_f05_device_sales_force_scaling_pulsexlogcap_21d_base_v144_signal,
    f05dsf_f05_device_sales_force_scaling_pulsexlogcap_63d_base_v145_signal,
    f05dsf_f05_device_sales_force_scaling_accelmean_126d_base_v146_signal,
    f05dsf_f05_device_sales_force_scaling_accelmean_504d_base_v147_signal,
    f05dsf_f05_device_sales_force_scaling_pulsemean_126dshort_base_v148_signal,
    f05dsf_f05_device_sales_force_scaling_pulsemean_504d_base_v149_signal,
    f05dsf_f05_device_sales_force_scaling_sigmean_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F05_DEVICE_SALES_FORCE_SCALING_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    sgna = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    opex = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")

    cols = {"closeadj": closeadj, "sgna": sgna, "revenue": revenue, "opex": opex}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f05_sga_growth_gap", "_f05_sga_to_revenue", "_f05_sga_leverage_score")
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
    print(f"OK f05_device_sales_force_scaling_base_076_150_claude: {n_features} features pass")
