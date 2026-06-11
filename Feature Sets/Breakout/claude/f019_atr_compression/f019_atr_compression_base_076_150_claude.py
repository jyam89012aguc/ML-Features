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

def _f019_atr(high, low, closeadj, w):
    prev_c = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(),
                    (high - prev_c).abs(),
                    (low - prev_c).abs()], axis=1).max(axis=1)
    return tr.rolling(w, min_periods=max(1, w // 2)).mean()


def _f019_atr_compression(high, low, closeadj, w):
    atr_s = _f019_atr(high, low, closeadj, w)
    atr_l = _f019_atr(high, low, closeadj, w * 4)
    return atr_s / atr_l.replace(0, np.nan)


def _f019_squeeze_score(high, low, closeadj, w):
    atr = _f019_atr(high, low, closeadj, w)
    atr_norm = atr / closeadj.replace(0, np.nan).abs()
    z = _z(atr_norm, w * 2)
    return -z



# ===== features =====
def f019atc_f019_atr_compression_p1_sma126_closesma21_63d_base_v076_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 63)
    result = (_mean(base, 126)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_raw_closesq_378d_base_v077_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 378)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_diff63_closesq_42d_base_v078_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 42)
    result = ((base).diff(63)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_raw_closesma21_252d_base_v079_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 252)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_raw_closesq_252d_base_v080_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 252)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_diff5_closesma21_504d_base_v081_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 504)
    result = ((base).diff(5)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_sma63_close_189d_base_v082_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 189)
    result = (_mean(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_diff63_close_10d_base_v083_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 10)
    result = ((base).diff(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_raw_closesma21_126d_base_v084_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 126)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_sma21_close_63d_base_v085_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 63)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_diff21_closesq_126d_base_v086_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 126)
    result = ((base).diff(21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_std126_close_504d_base_v087_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 504)
    result = (_std(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_std126_closesq_378d_base_v088_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 378)
    result = (_std(base, 126)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_sma63_closesma63_63d_base_v089_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 63)
    result = (_mean(base, 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_z63_close_378d_base_v090_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 378)
    result = (_z(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_sma63_closesq_189d_base_v091_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 189)
    result = (_mean(base, 63)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_std126_closesq_10d_base_v092_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 10)
    result = (_std(base, 126)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_std126_closesma63_21d_base_v093_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 21)
    result = (_std(base, 126)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_sma126_closesq_378d_base_v094_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 378)
    result = (_mean(base, 126)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_diff63_closesma21_21d_base_v095_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 21)
    result = ((base).diff(63)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_z252_close_21d_base_v096_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 21)
    result = (_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_z21_closesma21_252d_base_v097_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 252)
    result = (_z(base, 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_std63_closesma21_5d_base_v098_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 5)
    result = (_std(base, 63)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_diff63_closesq_189d_base_v099_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 189)
    result = ((base).diff(63)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_raw_closesma63_504d_base_v100_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 504)
    result = (base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_std126_close_378d_base_v101_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 378)
    result = (_std(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_z63_closesq_252d_base_v102_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 252)
    result = (_z(base, 63)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_std126_closesma21_5d_base_v103_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 5)
    result = (_std(base, 126)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_sma21_closesma63_42d_base_v104_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 42)
    result = (_mean(base, 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_sma63_closesma21_63d_base_v105_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 63)
    result = (_mean(base, 63)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_sma21_closesq_189d_base_v106_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 189)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_z63_closesma21_189d_base_v107_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 189)
    result = (_z(base, 63)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_sma21_closesq_42d_base_v108_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 42)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_diff63_closesma21_189d_base_v109_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 189)
    result = ((base).diff(63)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_z21_closesma63_10d_base_v110_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 10)
    result = (_z(base, 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_z252_closesma21_21d_base_v111_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 21)
    result = (_z(base, 252)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_diff63_closesq_63d_base_v112_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 63)
    result = ((base).diff(63)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_z126_closesma63_10d_base_v113_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 10)
    result = (_z(base, 126)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_diff21_close_63d_base_v114_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 63)
    result = ((base).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_raw_close_189d_base_v115_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 189)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_sma63_close_5d_base_v116_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 5)
    result = (_mean(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_z126_closesq_42d_base_v117_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 42)
    result = (_z(base, 126)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_z63_closesq_42d_base_v118_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 42)
    result = (_z(base, 63)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_z252_close_21d_base_v119_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 21)
    result = (_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_std21_closesma21_5d_base_v120_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 5)
    result = (_std(base, 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_diff5_closesq_10d_base_v121_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 10)
    result = ((base).diff(5)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_z252_closesma63_189d_base_v122_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 189)
    result = (_z(base, 252)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_sma21_closesq_42d_base_v123_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 42)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_raw_close_42d_base_v124_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 42)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_z126_closesma21_378d_base_v125_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 378)
    result = (_z(base, 126)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_sma63_closesq_5d_base_v126_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 5)
    result = (_mean(base, 63)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_z63_close_504d_base_v127_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 504)
    result = (_z(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_sma63_closesma63_21d_base_v128_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 21)
    result = (_mean(base, 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_sma126_closesma63_5d_base_v129_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 5)
    result = (_mean(base, 126)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_std21_closesq_10d_base_v130_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 10)
    result = (_std(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_diff5_close_189d_base_v131_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 189)
    result = ((base).diff(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_std63_close_5d_base_v132_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 5)
    result = (_std(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_sma63_closesma21_5d_base_v133_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 5)
    result = (_mean(base, 63)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_z63_closesma21_42d_base_v134_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 42)
    result = (_z(base, 63)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_diff5_closesq_252d_base_v135_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 252)
    result = ((base).diff(5)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_sma126_close_21d_base_v136_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 21)
    result = (_mean(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_diff5_closesq_63d_base_v137_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 63)
    result = ((base).diff(5)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_diff21_close_252d_base_v138_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 252)
    result = ((base).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_z63_close_5d_base_v139_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 5)
    result = (_z(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_diff21_close_5d_base_v140_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 5)
    result = ((base).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_diff63_closesma63_10d_base_v141_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 10)
    result = ((base).diff(63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_diff21_closesq_504d_base_v142_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 504)
    result = ((base).diff(21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_z21_closesq_189d_base_v143_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 189)
    result = (_z(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_raw_closesma21_5d_base_v144_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 5)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_sma21_close_126d_base_v145_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 126)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_sma21_closesma63_378d_base_v146_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 378)
    result = (_mean(base, 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_z126_closesq_42d_base_v147_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 42)
    result = (_z(base, 126)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_sma63_closesq_252d_base_v148_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 252)
    result = (_mean(base, 63)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_sma126_closesma63_42d_base_v149_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 42)
    result = (_mean(base, 126)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_sma126_closesma63_504d_base_v150_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 504)
    result = (_mean(base, 126)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f019atc_f019_atr_compression_p1_sma126_closesma21_63d_base_v076_signal,
    f019atc_f019_atr_compression_p2_raw_closesq_378d_base_v077_signal,
    f019atc_f019_atr_compression_p3_diff63_closesq_42d_base_v078_signal,
    f019atc_f019_atr_compression_p3_raw_closesma21_252d_base_v079_signal,
    f019atc_f019_atr_compression_p2_raw_closesq_252d_base_v080_signal,
    f019atc_f019_atr_compression_p1_diff5_closesma21_504d_base_v081_signal,
    f019atc_f019_atr_compression_p2_sma63_close_189d_base_v082_signal,
    f019atc_f019_atr_compression_p1_diff63_close_10d_base_v083_signal,
    f019atc_f019_atr_compression_p3_raw_closesma21_126d_base_v084_signal,
    f019atc_f019_atr_compression_p1_sma21_close_63d_base_v085_signal,
    f019atc_f019_atr_compression_p1_diff21_closesq_126d_base_v086_signal,
    f019atc_f019_atr_compression_p1_std126_close_504d_base_v087_signal,
    f019atc_f019_atr_compression_p1_std126_closesq_378d_base_v088_signal,
    f019atc_f019_atr_compression_p2_sma63_closesma63_63d_base_v089_signal,
    f019atc_f019_atr_compression_p2_z63_close_378d_base_v090_signal,
    f019atc_f019_atr_compression_p3_sma63_closesq_189d_base_v091_signal,
    f019atc_f019_atr_compression_p3_std126_closesq_10d_base_v092_signal,
    f019atc_f019_atr_compression_p2_std126_closesma63_21d_base_v093_signal,
    f019atc_f019_atr_compression_p3_sma126_closesq_378d_base_v094_signal,
    f019atc_f019_atr_compression_p3_diff63_closesma21_21d_base_v095_signal,
    f019atc_f019_atr_compression_p2_z252_close_21d_base_v096_signal,
    f019atc_f019_atr_compression_p3_z21_closesma21_252d_base_v097_signal,
    f019atc_f019_atr_compression_p2_std63_closesma21_5d_base_v098_signal,
    f019atc_f019_atr_compression_p1_diff63_closesq_189d_base_v099_signal,
    f019atc_f019_atr_compression_p3_raw_closesma63_504d_base_v100_signal,
    f019atc_f019_atr_compression_p2_std126_close_378d_base_v101_signal,
    f019atc_f019_atr_compression_p2_z63_closesq_252d_base_v102_signal,
    f019atc_f019_atr_compression_p2_std126_closesma21_5d_base_v103_signal,
    f019atc_f019_atr_compression_p1_sma21_closesma63_42d_base_v104_signal,
    f019atc_f019_atr_compression_p2_sma63_closesma21_63d_base_v105_signal,
    f019atc_f019_atr_compression_p2_sma21_closesq_189d_base_v106_signal,
    f019atc_f019_atr_compression_p1_z63_closesma21_189d_base_v107_signal,
    f019atc_f019_atr_compression_p1_sma21_closesq_42d_base_v108_signal,
    f019atc_f019_atr_compression_p2_diff63_closesma21_189d_base_v109_signal,
    f019atc_f019_atr_compression_p2_z21_closesma63_10d_base_v110_signal,
    f019atc_f019_atr_compression_p1_z252_closesma21_21d_base_v111_signal,
    f019atc_f019_atr_compression_p1_diff63_closesq_63d_base_v112_signal,
    f019atc_f019_atr_compression_p1_z126_closesma63_10d_base_v113_signal,
    f019atc_f019_atr_compression_p2_diff21_close_63d_base_v114_signal,
    f019atc_f019_atr_compression_p2_raw_close_189d_base_v115_signal,
    f019atc_f019_atr_compression_p3_sma63_close_5d_base_v116_signal,
    f019atc_f019_atr_compression_p3_z126_closesq_42d_base_v117_signal,
    f019atc_f019_atr_compression_p2_z63_closesq_42d_base_v118_signal,
    f019atc_f019_atr_compression_p1_z252_close_21d_base_v119_signal,
    f019atc_f019_atr_compression_p2_std21_closesma21_5d_base_v120_signal,
    f019atc_f019_atr_compression_p1_diff5_closesq_10d_base_v121_signal,
    f019atc_f019_atr_compression_p1_z252_closesma63_189d_base_v122_signal,
    f019atc_f019_atr_compression_p2_sma21_closesq_42d_base_v123_signal,
    f019atc_f019_atr_compression_p3_raw_close_42d_base_v124_signal,
    f019atc_f019_atr_compression_p3_z126_closesma21_378d_base_v125_signal,
    f019atc_f019_atr_compression_p2_sma63_closesq_5d_base_v126_signal,
    f019atc_f019_atr_compression_p1_z63_close_504d_base_v127_signal,
    f019atc_f019_atr_compression_p2_sma63_closesma63_21d_base_v128_signal,
    f019atc_f019_atr_compression_p3_sma126_closesma63_5d_base_v129_signal,
    f019atc_f019_atr_compression_p3_std21_closesq_10d_base_v130_signal,
    f019atc_f019_atr_compression_p3_diff5_close_189d_base_v131_signal,
    f019atc_f019_atr_compression_p3_std63_close_5d_base_v132_signal,
    f019atc_f019_atr_compression_p3_sma63_closesma21_5d_base_v133_signal,
    f019atc_f019_atr_compression_p1_z63_closesma21_42d_base_v134_signal,
    f019atc_f019_atr_compression_p3_diff5_closesq_252d_base_v135_signal,
    f019atc_f019_atr_compression_p1_sma126_close_21d_base_v136_signal,
    f019atc_f019_atr_compression_p2_diff5_closesq_63d_base_v137_signal,
    f019atc_f019_atr_compression_p3_diff21_close_252d_base_v138_signal,
    f019atc_f019_atr_compression_p2_z63_close_5d_base_v139_signal,
    f019atc_f019_atr_compression_p2_diff21_close_5d_base_v140_signal,
    f019atc_f019_atr_compression_p2_diff63_closesma63_10d_base_v141_signal,
    f019atc_f019_atr_compression_p1_diff21_closesq_504d_base_v142_signal,
    f019atc_f019_atr_compression_p1_z21_closesq_189d_base_v143_signal,
    f019atc_f019_atr_compression_p2_raw_closesma21_5d_base_v144_signal,
    f019atc_f019_atr_compression_p3_sma21_close_126d_base_v145_signal,
    f019atc_f019_atr_compression_p2_sma21_closesma63_378d_base_v146_signal,
    f019atc_f019_atr_compression_p1_z126_closesq_42d_base_v147_signal,
    f019atc_f019_atr_compression_p2_sma63_closesq_252d_base_v148_signal,
    f019atc_f019_atr_compression_p2_sma126_closesma63_42d_base_v149_signal,
    f019atc_f019_atr_compression_p3_sma126_closesma63_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F019_ATR_COMPRESSION_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high.values, name="high")
    low = pd.Series(low.values, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f019_atr', '_f019_atr_compression', '_f019_squeeze_score')
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
    print(f"OK f019_atr_compression_base_076_150_claude: {n_features} features pass")
