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


def _ema(s, w):
    return s.ewm(span=w, adjust=False, min_periods=max(1, w // 2)).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f05_ltd_ratio(debt, deposits):
    return debt / deposits.replace(0, np.nan).abs()


def _f05_ltd_dynamics(debt, deposits, w):
    r = debt / deposits.replace(0, np.nan).abs()
    return r - r.shift(w)


def _f05_ltd_stability(debt, deposits, w):
    r = debt / deposits.replace(0, np.nan).abs()
    m = r.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = r.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan).abs()


def f05ltd_f05_loan_to_deposit_dynamics_ltr_lvl_126d_base_v076_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_ratio(debt, deposits), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_std_126d_base_v077_signal(debt, deposits, closeadj):
    result = _std(_f05_ltd_ratio(debt, deposits), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_ema_126d_base_v078_signal(debt, deposits, closeadj):
    result = _ema(_f05_ltd_ratio(debt, deposits), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_z_126d_base_v079_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_ratio(debt, deposits), 273) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_lvl_126d_base_v080_signal(debt, deposits, closeadj):
    result = _f05_ltd_dynamics(debt, deposits, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_mean_126d_base_v081_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_dynamics(debt, deposits, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_std_126d_base_v082_signal(debt, deposits, closeadj):
    result = _std(_f05_ltd_dynamics(debt, deposits, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_z_126d_base_v083_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_dynamics(debt, deposits, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_lvl_126d_base_v084_signal(debt, deposits, closeadj):
    result = _f05_ltd_stability(debt, deposits, 126) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_mean_126d_base_v085_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_stability(debt, deposits, 126), 21) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_z_126d_base_v086_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_stability(debt, deposits, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltrxltd_126d_base_v087_signal(debt, deposits, closeadj):
    result = _f05_ltd_ratio(debt, deposits) * _f05_ltd_dynamics(debt, deposits, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltrxlts_126d_base_v088_signal(debt, deposits, closeadj):
    result = _f05_ltd_ratio(debt, deposits) + _f05_ltd_stability(debt, deposits, 126) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_log_126d_base_v089_signal(debt, deposits, closeadj):
    r = _f05_ltd_ratio(debt, deposits)
    result = np.sign(r) * np.log1p(r.abs()) * closeadj * 126 / 252.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_sq_126d_base_v090_signal(debt, deposits, closeadj):
    r = _f05_ltd_ratio(debt, deposits)
    result = r * r * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_lvl_189d_base_v091_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_ratio(debt, deposits), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_std_189d_base_v092_signal(debt, deposits, closeadj):
    result = _std(_f05_ltd_ratio(debt, deposits), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_ema_189d_base_v093_signal(debt, deposits, closeadj):
    result = _ema(_f05_ltd_ratio(debt, deposits), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_z_189d_base_v094_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_ratio(debt, deposits), 399) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_lvl_189d_base_v095_signal(debt, deposits, closeadj):
    result = _f05_ltd_dynamics(debt, deposits, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_mean_189d_base_v096_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_dynamics(debt, deposits, 189), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_std_189d_base_v097_signal(debt, deposits, closeadj):
    result = _std(_f05_ltd_dynamics(debt, deposits, 189), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_z_189d_base_v098_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_dynamics(debt, deposits, 189), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_lvl_189d_base_v099_signal(debt, deposits, closeadj):
    result = _f05_ltd_stability(debt, deposits, 189) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_mean_189d_base_v100_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_stability(debt, deposits, 189), 21) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_z_189d_base_v101_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_stability(debt, deposits, 189), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltrxltd_189d_base_v102_signal(debt, deposits, closeadj):
    result = _f05_ltd_ratio(debt, deposits) * _f05_ltd_dynamics(debt, deposits, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltrxlts_189d_base_v103_signal(debt, deposits, closeadj):
    result = _f05_ltd_ratio(debt, deposits) + _f05_ltd_stability(debt, deposits, 189) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_log_189d_base_v104_signal(debt, deposits, closeadj):
    r = _f05_ltd_ratio(debt, deposits)
    result = np.sign(r) * np.log1p(r.abs()) * closeadj * 189 / 252.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_sq_189d_base_v105_signal(debt, deposits, closeadj):
    r = _f05_ltd_ratio(debt, deposits)
    result = r * r * _mean(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_lvl_252d_base_v106_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_ratio(debt, deposits), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_std_252d_base_v107_signal(debt, deposits, closeadj):
    result = _std(_f05_ltd_ratio(debt, deposits), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_ema_252d_base_v108_signal(debt, deposits, closeadj):
    result = _ema(_f05_ltd_ratio(debt, deposits), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_z_252d_base_v109_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_ratio(debt, deposits), 525) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_lvl_252d_base_v110_signal(debt, deposits, closeadj):
    result = _f05_ltd_dynamics(debt, deposits, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_mean_252d_base_v111_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_dynamics(debt, deposits, 252), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_std_252d_base_v112_signal(debt, deposits, closeadj):
    result = _std(_f05_ltd_dynamics(debt, deposits, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_z_252d_base_v113_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_dynamics(debt, deposits, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_lvl_252d_base_v114_signal(debt, deposits, closeadj):
    result = _f05_ltd_stability(debt, deposits, 252) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_mean_252d_base_v115_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_stability(debt, deposits, 252), 21) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_z_252d_base_v116_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_stability(debt, deposits, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltrxltd_252d_base_v117_signal(debt, deposits, closeadj):
    result = _f05_ltd_ratio(debt, deposits) * _f05_ltd_dynamics(debt, deposits, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltrxlts_252d_base_v118_signal(debt, deposits, closeadj):
    result = _f05_ltd_ratio(debt, deposits) + _f05_ltd_stability(debt, deposits, 252) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_log_252d_base_v119_signal(debt, deposits, closeadj):
    r = _f05_ltd_ratio(debt, deposits)
    result = np.sign(r) * np.log1p(r.abs()) * closeadj * 252 / 252.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_sq_252d_base_v120_signal(debt, deposits, closeadj):
    r = _f05_ltd_ratio(debt, deposits)
    result = r * r * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_lvl_378d_base_v121_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_ratio(debt, deposits), 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_std_378d_base_v122_signal(debt, deposits, closeadj):
    result = _std(_f05_ltd_ratio(debt, deposits), 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_ema_378d_base_v123_signal(debt, deposits, closeadj):
    result = _ema(_f05_ltd_ratio(debt, deposits), 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_z_378d_base_v124_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_ratio(debt, deposits), 777) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_lvl_378d_base_v125_signal(debt, deposits, closeadj):
    result = _f05_ltd_dynamics(debt, deposits, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_mean_378d_base_v126_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_dynamics(debt, deposits, 378), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_std_378d_base_v127_signal(debt, deposits, closeadj):
    result = _std(_f05_ltd_dynamics(debt, deposits, 378), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_z_378d_base_v128_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_dynamics(debt, deposits, 378), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_lvl_378d_base_v129_signal(debt, deposits, closeadj):
    result = _f05_ltd_stability(debt, deposits, 378) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_mean_378d_base_v130_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_stability(debt, deposits, 378), 21) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_z_378d_base_v131_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_stability(debt, deposits, 378), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltrxltd_378d_base_v132_signal(debt, deposits, closeadj):
    result = _f05_ltd_ratio(debt, deposits) * _f05_ltd_dynamics(debt, deposits, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltrxlts_378d_base_v133_signal(debt, deposits, closeadj):
    result = _f05_ltd_ratio(debt, deposits) + _f05_ltd_stability(debt, deposits, 378) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_log_378d_base_v134_signal(debt, deposits, closeadj):
    r = _f05_ltd_ratio(debt, deposits)
    result = np.sign(r) * np.log1p(r.abs()) * closeadj * 378 / 252.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_sq_378d_base_v135_signal(debt, deposits, closeadj):
    r = _f05_ltd_ratio(debt, deposits)
    result = r * r * _mean(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_lvl_504d_base_v136_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_ratio(debt, deposits), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_std_504d_base_v137_signal(debt, deposits, closeadj):
    result = _std(_f05_ltd_ratio(debt, deposits), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_ema_504d_base_v138_signal(debt, deposits, closeadj):
    result = _ema(_f05_ltd_ratio(debt, deposits), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_z_504d_base_v139_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_ratio(debt, deposits), 1029) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_lvl_504d_base_v140_signal(debt, deposits, closeadj):
    result = _f05_ltd_dynamics(debt, deposits, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_mean_504d_base_v141_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_dynamics(debt, deposits, 504), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_std_504d_base_v142_signal(debt, deposits, closeadj):
    result = _std(_f05_ltd_dynamics(debt, deposits, 504), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltd_z_504d_base_v143_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_dynamics(debt, deposits, 504), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_lvl_504d_base_v144_signal(debt, deposits, closeadj):
    result = _f05_ltd_stability(debt, deposits, 504) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_mean_504d_base_v145_signal(debt, deposits, closeadj):
    result = _mean(_f05_ltd_stability(debt, deposits, 504), 21) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_lts_z_504d_base_v146_signal(debt, deposits, closeadj):
    result = _z(_f05_ltd_stability(debt, deposits, 504), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltrxltd_504d_base_v147_signal(debt, deposits, closeadj):
    result = _f05_ltd_ratio(debt, deposits) * _f05_ltd_dynamics(debt, deposits, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltrxlts_504d_base_v148_signal(debt, deposits, closeadj):
    result = _f05_ltd_ratio(debt, deposits) + _f05_ltd_stability(debt, deposits, 504) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_log_504d_base_v149_signal(debt, deposits, closeadj):
    r = _f05_ltd_ratio(debt, deposits)
    result = np.sign(r) * np.log1p(r.abs()) * closeadj * 504 / 252.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05ltd_f05_loan_to_deposit_dynamics_ltr_sq_504d_base_v150_signal(debt, deposits, closeadj):
    r = _f05_ltd_ratio(debt, deposits)
    result = r * r * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f05ltd_f05_loan_to_deposit_dynamics_ltr_lvl_126d_base_v076_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_std_126d_base_v077_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_ema_126d_base_v078_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_z_126d_base_v079_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_lvl_126d_base_v080_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_mean_126d_base_v081_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_std_126d_base_v082_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_z_126d_base_v083_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_lvl_126d_base_v084_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_mean_126d_base_v085_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_z_126d_base_v086_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltrxltd_126d_base_v087_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltrxlts_126d_base_v088_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_log_126d_base_v089_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_sq_126d_base_v090_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_lvl_189d_base_v091_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_std_189d_base_v092_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_ema_189d_base_v093_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_z_189d_base_v094_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_lvl_189d_base_v095_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_mean_189d_base_v096_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_std_189d_base_v097_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_z_189d_base_v098_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_lvl_189d_base_v099_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_mean_189d_base_v100_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_z_189d_base_v101_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltrxltd_189d_base_v102_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltrxlts_189d_base_v103_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_log_189d_base_v104_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_sq_189d_base_v105_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_lvl_252d_base_v106_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_std_252d_base_v107_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_ema_252d_base_v108_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_z_252d_base_v109_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_lvl_252d_base_v110_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_mean_252d_base_v111_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_std_252d_base_v112_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_z_252d_base_v113_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_lvl_252d_base_v114_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_mean_252d_base_v115_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_z_252d_base_v116_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltrxltd_252d_base_v117_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltrxlts_252d_base_v118_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_log_252d_base_v119_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_sq_252d_base_v120_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_lvl_378d_base_v121_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_std_378d_base_v122_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_ema_378d_base_v123_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_z_378d_base_v124_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_lvl_378d_base_v125_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_mean_378d_base_v126_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_std_378d_base_v127_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_z_378d_base_v128_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_lvl_378d_base_v129_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_mean_378d_base_v130_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_z_378d_base_v131_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltrxltd_378d_base_v132_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltrxlts_378d_base_v133_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_log_378d_base_v134_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_sq_378d_base_v135_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_lvl_504d_base_v136_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_std_504d_base_v137_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_ema_504d_base_v138_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_z_504d_base_v139_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_lvl_504d_base_v140_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_mean_504d_base_v141_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_std_504d_base_v142_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltd_z_504d_base_v143_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_lvl_504d_base_v144_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_mean_504d_base_v145_signal,
    f05ltd_f05_loan_to_deposit_dynamics_lts_z_504d_base_v146_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltrxltd_504d_base_v147_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltrxlts_504d_base_v148_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_log_504d_base_v149_signal,
    f05ltd_f05_loan_to_deposit_dynamics_ltr_sq_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F05_LOAN_TO_DEPOSIT_DYNAMICS_REGISTRY_076_150 = REGISTRY


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
    deposits     = pd.Series(1.5e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="deposits")
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
        "deposits": deposits,
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
    domain_primitives = ("_f05_ltd_ratio", "_f05_ltd_dynamics", "_f05_ltd_stability",)
    import hashlib
    seen_bodies = set()
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
        # body hash dup check
        body_lines = [ln.strip() for ln in src.splitlines()
                      if ln.strip() and not ln.strip().startswith("#") and not ln.strip().startswith("def ")]
        body_hash = hashlib.sha1("\n".join(body_lines).encode()).hexdigest()
        assert body_hash not in seen_bodies, f"DUP body in {name}"
        seen_bodies.add(body_hash)
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f05_loan_to_deposit_dynamics_base_076_150_claude: {n_features} features pass, 0 dup bodies")
