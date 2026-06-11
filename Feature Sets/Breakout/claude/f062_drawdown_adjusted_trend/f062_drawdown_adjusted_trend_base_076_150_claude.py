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
def _f062_trend_slope(closeadj, w):
    return (closeadj - closeadj.shift(w)) / closeadj.shift(w).abs().replace(0, np.nan)


def _f062_max_drawdown(closeadj, w):
    peak = closeadj.rolling(w, min_periods=max(1, w // 2)).max()
    return (closeadj - peak) / peak.replace(0, np.nan).abs()


def _f062_clean_trend(closeadj, w):
    slope = (closeadj - closeadj.shift(w)) / closeadj.shift(w).abs().replace(0, np.nan)
    peak = closeadj.rolling(w, min_periods=max(1, w // 2)).max()
    dd = (closeadj - peak) / peak.replace(0, np.nan).abs()
    return slope / (1.0 + dd.abs())


# ===== features =====

def f062dat_f062_drawdown_adjusted_trend_rawb_42d_base_v076_signal(closeadj):
    base = _f062_trend_slope(closeadj, 42)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_rawb_63d_base_v077_signal(closeadj):
    base = _f062_max_drawdown(closeadj, 63)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_rawb_126d_base_v078_signal(closeadj):
    base = _f062_clean_trend(closeadj, 126)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_m21b_189d_base_v079_signal(closeadj):
    base = _f062_trend_slope(closeadj, 189)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_m21b_252d_base_v080_signal(closeadj):
    base = _f062_max_drawdown(closeadj, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_m21b_378d_base_v081_signal(closeadj):
    base = _f062_clean_trend(closeadj, 378)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_m63b_504d_base_v082_signal(closeadj):
    base = _f062_trend_slope(closeadj, 504)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_m63b_5d_base_v083_signal(closeadj):
    base = _f062_max_drawdown(closeadj, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_m63b_10d_base_v084_signal(closeadj):
    base = _f062_clean_trend(closeadj, 10)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_s21b_21d_base_v085_signal(closeadj):
    base = _f062_trend_slope(closeadj, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_s21b_42d_base_v086_signal(closeadj):
    base = _f062_max_drawdown(closeadj, 42)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_s21b_63d_base_v087_signal(closeadj):
    base = _f062_clean_trend(closeadj, 63)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_s63b_126d_base_v088_signal(closeadj):
    base = _f062_trend_slope(closeadj, 126)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_s63b_189d_base_v089_signal(closeadj):
    base = _f062_max_drawdown(closeadj, 189)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_s63b_252d_base_v090_signal(closeadj):
    base = _f062_clean_trend(closeadj, 252)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_z21b_378d_base_v091_signal(closeadj):
    base = _f062_trend_slope(closeadj, 378)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_z21b_504d_base_v092_signal(closeadj):
    base = _f062_max_drawdown(closeadj, 504)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_z21b_5d_base_v093_signal(closeadj):
    base = _f062_clean_trend(closeadj, 5)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_z63b_10d_base_v094_signal(closeadj):
    base = _f062_trend_slope(closeadj, 10)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_z63b_21d_base_v095_signal(closeadj):
    base = _f062_max_drawdown(closeadj, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_z63b_42d_base_v096_signal(closeadj):
    base = _f062_clean_trend(closeadj, 42)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_z252b_63d_base_v097_signal(closeadj):
    base = _f062_trend_slope(closeadj, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_z252b_126d_base_v098_signal(closeadj):
    base = _f062_max_drawdown(closeadj, 126)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_z252b_189d_base_v099_signal(closeadj):
    base = _f062_clean_trend(closeadj, 189)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_e21b_252d_base_v100_signal(closeadj):
    base = _f062_trend_slope(closeadj, 252)
    result = (base).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_e21b_378d_base_v101_signal(closeadj):
    base = _f062_max_drawdown(closeadj, 378)
    result = (base).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_e21b_504d_base_v102_signal(closeadj):
    base = _f062_clean_trend(closeadj, 504)
    result = (base).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_e63b_5d_base_v103_signal(closeadj):
    base = _f062_trend_slope(closeadj, 5)
    result = (base).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_e63b_10d_base_v104_signal(closeadj):
    base = _f062_max_drawdown(closeadj, 10)
    result = (base).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_e63b_21d_base_v105_signal(closeadj):
    base = _f062_clean_trend(closeadj, 21)
    result = (base).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_e126b_42d_base_v106_signal(closeadj):
    base = _f062_trend_slope(closeadj, 42)
    result = (base).ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_e126b_63d_base_v107_signal(closeadj):
    base = _f062_max_drawdown(closeadj, 63)
    result = (base).ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_e126b_126d_base_v108_signal(closeadj):
    base = _f062_clean_trend(closeadj, 126)
    result = (base).ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_cumb_189d_base_v109_signal(closeadj):
    base = _f062_trend_slope(closeadj, 189)
    result = (base).fillna(0).cumsum() / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_cumb_252d_base_v110_signal(closeadj):
    base = _f062_max_drawdown(closeadj, 252)
    result = (base).fillna(0).cumsum() / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_cumb_378d_base_v111_signal(closeadj):
    base = _f062_clean_trend(closeadj, 378)
    result = (base).fillna(0).cumsum() / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_logb_504d_base_v112_signal(closeadj):
    base = _f062_trend_slope(closeadj, 504)
    result = np.log1p((base).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_logb_5d_base_v113_signal(closeadj):
    base = _f062_max_drawdown(closeadj, 5)
    result = np.log1p((base).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_logb_10d_base_v114_signal(closeadj):
    base = _f062_clean_trend(closeadj, 10)
    result = np.log1p((base).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_sgnb_21d_base_v115_signal(closeadj):
    base = _f062_trend_slope(closeadj, 21)
    result = np.sign(base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_sgnb_42d_base_v116_signal(closeadj):
    base = _f062_max_drawdown(closeadj, 42)
    result = np.sign(base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_sgnb_63d_base_v117_signal(closeadj):
    base = _f062_clean_trend(closeadj, 63)
    result = np.sign(base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_r63b_126d_base_v118_signal(closeadj):
    base = _f062_trend_slope(closeadj, 126)
    result = (base).rolling(63, min_periods=21).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_r63b_189d_base_v119_signal(closeadj):
    base = _f062_max_drawdown(closeadj, 189)
    result = (base).rolling(63, min_periods=21).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_r63b_252d_base_v120_signal(closeadj):
    base = _f062_clean_trend(closeadj, 252)
    result = (base).rolling(63, min_periods=21).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_r252b_378d_base_v121_signal(closeadj):
    base = _f062_trend_slope(closeadj, 378)
    result = (base).rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_r252b_504d_base_v122_signal(closeadj):
    base = _f062_max_drawdown(closeadj, 504)
    result = (base).rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_r252b_5d_base_v123_signal(closeadj):
    base = _f062_clean_trend(closeadj, 5)
    result = (base).rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_mcb_10d_base_v124_signal(closeadj):
    base = _f062_trend_slope(closeadj, 10)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_mcb_21d_base_v125_signal(closeadj):
    base = _f062_max_drawdown(closeadj, 21)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_mcb_42d_base_v126_signal(closeadj):
    base = _f062_clean_trend(closeadj, 42)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_dcb_63d_base_v127_signal(closeadj):
    base = _f062_trend_slope(closeadj, 63)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_dcb_126d_base_v128_signal(closeadj):
    base = _f062_max_drawdown(closeadj, 126)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_dcb_189d_base_v129_signal(closeadj):
    base = _f062_clean_trend(closeadj, 189)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_pc5b_252d_base_v130_signal(closeadj):
    base = _f062_trend_slope(closeadj, 252)
    result = (base).pct_change(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_pc5b_378d_base_v131_signal(closeadj):
    base = _f062_max_drawdown(closeadj, 378)
    result = (base).pct_change(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_pc5b_504d_base_v132_signal(closeadj):
    base = _f062_clean_trend(closeadj, 504)
    result = (base).pct_change(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_pc21b_5d_base_v133_signal(closeadj):
    base = _f062_trend_slope(closeadj, 5)
    result = (base).pct_change(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_pc21b_10d_base_v134_signal(closeadj):
    base = _f062_max_drawdown(closeadj, 10)
    result = (base).pct_change(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_pc21b_21d_base_v135_signal(closeadj):
    base = _f062_clean_trend(closeadj, 21)
    result = (base).pct_change(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_d21b_42d_base_v136_signal(closeadj):
    base = _f062_trend_slope(closeadj, 42)
    result = (base).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_d21b_63d_base_v137_signal(closeadj):
    base = _f062_max_drawdown(closeadj, 63)
    result = (base).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_d21b_126d_base_v138_signal(closeadj):
    base = _f062_clean_trend(closeadj, 126)
    result = (base).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_sqb_189d_base_v139_signal(closeadj):
    base = _f062_trend_slope(closeadj, 189)
    result = (base) * (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_sqb_252d_base_v140_signal(closeadj):
    base = _f062_max_drawdown(closeadj, 252)
    result = (base) * (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_sqb_378d_base_v141_signal(closeadj):
    base = _f062_clean_trend(closeadj, 378)
    result = (base) * (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_cbb_504d_base_v142_signal(closeadj):
    base = _f062_trend_slope(closeadj, 504)
    result = (base) ** 3 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_cbb_5d_base_v143_signal(closeadj):
    base = _f062_max_drawdown(closeadj, 5)
    result = (base) ** 3 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_cbb_10d_base_v144_signal(closeadj):
    base = _f062_clean_trend(closeadj, 10)
    result = (base) ** 3 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_sqrb_21d_base_v145_signal(closeadj):
    base = _f062_trend_slope(closeadj, 21)
    result = np.sqrt((base).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_sqrb_42d_base_v146_signal(closeadj):
    base = _f062_max_drawdown(closeadj, 42)
    result = np.sqrt((base).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_sqrb_63d_base_v147_signal(closeadj):
    base = _f062_clean_trend(closeadj, 63)
    result = np.sqrt((base).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_m126b_126d_base_v148_signal(closeadj):
    base = _f062_trend_slope(closeadj, 126)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_m126b_189d_base_v149_signal(closeadj):
    base = _f062_max_drawdown(closeadj, 189)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f062dat_f062_drawdown_adjusted_trend_m126b_252d_base_v150_signal(closeadj):
    base = _f062_clean_trend(closeadj, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f062dat_f062_drawdown_adjusted_trend_rawb_42d_base_v076_signal,
    f062dat_f062_drawdown_adjusted_trend_rawb_63d_base_v077_signal,
    f062dat_f062_drawdown_adjusted_trend_rawb_126d_base_v078_signal,
    f062dat_f062_drawdown_adjusted_trend_m21b_189d_base_v079_signal,
    f062dat_f062_drawdown_adjusted_trend_m21b_252d_base_v080_signal,
    f062dat_f062_drawdown_adjusted_trend_m21b_378d_base_v081_signal,
    f062dat_f062_drawdown_adjusted_trend_m63b_504d_base_v082_signal,
    f062dat_f062_drawdown_adjusted_trend_m63b_5d_base_v083_signal,
    f062dat_f062_drawdown_adjusted_trend_m63b_10d_base_v084_signal,
    f062dat_f062_drawdown_adjusted_trend_s21b_21d_base_v085_signal,
    f062dat_f062_drawdown_adjusted_trend_s21b_42d_base_v086_signal,
    f062dat_f062_drawdown_adjusted_trend_s21b_63d_base_v087_signal,
    f062dat_f062_drawdown_adjusted_trend_s63b_126d_base_v088_signal,
    f062dat_f062_drawdown_adjusted_trend_s63b_189d_base_v089_signal,
    f062dat_f062_drawdown_adjusted_trend_s63b_252d_base_v090_signal,
    f062dat_f062_drawdown_adjusted_trend_z21b_378d_base_v091_signal,
    f062dat_f062_drawdown_adjusted_trend_z21b_504d_base_v092_signal,
    f062dat_f062_drawdown_adjusted_trend_z21b_5d_base_v093_signal,
    f062dat_f062_drawdown_adjusted_trend_z63b_10d_base_v094_signal,
    f062dat_f062_drawdown_adjusted_trend_z63b_21d_base_v095_signal,
    f062dat_f062_drawdown_adjusted_trend_z63b_42d_base_v096_signal,
    f062dat_f062_drawdown_adjusted_trend_z252b_63d_base_v097_signal,
    f062dat_f062_drawdown_adjusted_trend_z252b_126d_base_v098_signal,
    f062dat_f062_drawdown_adjusted_trend_z252b_189d_base_v099_signal,
    f062dat_f062_drawdown_adjusted_trend_e21b_252d_base_v100_signal,
    f062dat_f062_drawdown_adjusted_trend_e21b_378d_base_v101_signal,
    f062dat_f062_drawdown_adjusted_trend_e21b_504d_base_v102_signal,
    f062dat_f062_drawdown_adjusted_trend_e63b_5d_base_v103_signal,
    f062dat_f062_drawdown_adjusted_trend_e63b_10d_base_v104_signal,
    f062dat_f062_drawdown_adjusted_trend_e63b_21d_base_v105_signal,
    f062dat_f062_drawdown_adjusted_trend_e126b_42d_base_v106_signal,
    f062dat_f062_drawdown_adjusted_trend_e126b_63d_base_v107_signal,
    f062dat_f062_drawdown_adjusted_trend_e126b_126d_base_v108_signal,
    f062dat_f062_drawdown_adjusted_trend_cumb_189d_base_v109_signal,
    f062dat_f062_drawdown_adjusted_trend_cumb_252d_base_v110_signal,
    f062dat_f062_drawdown_adjusted_trend_cumb_378d_base_v111_signal,
    f062dat_f062_drawdown_adjusted_trend_logb_504d_base_v112_signal,
    f062dat_f062_drawdown_adjusted_trend_logb_5d_base_v113_signal,
    f062dat_f062_drawdown_adjusted_trend_logb_10d_base_v114_signal,
    f062dat_f062_drawdown_adjusted_trend_sgnb_21d_base_v115_signal,
    f062dat_f062_drawdown_adjusted_trend_sgnb_42d_base_v116_signal,
    f062dat_f062_drawdown_adjusted_trend_sgnb_63d_base_v117_signal,
    f062dat_f062_drawdown_adjusted_trend_r63b_126d_base_v118_signal,
    f062dat_f062_drawdown_adjusted_trend_r63b_189d_base_v119_signal,
    f062dat_f062_drawdown_adjusted_trend_r63b_252d_base_v120_signal,
    f062dat_f062_drawdown_adjusted_trend_r252b_378d_base_v121_signal,
    f062dat_f062_drawdown_adjusted_trend_r252b_504d_base_v122_signal,
    f062dat_f062_drawdown_adjusted_trend_r252b_5d_base_v123_signal,
    f062dat_f062_drawdown_adjusted_trend_mcb_10d_base_v124_signal,
    f062dat_f062_drawdown_adjusted_trend_mcb_21d_base_v125_signal,
    f062dat_f062_drawdown_adjusted_trend_mcb_42d_base_v126_signal,
    f062dat_f062_drawdown_adjusted_trend_dcb_63d_base_v127_signal,
    f062dat_f062_drawdown_adjusted_trend_dcb_126d_base_v128_signal,
    f062dat_f062_drawdown_adjusted_trend_dcb_189d_base_v129_signal,
    f062dat_f062_drawdown_adjusted_trend_pc5b_252d_base_v130_signal,
    f062dat_f062_drawdown_adjusted_trend_pc5b_378d_base_v131_signal,
    f062dat_f062_drawdown_adjusted_trend_pc5b_504d_base_v132_signal,
    f062dat_f062_drawdown_adjusted_trend_pc21b_5d_base_v133_signal,
    f062dat_f062_drawdown_adjusted_trend_pc21b_10d_base_v134_signal,
    f062dat_f062_drawdown_adjusted_trend_pc21b_21d_base_v135_signal,
    f062dat_f062_drawdown_adjusted_trend_d21b_42d_base_v136_signal,
    f062dat_f062_drawdown_adjusted_trend_d21b_63d_base_v137_signal,
    f062dat_f062_drawdown_adjusted_trend_d21b_126d_base_v138_signal,
    f062dat_f062_drawdown_adjusted_trend_sqb_189d_base_v139_signal,
    f062dat_f062_drawdown_adjusted_trend_sqb_252d_base_v140_signal,
    f062dat_f062_drawdown_adjusted_trend_sqb_378d_base_v141_signal,
    f062dat_f062_drawdown_adjusted_trend_cbb_504d_base_v142_signal,
    f062dat_f062_drawdown_adjusted_trend_cbb_5d_base_v143_signal,
    f062dat_f062_drawdown_adjusted_trend_cbb_10d_base_v144_signal,
    f062dat_f062_drawdown_adjusted_trend_sqrb_21d_base_v145_signal,
    f062dat_f062_drawdown_adjusted_trend_sqrb_42d_base_v146_signal,
    f062dat_f062_drawdown_adjusted_trend_sqrb_63d_base_v147_signal,
    f062dat_f062_drawdown_adjusted_trend_m126b_126d_base_v148_signal,
    f062dat_f062_drawdown_adjusted_trend_m126b_189d_base_v149_signal,
    f062dat_f062_drawdown_adjusted_trend_m126b_252d_base_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F062_DRAWDOWN_ADJUSTED_TREND_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f062_trend_slope", "_f062_max_drawdown", "_f062_clean_trend")
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
    print(f"OK f062_drawdown_adjusted_trend_076_150_claude: {n_features} features pass")
