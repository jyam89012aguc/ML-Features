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
def _f04_rd_efficiency(rnd, revenue, w):
    rev_g = revenue.pct_change(periods=w)
    rd_g = rnd.pct_change(periods=w)
    return rev_g - rd_g


def _f04_rd_intensity(rnd, revenue, w):
    ratio = rnd / revenue.replace(0, np.nan).abs()
    base = ratio.rolling(w * 4, min_periods=max(1, w)).mean()
    return (ratio - base) / base.replace(0, np.nan).abs()


def _f04_rd_productivity(rnd, revenue, w):
    rev_g = revenue.pct_change(periods=w)
    rd_g = rnd.pct_change(periods=w)
    return rev_g - 0.5 * rd_g


# v076: 21d rnd acceleration EMA 63d * closeadj
def f04dre_f04_device_rd_efficiency_accelema_21d_base_v076_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v077: 63d rnd acceleration EMA 126d * closeadj
def f04dre_f04_device_rd_efficiency_accelema_63d_base_v077_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v078: 21d launch pulse EMA 63d * closeadj
def f04dre_f04_device_rd_efficiency_pulseema_21d_base_v078_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v079: 63d launch pulse EMA 252d * closeadj
def f04dre_f04_device_rd_efficiency_pulseema_63d_base_v079_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v080: 21d signature EMA 63d * closeadj
def f04dre_f04_device_rd_efficiency_sigema_21d_base_v080_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v081: 63d signature EMA 252d * closeadj
def f04dre_f04_device_rd_efficiency_sigema_63d_base_v081_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 63)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v082: 21d rnd acceleration rank 252d * closeadj
def f04dre_f04_device_rd_efficiency_accelrank_21d_base_v082_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21)
    result = _rank(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v083: 63d rnd acceleration rank 504d * closeadj
def f04dre_f04_device_rd_efficiency_accelrank_63d_base_v083_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63)
    result = _rank(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v084: 21d launch pulse rank 252d * closeadj
def f04dre_f04_device_rd_efficiency_pulserank_21d_base_v084_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21)
    result = _rank(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v085: 63d launch pulse rank 504d * closeadj
def f04dre_f04_device_rd_efficiency_pulserank_63d_base_v085_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63)
    result = _rank(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v086: 21d signature rank 252d * closeadj
def f04dre_f04_device_rd_efficiency_sigrank_21d_base_v086_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21)
    result = _rank(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v087: 63d signature rank 504d * closeadj
def f04dre_f04_device_rd_efficiency_sigrank_63d_base_v087_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 63)
    result = _rank(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v088: 21d rnd acceleration log magnitude * closeadj * sign
def f04dre_f04_device_rd_efficiency_accellog_21d_base_v088_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21)
    result = _logabs(base) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v089: 63d rnd acceleration log magnitude * closeadj * sign
def f04dre_f04_device_rd_efficiency_accellog_63d_base_v089_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63)
    result = _logabs(base) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v090: 21d pulse log magnitude * closeadj * sign
def f04dre_f04_device_rd_efficiency_pulselog_21d_base_v090_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21)
    result = _logabs(base) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v091: 63d pulse log magnitude * closeadj * sign
def f04dre_f04_device_rd_efficiency_pulselog_63d_base_v091_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63)
    result = _logabs(base) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v092: 21d signature log magnitude * closeadj * sign
def f04dre_f04_device_rd_efficiency_siglog_21d_base_v092_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21)
    result = _logabs(base) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v093: 63d signature log magnitude * closeadj * sign
def f04dre_f04_device_rd_efficiency_siglog_63d_base_v093_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 63)
    result = _logabs(base) * np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v094: 21d accel × 21d pulse interaction * closeadj
def f04dre_f04_device_rd_efficiency_accelxpulse_21d_base_v094_signal(rnd, revenue, closeadj):
    a = _f04_rd_efficiency(rnd, revenue, 21)
    p = _f04_rd_intensity(rnd, revenue, 21)
    result = a * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v095: 63d accel × 63d pulse interaction * closeadj
def f04dre_f04_device_rd_efficiency_accelxpulse_63d_base_v095_signal(rnd, revenue, closeadj):
    a = _f04_rd_efficiency(rnd, revenue, 63)
    p = _f04_rd_intensity(rnd, revenue, 63)
    result = a * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v096: 21d accel × 21d signature interaction * closeadj
def f04dre_f04_device_rd_efficiency_accelxsig_21d_base_v096_signal(rnd, revenue, closeadj):
    a = _f04_rd_efficiency(rnd, revenue, 21)
    s = _f04_rd_productivity(rnd, rnd, 21)
    result = a * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v097: 63d accel × 63d signature interaction * closeadj
def f04dre_f04_device_rd_efficiency_accelxsig_63d_base_v097_signal(rnd, revenue, closeadj):
    a = _f04_rd_efficiency(rnd, revenue, 63)
    s = _f04_rd_productivity(rnd, rnd, 63)
    result = a * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v098: 21d pulse × 21d signature interaction * closeadj
def f04dre_f04_device_rd_efficiency_pulsexsig_21d_base_v098_signal(rnd, revenue, closeadj):
    p = _f04_rd_intensity(rnd, revenue, 21)
    s = _f04_rd_productivity(rnd, rnd, 21)
    result = p * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v099: 63d pulse × 63d signature interaction * closeadj
def f04dre_f04_device_rd_efficiency_pulsexsig_63d_base_v099_signal(rnd, revenue, closeadj):
    p = _f04_rd_intensity(rnd, revenue, 63)
    s = _f04_rd_productivity(rnd, rnd, 63)
    result = p * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v100: 21d accel - 63d accel (short minus long) * closeadj
def f04dre_f04_device_rd_efficiency_accelxshortlong_21d_base_v100_signal(rnd, revenue, closeadj):
    a_s = _f04_rd_efficiency(rnd, revenue, 21)
    a_l = _f04_rd_efficiency(rnd, revenue, 63)
    result = (a_s - a_l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v101: 63d accel - 252d accel * closeadj
def f04dre_f04_device_rd_efficiency_accelxshortlong_63d_base_v101_signal(rnd, revenue, closeadj):
    a_s = _f04_rd_efficiency(rnd, revenue, 63)
    a_l = _f04_rd_efficiency(rnd, revenue, 252)
    result = (a_s - a_l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v102: 21d pulse - 63d pulse * closeadj
def f04dre_f04_device_rd_efficiency_pulsexshortlong_21d_base_v102_signal(rnd, revenue, closeadj):
    p_s = _f04_rd_intensity(rnd, revenue, 21)
    p_l = _f04_rd_intensity(rnd, revenue, 63)
    result = (p_s - p_l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v103: 63d pulse - 252d pulse * closeadj
def f04dre_f04_device_rd_efficiency_pulsexshortlong_63d_base_v103_signal(rnd, revenue, closeadj):
    p_s = _f04_rd_intensity(rnd, revenue, 63)
    p_l = _f04_rd_intensity(rnd, revenue, 252)
    result = (p_s - p_l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v104: 21d sig - 63d sig * closeadj
def f04dre_f04_device_rd_efficiency_sigxshortlong_21d_base_v104_signal(rnd, closeadj):
    s_s = _f04_rd_productivity(rnd, rnd, 21)
    s_l = _f04_rd_productivity(rnd, rnd, 63)
    result = (s_s - s_l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v105: 63d sig - 252d sig * closeadj
def f04dre_f04_device_rd_efficiency_sigxshortlong_63d_base_v105_signal(rnd, closeadj):
    s_s = _f04_rd_productivity(rnd, rnd, 63)
    s_l = _f04_rd_productivity(rnd, rnd, 252)
    result = (s_s - s_l) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v106: 21d accel rolling max 63d * closeadj
def f04dre_f04_device_rd_efficiency_accelmax_21d_base_v106_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21)
    result = base.rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v107: 63d accel rolling max 252d * closeadj
def f04dre_f04_device_rd_efficiency_accelmax_63d_base_v107_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v108: 21d pulse rolling max 63d * closeadj
def f04dre_f04_device_rd_efficiency_pulsemax_21d_base_v108_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21)
    result = base.rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v109: 63d pulse rolling max 252d * closeadj
def f04dre_f04_device_rd_efficiency_pulsemax_63d_base_v109_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v110: 21d sig rolling max 63d * closeadj
def f04dre_f04_device_rd_efficiency_sigmax_21d_base_v110_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21)
    result = base.rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v111: 63d sig rolling max 252d * closeadj
def f04dre_f04_device_rd_efficiency_sigmax_63d_base_v111_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v112: 21d accel rolling min 63d * closeadj
def f04dre_f04_device_rd_efficiency_accelmin_21d_base_v112_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21)
    result = base.rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v113: 63d accel rolling min 252d * closeadj
def f04dre_f04_device_rd_efficiency_accelmin_63d_base_v113_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v114: 21d pulse rolling min 63d * closeadj
def f04dre_f04_device_rd_efficiency_pulsemin_21d_base_v114_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21)
    result = base.rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v115: 63d pulse rolling min 252d * closeadj
def f04dre_f04_device_rd_efficiency_pulsemin_63d_base_v115_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v116: 21d sig rolling min 63d * closeadj
def f04dre_f04_device_rd_efficiency_sigmin_21d_base_v116_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21)
    result = base.rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v117: 63d sig rolling min 252d * closeadj
def f04dre_f04_device_rd_efficiency_sigmin_63d_base_v117_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 63)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v118: 21d accel × closeadj momentum (closeadj 63d return)
def f04dre_f04_device_rd_efficiency_accelxmomp_21d_base_v118_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21)
    mom = closeadj.pct_change(63)
    result = base * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v119: 63d accel × closeadj momentum 252d
def f04dre_f04_device_rd_efficiency_accelxmomp_63d_base_v119_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63)
    mom = closeadj.pct_change(252)
    result = base * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v120: 21d pulse × closeadj momentum
def f04dre_f04_device_rd_efficiency_pulsexmomp_21d_base_v120_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21)
    mom = closeadj.pct_change(63)
    result = base * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v121: 63d pulse × closeadj momentum 252d
def f04dre_f04_device_rd_efficiency_pulsexmomp_63d_base_v121_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63)
    mom = closeadj.pct_change(252)
    result = base * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v122: 21d sig × closeadj momentum
def f04dre_f04_device_rd_efficiency_sigxmomp_21d_base_v122_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21)
    mom = closeadj.pct_change(63)
    result = base * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v123: 63d sig × closeadj momentum 252d
def f04dre_f04_device_rd_efficiency_sigxmomp_63d_base_v123_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 63)
    mom = closeadj.pct_change(252)
    result = base * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v124: 21d accel cumulative sum 63d * closeadj
def f04dre_f04_device_rd_efficiency_accelcum_21d_base_v124_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21)
    result = base.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v125: 63d accel cumulative sum 252d * closeadj
def f04dre_f04_device_rd_efficiency_accelcum_63d_base_v125_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v126: 21d pulse cum sum 63d * closeadj
def f04dre_f04_device_rd_efficiency_pulsecum_21d_base_v126_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21)
    result = base.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v127: 63d pulse cum sum 252d * closeadj
def f04dre_f04_device_rd_efficiency_pulsecum_63d_base_v127_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v128: 21d sig cum sum 63d * closeadj
def f04dre_f04_device_rd_efficiency_sigcum_21d_base_v128_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21)
    result = base.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v129: 63d sig cum sum 252d * closeadj
def f04dre_f04_device_rd_efficiency_sigcum_63d_base_v129_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 63)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v130: 21d accel × rnd growth 252d * closeadj
def f04dre_f04_device_rd_efficiency_accelxinstg_21d_base_v130_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21)
    inst_g = (rnd * 100.0).pct_change(252)
    result = base * inst_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v131: 63d accel × rnd growth 252d * closeadj
def f04dre_f04_device_rd_efficiency_accelxinstg_63d_base_v131_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63)
    inst_g = (rnd * 100.0).pct_change(252)
    result = base * inst_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v132: 21d pulse × rnd growth 252d * closeadj
def f04dre_f04_device_rd_efficiency_pulsexinstg_21d_base_v132_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21)
    inst_g = (rnd * 100.0).pct_change(252)
    result = base * inst_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v133: 63d pulse × rnd growth 252d * closeadj
def f04dre_f04_device_rd_efficiency_pulsexinstg_63d_base_v133_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63)
    inst_g = (rnd * 100.0).pct_change(252)
    result = base * inst_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v134: 21d sig × rnd growth 252d * closeadj
def f04dre_f04_device_rd_efficiency_sigxinstg_21d_base_v134_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21)
    inst_g = (rnd * 100.0).pct_change(252)
    result = base * inst_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v135: 63d sig × rnd growth 252d * closeadj
def f04dre_f04_device_rd_efficiency_sigxinstg_63d_base_v135_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 63)
    inst_g = (rnd * 100.0).pct_change(252)
    result = base * inst_g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v136: 21d accel × log(rnd) * closeadj
def f04dre_f04_device_rd_efficiency_accelxlogrev_21d_base_v136_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21)
    result = base * np.log((rnd * 10.0).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v137: 63d accel × log(rnd) * closeadj
def f04dre_f04_device_rd_efficiency_accelxlogrev_63d_base_v137_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63)
    result = base * np.log((rnd * 10.0).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v138: 21d pulse × log(rnd) * closeadj
def f04dre_f04_device_rd_efficiency_pulsexlogrev_21d_base_v138_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21)
    result = base * np.log((rnd * 10.0).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v139: 63d pulse × log(rnd) * closeadj
def f04dre_f04_device_rd_efficiency_pulsexlogrev_63d_base_v139_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63)
    result = base * np.log((rnd * 10.0).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v140: 21d sig × log(rnd) * closeadj
def f04dre_f04_device_rd_efficiency_sigxlogrev_21d_base_v140_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21)
    result = base * np.log((rnd * 10.0).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v141: 63d sig × log(rnd) * closeadj
def f04dre_f04_device_rd_efficiency_sigxlogrev_63d_base_v141_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 63)
    result = base * np.log((rnd * 10.0).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v142: 21d accel × log(rnd) * closeadj
def f04dre_f04_device_rd_efficiency_accelxlogcap_21d_base_v142_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21)
    result = base * np.log((rnd * 5.0).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v143: 63d accel × log(rnd) * closeadj
def f04dre_f04_device_rd_efficiency_accelxlogcap_63d_base_v143_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63)
    result = base * np.log((rnd * 5.0).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v144: 21d pulse × log(rnd) * closeadj
def f04dre_f04_device_rd_efficiency_pulsexlogcap_21d_base_v144_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21)
    result = base * np.log((rnd * 5.0).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v145: 63d pulse × log(rnd) * closeadj
def f04dre_f04_device_rd_efficiency_pulsexlogcap_63d_base_v145_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63)
    result = base * np.log((rnd * 5.0).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v146: 21d accel mean 126d * closeadj
def f04dre_f04_device_rd_efficiency_accelmean_126d_base_v146_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v147: 63d accel mean 504d * closeadj
def f04dre_f04_device_rd_efficiency_accelmean_504d_base_v147_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v148: 21d pulse mean 126d * closeadj
def f04dre_f04_device_rd_efficiency_pulsemean_126dshort_base_v148_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v149: 63d pulse mean 504d * closeadj
def f04dre_f04_device_rd_efficiency_pulsemean_504d_base_v149_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v150: 21d sig mean 504d * closeadj
def f04dre_f04_device_rd_efficiency_sigmean_504d_base_v150_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f04dre_f04_device_rd_efficiency_accelema_21d_base_v076_signal,
    f04dre_f04_device_rd_efficiency_accelema_63d_base_v077_signal,
    f04dre_f04_device_rd_efficiency_pulseema_21d_base_v078_signal,
    f04dre_f04_device_rd_efficiency_pulseema_63d_base_v079_signal,
    f04dre_f04_device_rd_efficiency_sigema_21d_base_v080_signal,
    f04dre_f04_device_rd_efficiency_sigema_63d_base_v081_signal,
    f04dre_f04_device_rd_efficiency_accelrank_21d_base_v082_signal,
    f04dre_f04_device_rd_efficiency_accelrank_63d_base_v083_signal,
    f04dre_f04_device_rd_efficiency_pulserank_21d_base_v084_signal,
    f04dre_f04_device_rd_efficiency_pulserank_63d_base_v085_signal,
    f04dre_f04_device_rd_efficiency_sigrank_21d_base_v086_signal,
    f04dre_f04_device_rd_efficiency_sigrank_63d_base_v087_signal,
    f04dre_f04_device_rd_efficiency_accellog_21d_base_v088_signal,
    f04dre_f04_device_rd_efficiency_accellog_63d_base_v089_signal,
    f04dre_f04_device_rd_efficiency_pulselog_21d_base_v090_signal,
    f04dre_f04_device_rd_efficiency_pulselog_63d_base_v091_signal,
    f04dre_f04_device_rd_efficiency_siglog_21d_base_v092_signal,
    f04dre_f04_device_rd_efficiency_siglog_63d_base_v093_signal,
    f04dre_f04_device_rd_efficiency_accelxpulse_21d_base_v094_signal,
    f04dre_f04_device_rd_efficiency_accelxpulse_63d_base_v095_signal,
    f04dre_f04_device_rd_efficiency_accelxsig_21d_base_v096_signal,
    f04dre_f04_device_rd_efficiency_accelxsig_63d_base_v097_signal,
    f04dre_f04_device_rd_efficiency_pulsexsig_21d_base_v098_signal,
    f04dre_f04_device_rd_efficiency_pulsexsig_63d_base_v099_signal,
    f04dre_f04_device_rd_efficiency_accelxshortlong_21d_base_v100_signal,
    f04dre_f04_device_rd_efficiency_accelxshortlong_63d_base_v101_signal,
    f04dre_f04_device_rd_efficiency_pulsexshortlong_21d_base_v102_signal,
    f04dre_f04_device_rd_efficiency_pulsexshortlong_63d_base_v103_signal,
    f04dre_f04_device_rd_efficiency_sigxshortlong_21d_base_v104_signal,
    f04dre_f04_device_rd_efficiency_sigxshortlong_63d_base_v105_signal,
    f04dre_f04_device_rd_efficiency_accelmax_21d_base_v106_signal,
    f04dre_f04_device_rd_efficiency_accelmax_63d_base_v107_signal,
    f04dre_f04_device_rd_efficiency_pulsemax_21d_base_v108_signal,
    f04dre_f04_device_rd_efficiency_pulsemax_63d_base_v109_signal,
    f04dre_f04_device_rd_efficiency_sigmax_21d_base_v110_signal,
    f04dre_f04_device_rd_efficiency_sigmax_63d_base_v111_signal,
    f04dre_f04_device_rd_efficiency_accelmin_21d_base_v112_signal,
    f04dre_f04_device_rd_efficiency_accelmin_63d_base_v113_signal,
    f04dre_f04_device_rd_efficiency_pulsemin_21d_base_v114_signal,
    f04dre_f04_device_rd_efficiency_pulsemin_63d_base_v115_signal,
    f04dre_f04_device_rd_efficiency_sigmin_21d_base_v116_signal,
    f04dre_f04_device_rd_efficiency_sigmin_63d_base_v117_signal,
    f04dre_f04_device_rd_efficiency_accelxmomp_21d_base_v118_signal,
    f04dre_f04_device_rd_efficiency_accelxmomp_63d_base_v119_signal,
    f04dre_f04_device_rd_efficiency_pulsexmomp_21d_base_v120_signal,
    f04dre_f04_device_rd_efficiency_pulsexmomp_63d_base_v121_signal,
    f04dre_f04_device_rd_efficiency_sigxmomp_21d_base_v122_signal,
    f04dre_f04_device_rd_efficiency_sigxmomp_63d_base_v123_signal,
    f04dre_f04_device_rd_efficiency_accelcum_21d_base_v124_signal,
    f04dre_f04_device_rd_efficiency_accelcum_63d_base_v125_signal,
    f04dre_f04_device_rd_efficiency_pulsecum_21d_base_v126_signal,
    f04dre_f04_device_rd_efficiency_pulsecum_63d_base_v127_signal,
    f04dre_f04_device_rd_efficiency_sigcum_21d_base_v128_signal,
    f04dre_f04_device_rd_efficiency_sigcum_63d_base_v129_signal,
    f04dre_f04_device_rd_efficiency_accelxinstg_21d_base_v130_signal,
    f04dre_f04_device_rd_efficiency_accelxinstg_63d_base_v131_signal,
    f04dre_f04_device_rd_efficiency_pulsexinstg_21d_base_v132_signal,
    f04dre_f04_device_rd_efficiency_pulsexinstg_63d_base_v133_signal,
    f04dre_f04_device_rd_efficiency_sigxinstg_21d_base_v134_signal,
    f04dre_f04_device_rd_efficiency_sigxinstg_63d_base_v135_signal,
    f04dre_f04_device_rd_efficiency_accelxlogrev_21d_base_v136_signal,
    f04dre_f04_device_rd_efficiency_accelxlogrev_63d_base_v137_signal,
    f04dre_f04_device_rd_efficiency_pulsexlogrev_21d_base_v138_signal,
    f04dre_f04_device_rd_efficiency_pulsexlogrev_63d_base_v139_signal,
    f04dre_f04_device_rd_efficiency_sigxlogrev_21d_base_v140_signal,
    f04dre_f04_device_rd_efficiency_sigxlogrev_63d_base_v141_signal,
    f04dre_f04_device_rd_efficiency_accelxlogcap_21d_base_v142_signal,
    f04dre_f04_device_rd_efficiency_accelxlogcap_63d_base_v143_signal,
    f04dre_f04_device_rd_efficiency_pulsexlogcap_21d_base_v144_signal,
    f04dre_f04_device_rd_efficiency_pulsexlogcap_63d_base_v145_signal,
    f04dre_f04_device_rd_efficiency_accelmean_126d_base_v146_signal,
    f04dre_f04_device_rd_efficiency_accelmean_504d_base_v147_signal,
    f04dre_f04_device_rd_efficiency_pulsemean_126dshort_base_v148_signal,
    f04dre_f04_device_rd_efficiency_pulsemean_504d_base_v149_signal,
    f04dre_f04_device_rd_efficiency_sigmean_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F04_DEVICE_RD_EFFICIENCY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    rnd = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")

    cols = {"closeadj": closeadj, "rnd": rnd, "revenue": revenue}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f04_rd_efficiency", "_f04_rd_intensity", "_f04_rd_productivity")
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
    print(f"OK f04_device_rd_efficiency_base_076_150_claude: {n_features} features pass")
