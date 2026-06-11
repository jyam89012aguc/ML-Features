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


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f11_own_ret(s):
    return s.pct_change()


def _f11_log_ret(s, n=1):
    return np.log(s / s.shift(n))


def _f11_mom(s, n):
    return s / s.shift(n) - 1.0


def _f11_accel(s, n):
    return (s / s.shift(n) - 1.0) - (s.shift(n) / s.shift(2 * n) - 1.0)


# 21d robust z of 21d acceleration
def f11ac_f11_semi_acceleration_accelrobustz_21d_base_v076_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    med = a.rolling(21, min_periods=11).median()
    mad = (a - med).abs().rolling(21, min_periods=11).median()
    result = (a - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z of 21d acceleration
def f11ac_f11_semi_acceleration_accelrobustz_63d_base_v077_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    med = a.rolling(63, min_periods=32).median()
    mad = (a - med).abs().rolling(63, min_periods=32).median()
    result = (a - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z of 21d acceleration
def f11ac_f11_semi_acceleration_accelrobustz_126d_base_v078_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    med = a.rolling(126, min_periods=63).median()
    mad = (a - med).abs().rolling(126, min_periods=63).median()
    result = (a - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z of 21d acceleration
def f11ac_f11_semi_acceleration_accelrobustz_252d_base_v079_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    med = a.rolling(252, min_periods=126).median()
    mad = (a - med).abs().rolling(252, min_periods=126).median()
    result = (a - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z of 21d acceleration
def f11ac_f11_semi_acceleration_accelrobustz_504d_base_v080_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    med = a.rolling(504, min_periods=252).median()
    mad = (a - med).abs().rolling(504, min_periods=252).median()
    result = (a - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of cumulative acceleration
def f11ac_f11_semi_acceleration_accelcumdd_21d_base_v081_signal(closeadj):
    a = _f11_accel(closeadj, 21).rolling(21, min_periods=11).sum()
    result = a - _max(a, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of cumulative acceleration
def f11ac_f11_semi_acceleration_accelcumdd_63d_base_v082_signal(closeadj):
    a = _f11_accel(closeadj, 21).rolling(63, min_periods=32).sum()
    result = a - _max(a, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of cumulative acceleration
def f11ac_f11_semi_acceleration_accelcumdd_126d_base_v083_signal(closeadj):
    a = _f11_accel(closeadj, 21).rolling(126, min_periods=63).sum()
    result = a - _max(a, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of cumulative acceleration
def f11ac_f11_semi_acceleration_accelcumdd_252d_base_v084_signal(closeadj):
    a = _f11_accel(closeadj, 21).rolling(252, min_periods=126).sum()
    result = a - _max(a, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of cumulative acceleration
def f11ac_f11_semi_acceleration_accelcumdd_504d_base_v085_signal(closeadj):
    a = _f11_accel(closeadj, 21).rolling(504, min_periods=252).sum()
    result = a - _max(a, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of cumulative acceleration
def f11ac_f11_semi_acceleration_accelcumup_21d_base_v086_signal(closeadj):
    a = _f11_accel(closeadj, 21).rolling(21, min_periods=11).sum()
    result = a - _min(a, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of cumulative acceleration
def f11ac_f11_semi_acceleration_accelcumup_63d_base_v087_signal(closeadj):
    a = _f11_accel(closeadj, 21).rolling(63, min_periods=32).sum()
    result = a - _min(a, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of cumulative acceleration
def f11ac_f11_semi_acceleration_accelcumup_126d_base_v088_signal(closeadj):
    a = _f11_accel(closeadj, 21).rolling(126, min_periods=63).sum()
    result = a - _min(a, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of cumulative acceleration
def f11ac_f11_semi_acceleration_accelcumup_252d_base_v089_signal(closeadj):
    a = _f11_accel(closeadj, 21).rolling(252, min_periods=126).sum()
    result = a - _min(a, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of cumulative acceleration
def f11ac_f11_semi_acceleration_accelcumup_504d_base_v090_signal(closeadj):
    a = _f11_accel(closeadj, 21).rolling(504, min_periods=252).sum()
    result = a - _min(a, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of 21d acceleration
def f11ac_f11_semi_acceleration_accelskew_21d_base_v091_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = a.rolling(21, min_periods=11).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of 21d acceleration
def f11ac_f11_semi_acceleration_accelskew_63d_base_v092_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = a.rolling(63, min_periods=32).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of 21d acceleration
def f11ac_f11_semi_acceleration_accelskew_126d_base_v093_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = a.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of 21d acceleration
def f11ac_f11_semi_acceleration_accelskew_252d_base_v094_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = a.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of 21d acceleration
def f11ac_f11_semi_acceleration_accelskew_504d_base_v095_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = a.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of 21d acceleration
def f11ac_f11_semi_acceleration_accelkurt_21d_base_v096_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = a.rolling(21, min_periods=11).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of 21d acceleration
def f11ac_f11_semi_acceleration_accelkurt_63d_base_v097_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = a.rolling(63, min_periods=32).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of 21d acceleration
def f11ac_f11_semi_acceleration_accelkurt_126d_base_v098_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = a.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of 21d acceleration
def f11ac_f11_semi_acceleration_accelkurt_252d_base_v099_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = a.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of 21d acceleration
def f11ac_f11_semi_acceleration_accelkurt_504d_base_v100_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = a.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position-in-range of acceleration
def f11ac_f11_semi_acceleration_accelpos_21d_base_v101_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    lo = _min(a, 21)
    hi = _max(a, 21)
    result = (a - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position-in-range of acceleration
def f11ac_f11_semi_acceleration_accelpos_63d_base_v102_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    lo = _min(a, 63)
    hi = _max(a, 63)
    result = (a - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position-in-range of acceleration
def f11ac_f11_semi_acceleration_accelpos_126d_base_v103_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    lo = _min(a, 126)
    hi = _max(a, 126)
    result = (a - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of acceleration
def f11ac_f11_semi_acceleration_accelpos_252d_base_v104_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    lo = _min(a, 252)
    hi = _max(a, 252)
    result = (a - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of acceleration
def f11ac_f11_semi_acceleration_accelpos_504d_base_v105_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    lo = _min(a, 504)
    hi = _max(a, 504)
    result = (a - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of decel transitions (positive to negative)
def f11ac_f11_semi_acceleration_deceltrans_21d_base_v106_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    trans = ((a < 0) & (a.shift(1) > 0)).astype(float)
    result = trans.rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of decel transitions (positive to negative)
def f11ac_f11_semi_acceleration_deceltrans_63d_base_v107_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    trans = ((a < 0) & (a.shift(1) > 0)).astype(float)
    result = trans.rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of decel transitions (positive to negative)
def f11ac_f11_semi_acceleration_deceltrans_126d_base_v108_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    trans = ((a < 0) & (a.shift(1) > 0)).astype(float)
    result = trans.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of decel transitions (positive to negative)
def f11ac_f11_semi_acceleration_deceltrans_252d_base_v109_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    trans = ((a < 0) & (a.shift(1) > 0)).astype(float)
    result = trans.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of decel transitions (positive to negative)
def f11ac_f11_semi_acceleration_deceltrans_504d_base_v110_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    trans = ((a < 0) & (a.shift(1) > 0)).astype(float)
    result = trans.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of re-acceleration transitions (neg to pos)
def f11ac_f11_semi_acceleration_reacceltrans_21d_base_v111_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    trans = ((a > 0) & (a.shift(1) < 0)).astype(float)
    result = trans.rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of re-acceleration transitions (neg to pos)
def f11ac_f11_semi_acceleration_reacceltrans_63d_base_v112_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    trans = ((a > 0) & (a.shift(1) < 0)).astype(float)
    result = trans.rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of re-acceleration transitions (neg to pos)
def f11ac_f11_semi_acceleration_reacceltrans_126d_base_v113_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    trans = ((a > 0) & (a.shift(1) < 0)).astype(float)
    result = trans.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of re-acceleration transitions (neg to pos)
def f11ac_f11_semi_acceleration_reacceltrans_252d_base_v114_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    trans = ((a > 0) & (a.shift(1) < 0)).astype(float)
    result = trans.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of re-acceleration transitions (neg to pos)
def f11ac_f11_semi_acceleration_reacceltrans_504d_base_v115_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    trans = ((a > 0) & (a.shift(1) < 0)).astype(float)
    result = trans.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sustained positive acceleration ratio (consecutive)
def f11ac_f11_semi_acceleration_sustaccelratio_21d_base_v116_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    sign = (a > 0).astype(int) - (a < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumsum().where(sign > 0, 0.0)
    result = streak.rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sustained positive acceleration ratio (consecutive)
def f11ac_f11_semi_acceleration_sustaccelratio_63d_base_v117_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    sign = (a > 0).astype(int) - (a < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumsum().where(sign > 0, 0.0)
    result = streak.rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d sustained positive acceleration ratio (consecutive)
def f11ac_f11_semi_acceleration_sustaccelratio_126d_base_v118_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    sign = (a > 0).astype(int) - (a < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumsum().where(sign > 0, 0.0)
    result = streak.rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sustained positive acceleration ratio (consecutive)
def f11ac_f11_semi_acceleration_sustaccelratio_252d_base_v119_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    sign = (a > 0).astype(int) - (a < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumsum().where(sign > 0, 0.0)
    result = streak.rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sustained positive acceleration ratio (consecutive)
def f11ac_f11_semi_acceleration_sustaccelratio_504d_base_v120_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    sign = (a > 0).astype(int) - (a < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumsum().where(sign > 0, 0.0)
    result = streak.rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ratio of recent 5d mom to recent 21d mom
def f11ac_f11_semi_acceleration_mom5over21_21d_base_v121_signal(closeadj):
    m5 = closeadj / closeadj.shift(5) - 1.0
    m21 = closeadj / closeadj.shift(21) - 1.0
    result = (m5 / m21.replace(0, np.nan)).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ratio of recent 5d mom to recent 21d mom
def f11ac_f11_semi_acceleration_mom5over21_63d_base_v122_signal(closeadj):
    m5 = closeadj / closeadj.shift(5) - 1.0
    m21 = closeadj / closeadj.shift(21) - 1.0
    result = (m5 / m21.replace(0, np.nan)).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ratio of recent 5d mom to recent 21d mom
def f11ac_f11_semi_acceleration_mom5over21_126d_base_v123_signal(closeadj):
    m5 = closeadj / closeadj.shift(5) - 1.0
    m21 = closeadj / closeadj.shift(21) - 1.0
    result = (m5 / m21.replace(0, np.nan)).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ratio of recent 5d mom to recent 21d mom
def f11ac_f11_semi_acceleration_mom5over21_252d_base_v124_signal(closeadj):
    m5 = closeadj / closeadj.shift(5) - 1.0
    m21 = closeadj / closeadj.shift(21) - 1.0
    result = (m5 / m21.replace(0, np.nan)).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ratio of recent 5d mom to recent 21d mom
def f11ac_f11_semi_acceleration_mom5over21_504d_base_v125_signal(closeadj):
    m5 = closeadj / closeadj.shift(5) - 1.0
    m21 = closeadj / closeadj.shift(21) - 1.0
    result = (m5 / m21.replace(0, np.nan)).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d acceleration conditional on prior up-trend
def f11ac_f11_semi_acceleration_accelcondup_21d_base_v126_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    prior = closeadj.shift(21) / closeadj.shift(42) - 1.0
    result = _mean(a.where(prior > 0), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration conditional on prior up-trend
def f11ac_f11_semi_acceleration_accelcondup_63d_base_v127_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    prior = closeadj.shift(21) / closeadj.shift(42) - 1.0
    result = _mean(a.where(prior > 0), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d acceleration conditional on prior up-trend
def f11ac_f11_semi_acceleration_accelcondup_126d_base_v128_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    prior = closeadj.shift(21) / closeadj.shift(42) - 1.0
    result = _mean(a.where(prior > 0), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration conditional on prior up-trend
def f11ac_f11_semi_acceleration_accelcondup_252d_base_v129_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    prior = closeadj.shift(21) / closeadj.shift(42) - 1.0
    result = _mean(a.where(prior > 0), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d acceleration conditional on prior up-trend
def f11ac_f11_semi_acceleration_accelcondup_504d_base_v130_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    prior = closeadj.shift(21) / closeadj.shift(42) - 1.0
    result = _mean(a.where(prior > 0), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d acceleration conditional on prior down-trend
def f11ac_f11_semi_acceleration_accelconddn_21d_base_v131_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    prior = closeadj.shift(21) / closeadj.shift(42) - 1.0
    result = _mean(a.where(prior < 0), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration conditional on prior down-trend
def f11ac_f11_semi_acceleration_accelconddn_63d_base_v132_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    prior = closeadj.shift(21) / closeadj.shift(42) - 1.0
    result = _mean(a.where(prior < 0), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d acceleration conditional on prior down-trend
def f11ac_f11_semi_acceleration_accelconddn_126d_base_v133_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    prior = closeadj.shift(21) / closeadj.shift(42) - 1.0
    result = _mean(a.where(prior < 0), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration conditional on prior down-trend
def f11ac_f11_semi_acceleration_accelconddn_252d_base_v134_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    prior = closeadj.shift(21) / closeadj.shift(42) - 1.0
    result = _mean(a.where(prior < 0), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d acceleration conditional on prior down-trend
def f11ac_f11_semi_acceleration_accelconddn_504d_base_v135_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    prior = closeadj.shift(21) / closeadj.shift(42) - 1.0
    result = _mean(a.where(prior < 0), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d info ratio of 21d acceleration
def f11ac_f11_semi_acceleration_accelir_21d_base_v136_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = _mean(a, 21) / _std(a, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d info ratio of 21d acceleration
def f11ac_f11_semi_acceleration_accelir_63d_base_v137_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = _mean(a, 63) / _std(a, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d info ratio of 21d acceleration
def f11ac_f11_semi_acceleration_accelir_126d_base_v138_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = _mean(a, 126) / _std(a, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d info ratio of 21d acceleration
def f11ac_f11_semi_acceleration_accelir_252d_base_v139_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = _mean(a, 252) / _std(a, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d info ratio of 21d acceleration
def f11ac_f11_semi_acceleration_accelir_504d_base_v140_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = _mean(a, 504) / _std(a, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration composite short (z21+z63+z126)
def f11ac_f11_semi_acceleration_accelcompshort_63d_base_v141_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = _z(a, 21) + _z(a, 63) + _z(a, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration composite long (z63+z126+z252)
def f11ac_f11_semi_acceleration_accelcomplong_252d_base_v142_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = _z(a, 63) + _z(a, 126) + _z(a, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration regime divergence (short EMA cross vs long EMA cross)
def f11ac_f11_semi_acceleration_accelregdiv_63d_base_v143_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    short = np.sign(a.ewm(span=21, adjust=False).mean() - a.ewm(span=63, adjust=False).mean())
    long = np.sign(a.ewm(span=126, adjust=False).mean() - a.ewm(span=252, adjust=False).mean())
    result = pd.Series(short - long, index=a.index)
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration quality 63d (IR x hit ratio)
def f11ac_f11_semi_acceleration_accelquality63_63d_base_v144_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    ir = _mean(a, 63) / _std(a, 63).replace(0, np.nan)
    hit = (a > 0).astype(float).rolling(63, min_periods=32).mean()
    result = ir * hit
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration quality 252d (IR x hit ratio)
def f11ac_f11_semi_acceleration_accelquality252_252d_base_v145_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    ir = _mean(a, 252) / _std(a, 252).replace(0, np.nan)
    hit = (a > 0).astype(float).rolling(252, min_periods=126).mean()
    result = ir * hit
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of acceleration from rolling peak
def f11ac_f11_semi_acceleration_acceldd_21d_base_v146_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = a - _max(a, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of acceleration from rolling peak
def f11ac_f11_semi_acceleration_acceldd_63d_base_v147_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = a - _max(a, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of acceleration from rolling peak
def f11ac_f11_semi_acceleration_acceldd_126d_base_v148_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = a - _max(a, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of acceleration from rolling peak
def f11ac_f11_semi_acceleration_acceldd_252d_base_v149_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = a - _max(a, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of acceleration from rolling peak
def f11ac_f11_semi_acceleration_acceldd_504d_base_v150_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = a - _max(a, 504)
    return result.replace([np.inf, -np.inf], np.nan)
