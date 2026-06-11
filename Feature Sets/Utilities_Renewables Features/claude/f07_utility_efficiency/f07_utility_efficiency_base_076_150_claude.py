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
def _f07_opex_intensity(opex, revenue):
    return opex / revenue.replace(0, np.nan)


def _f07_efficiency_trend(opex, revenue, w):
    oi = opex / revenue.replace(0, np.nan)
    return -oi.rolling(w, min_periods=max(1, w // 2)).mean()


def _f07_efficiency_score(opex, sgna, revenue, w):
    oi = opex / revenue.replace(0, np.nan)
    si = sgna / revenue.replace(0, np.nan)
    combined = (oi + si) * 0.5
    return -combined.rolling(w, min_periods=max(1, w // 2)).mean()


def f07uef_f07_utility_efficiency_opexint_median_5d_base_v076_signal(opex, revenue, closeadj):
    result = (_f07_opex_intensity(opex, revenue)).rolling(5, min_periods=max(1, 5//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_median_21d_base_v077_signal(opex, revenue, closeadj):
    result = (_f07_opex_intensity(opex, revenue)).rolling(21, min_periods=max(1, 21//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_median_63d_base_v078_signal(opex, revenue, closeadj):
    result = (_f07_opex_intensity(opex, revenue)).rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_median_126d_base_v079_signal(opex, revenue, closeadj):
    result = (_f07_opex_intensity(opex, revenue)).rolling(126, min_periods=max(1, 126//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_median_252d_base_v080_signal(opex, revenue, closeadj):
    result = (_f07_opex_intensity(opex, revenue)).rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_rank_5d_base_v081_signal(opex, revenue, closeadj):
    result = (_f07_opex_intensity(opex, revenue)).rolling(5, min_periods=max(1, 5//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_rank_21d_base_v082_signal(opex, revenue, closeadj):
    result = (_f07_opex_intensity(opex, revenue)).rolling(21, min_periods=max(1, 21//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_rank_63d_base_v083_signal(opex, revenue, closeadj):
    result = (_f07_opex_intensity(opex, revenue)).rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_rank_126d_base_v084_signal(opex, revenue, closeadj):
    result = (_f07_opex_intensity(opex, revenue)).rolling(126, min_periods=max(1, 126//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_rank_252d_base_v085_signal(opex, revenue, closeadj):
    result = (_f07_opex_intensity(opex, revenue)).rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_diff_5d_base_v086_signal(opex, revenue, closeadj):
    _b = _f07_opex_intensity(opex, revenue)
    result = (_b - _b.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_diff_21d_base_v087_signal(opex, revenue, closeadj):
    _b = _f07_opex_intensity(opex, revenue)
    result = (_b - _b.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_diff_63d_base_v088_signal(opex, revenue, closeadj):
    _b = _f07_opex_intensity(opex, revenue)
    result = (_b - _b.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_diff_126d_base_v089_signal(opex, revenue, closeadj):
    _b = _f07_opex_intensity(opex, revenue)
    result = (_b - _b.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_diff_252d_base_v090_signal(opex, revenue, closeadj):
    _b = _f07_opex_intensity(opex, revenue)
    result = (_b - _b.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_logc_5d_base_v091_signal(opex, revenue, closeadj):
    result = _mean(_f07_opex_intensity(opex, revenue), 5) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_logc_21d_base_v092_signal(opex, revenue, closeadj):
    result = _mean(_f07_opex_intensity(opex, revenue), 21) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_logc_63d_base_v093_signal(opex, revenue, closeadj):
    result = _mean(_f07_opex_intensity(opex, revenue), 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_logc_126d_base_v094_signal(opex, revenue, closeadj):
    result = _mean(_f07_opex_intensity(opex, revenue), 126) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_logc_252d_base_v095_signal(opex, revenue, closeadj):
    result = _mean(_f07_opex_intensity(opex, revenue), 252) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_tanhsig_5d_base_v096_signal(opex, revenue, closeadj):
    _b = _f07_opex_intensity(opex, revenue)
    result = np.tanh(_mean(_b, 5)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_tanhsig_21d_base_v097_signal(opex, revenue, closeadj):
    _b = _f07_opex_intensity(opex, revenue)
    result = np.tanh(_mean(_b, 21)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_tanhsig_63d_base_v098_signal(opex, revenue, closeadj):
    _b = _f07_opex_intensity(opex, revenue)
    result = np.tanh(_mean(_b, 63)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_tanhsig_126d_base_v099_signal(opex, revenue, closeadj):
    _b = _f07_opex_intensity(opex, revenue)
    result = np.tanh(_mean(_b, 126)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_tanhsig_252d_base_v100_signal(opex, revenue, closeadj):
    _b = _f07_opex_intensity(opex, revenue)
    result = np.tanh(_mean(_b, 252)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_median_5d_base_v101_signal(opex, revenue, closeadj):
    result = (_f07_efficiency_trend(opex, revenue, 5)).rolling(5, min_periods=max(1, 5//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_median_21d_base_v102_signal(opex, revenue, closeadj):
    result = (_f07_efficiency_trend(opex, revenue, 21)).rolling(21, min_periods=max(1, 21//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_median_63d_base_v103_signal(opex, revenue, closeadj):
    result = (_f07_efficiency_trend(opex, revenue, 63)).rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_median_126d_base_v104_signal(opex, revenue, closeadj):
    result = (_f07_efficiency_trend(opex, revenue, 126)).rolling(126, min_periods=max(1, 126//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_median_252d_base_v105_signal(opex, revenue, closeadj):
    result = (_f07_efficiency_trend(opex, revenue, 252)).rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_rank_5d_base_v106_signal(opex, revenue, closeadj):
    result = (_f07_efficiency_trend(opex, revenue, 5)).rolling(5, min_periods=max(1, 5//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_rank_21d_base_v107_signal(opex, revenue, closeadj):
    result = (_f07_efficiency_trend(opex, revenue, 21)).rolling(21, min_periods=max(1, 21//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_rank_63d_base_v108_signal(opex, revenue, closeadj):
    result = (_f07_efficiency_trend(opex, revenue, 63)).rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_rank_126d_base_v109_signal(opex, revenue, closeadj):
    result = (_f07_efficiency_trend(opex, revenue, 126)).rolling(126, min_periods=max(1, 126//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_rank_252d_base_v110_signal(opex, revenue, closeadj):
    result = (_f07_efficiency_trend(opex, revenue, 252)).rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_diff_5d_base_v111_signal(opex, revenue, closeadj):
    _b = _f07_efficiency_trend(opex, revenue, 5)
    result = (_b - _b.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_diff_21d_base_v112_signal(opex, revenue, closeadj):
    _b = _f07_efficiency_trend(opex, revenue, 21)
    result = (_b - _b.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_diff_63d_base_v113_signal(opex, revenue, closeadj):
    _b = _f07_efficiency_trend(opex, revenue, 63)
    result = (_b - _b.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_diff_126d_base_v114_signal(opex, revenue, closeadj):
    _b = _f07_efficiency_trend(opex, revenue, 126)
    result = (_b - _b.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_diff_252d_base_v115_signal(opex, revenue, closeadj):
    _b = _f07_efficiency_trend(opex, revenue, 252)
    result = (_b - _b.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_logc_5d_base_v116_signal(opex, revenue, closeadj):
    result = _mean(_f07_efficiency_trend(opex, revenue, 5), 5) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_logc_21d_base_v117_signal(opex, revenue, closeadj):
    result = _mean(_f07_efficiency_trend(opex, revenue, 21), 21) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_logc_63d_base_v118_signal(opex, revenue, closeadj):
    result = _mean(_f07_efficiency_trend(opex, revenue, 63), 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_logc_126d_base_v119_signal(opex, revenue, closeadj):
    result = _mean(_f07_efficiency_trend(opex, revenue, 126), 126) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_logc_252d_base_v120_signal(opex, revenue, closeadj):
    result = _mean(_f07_efficiency_trend(opex, revenue, 252), 252) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_tanhsig_5d_base_v121_signal(opex, revenue, closeadj):
    _b = _f07_efficiency_trend(opex, revenue, 5)
    result = np.tanh(_mean(_b, 5)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_tanhsig_21d_base_v122_signal(opex, revenue, closeadj):
    _b = _f07_efficiency_trend(opex, revenue, 21)
    result = np.tanh(_mean(_b, 21)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_tanhsig_63d_base_v123_signal(opex, revenue, closeadj):
    _b = _f07_efficiency_trend(opex, revenue, 63)
    result = np.tanh(_mean(_b, 63)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_tanhsig_126d_base_v124_signal(opex, revenue, closeadj):
    _b = _f07_efficiency_trend(opex, revenue, 126)
    result = np.tanh(_mean(_b, 126)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_tanhsig_252d_base_v125_signal(opex, revenue, closeadj):
    _b = _f07_efficiency_trend(opex, revenue, 252)
    result = np.tanh(_mean(_b, 252)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_median_5d_base_v126_signal(opex, sgna, revenue, closeadj):
    result = (_f07_efficiency_score(opex, sgna, revenue, 5)).rolling(5, min_periods=max(1, 5//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_median_21d_base_v127_signal(opex, sgna, revenue, closeadj):
    result = (_f07_efficiency_score(opex, sgna, revenue, 21)).rolling(21, min_periods=max(1, 21//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_median_63d_base_v128_signal(opex, sgna, revenue, closeadj):
    result = (_f07_efficiency_score(opex, sgna, revenue, 63)).rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_median_126d_base_v129_signal(opex, sgna, revenue, closeadj):
    result = (_f07_efficiency_score(opex, sgna, revenue, 126)).rolling(126, min_periods=max(1, 126//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_median_252d_base_v130_signal(opex, sgna, revenue, closeadj):
    result = (_f07_efficiency_score(opex, sgna, revenue, 252)).rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_rank_5d_base_v131_signal(opex, sgna, revenue, closeadj):
    result = (_f07_efficiency_score(opex, sgna, revenue, 5)).rolling(5, min_periods=max(1, 5//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_rank_21d_base_v132_signal(opex, sgna, revenue, closeadj):
    result = (_f07_efficiency_score(opex, sgna, revenue, 21)).rolling(21, min_periods=max(1, 21//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_rank_63d_base_v133_signal(opex, sgna, revenue, closeadj):
    result = (_f07_efficiency_score(opex, sgna, revenue, 63)).rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_rank_126d_base_v134_signal(opex, sgna, revenue, closeadj):
    result = (_f07_efficiency_score(opex, sgna, revenue, 126)).rolling(126, min_periods=max(1, 126//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_rank_252d_base_v135_signal(opex, sgna, revenue, closeadj):
    result = (_f07_efficiency_score(opex, sgna, revenue, 252)).rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_diff_5d_base_v136_signal(opex, sgna, revenue, closeadj):
    _b = _f07_efficiency_score(opex, sgna, revenue, 5)
    result = (_b - _b.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_diff_21d_base_v137_signal(opex, sgna, revenue, closeadj):
    _b = _f07_efficiency_score(opex, sgna, revenue, 21)
    result = (_b - _b.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_diff_63d_base_v138_signal(opex, sgna, revenue, closeadj):
    _b = _f07_efficiency_score(opex, sgna, revenue, 63)
    result = (_b - _b.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_diff_126d_base_v139_signal(opex, sgna, revenue, closeadj):
    _b = _f07_efficiency_score(opex, sgna, revenue, 126)
    result = (_b - _b.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_diff_252d_base_v140_signal(opex, sgna, revenue, closeadj):
    _b = _f07_efficiency_score(opex, sgna, revenue, 252)
    result = (_b - _b.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_logc_5d_base_v141_signal(opex, sgna, revenue, closeadj):
    result = _mean(_f07_efficiency_score(opex, sgna, revenue, 5), 5) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_logc_21d_base_v142_signal(opex, sgna, revenue, closeadj):
    result = _mean(_f07_efficiency_score(opex, sgna, revenue, 21), 21) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_logc_63d_base_v143_signal(opex, sgna, revenue, closeadj):
    result = _mean(_f07_efficiency_score(opex, sgna, revenue, 63), 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_logc_126d_base_v144_signal(opex, sgna, revenue, closeadj):
    result = _mean(_f07_efficiency_score(opex, sgna, revenue, 126), 126) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_logc_252d_base_v145_signal(opex, sgna, revenue, closeadj):
    result = _mean(_f07_efficiency_score(opex, sgna, revenue, 252), 252) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_tanhsig_5d_base_v146_signal(opex, sgna, revenue, closeadj):
    _b = _f07_efficiency_score(opex, sgna, revenue, 5)
    result = np.tanh(_mean(_b, 5)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_tanhsig_21d_base_v147_signal(opex, sgna, revenue, closeadj):
    _b = _f07_efficiency_score(opex, sgna, revenue, 21)
    result = np.tanh(_mean(_b, 21)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_tanhsig_63d_base_v148_signal(opex, sgna, revenue, closeadj):
    _b = _f07_efficiency_score(opex, sgna, revenue, 63)
    result = np.tanh(_mean(_b, 63)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_tanhsig_126d_base_v149_signal(opex, sgna, revenue, closeadj):
    _b = _f07_efficiency_score(opex, sgna, revenue, 126)
    result = np.tanh(_mean(_b, 126)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_tanhsig_252d_base_v150_signal(opex, sgna, revenue, closeadj):
    _b = _f07_efficiency_score(opex, sgna, revenue, 252)
    result = np.tanh(_mean(_b, 252)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f07uef_f07_utility_efficiency_opexint_median_5d_base_v076_signal,
    f07uef_f07_utility_efficiency_opexint_median_21d_base_v077_signal,
    f07uef_f07_utility_efficiency_opexint_median_63d_base_v078_signal,
    f07uef_f07_utility_efficiency_opexint_median_126d_base_v079_signal,
    f07uef_f07_utility_efficiency_opexint_median_252d_base_v080_signal,
    f07uef_f07_utility_efficiency_opexint_rank_5d_base_v081_signal,
    f07uef_f07_utility_efficiency_opexint_rank_21d_base_v082_signal,
    f07uef_f07_utility_efficiency_opexint_rank_63d_base_v083_signal,
    f07uef_f07_utility_efficiency_opexint_rank_126d_base_v084_signal,
    f07uef_f07_utility_efficiency_opexint_rank_252d_base_v085_signal,
    f07uef_f07_utility_efficiency_opexint_diff_5d_base_v086_signal,
    f07uef_f07_utility_efficiency_opexint_diff_21d_base_v087_signal,
    f07uef_f07_utility_efficiency_opexint_diff_63d_base_v088_signal,
    f07uef_f07_utility_efficiency_opexint_diff_126d_base_v089_signal,
    f07uef_f07_utility_efficiency_opexint_diff_252d_base_v090_signal,
    f07uef_f07_utility_efficiency_opexint_logc_5d_base_v091_signal,
    f07uef_f07_utility_efficiency_opexint_logc_21d_base_v092_signal,
    f07uef_f07_utility_efficiency_opexint_logc_63d_base_v093_signal,
    f07uef_f07_utility_efficiency_opexint_logc_126d_base_v094_signal,
    f07uef_f07_utility_efficiency_opexint_logc_252d_base_v095_signal,
    f07uef_f07_utility_efficiency_opexint_tanhsig_5d_base_v096_signal,
    f07uef_f07_utility_efficiency_opexint_tanhsig_21d_base_v097_signal,
    f07uef_f07_utility_efficiency_opexint_tanhsig_63d_base_v098_signal,
    f07uef_f07_utility_efficiency_opexint_tanhsig_126d_base_v099_signal,
    f07uef_f07_utility_efficiency_opexint_tanhsig_252d_base_v100_signal,
    f07uef_f07_utility_efficiency_efftrend_median_5d_base_v101_signal,
    f07uef_f07_utility_efficiency_efftrend_median_21d_base_v102_signal,
    f07uef_f07_utility_efficiency_efftrend_median_63d_base_v103_signal,
    f07uef_f07_utility_efficiency_efftrend_median_126d_base_v104_signal,
    f07uef_f07_utility_efficiency_efftrend_median_252d_base_v105_signal,
    f07uef_f07_utility_efficiency_efftrend_rank_5d_base_v106_signal,
    f07uef_f07_utility_efficiency_efftrend_rank_21d_base_v107_signal,
    f07uef_f07_utility_efficiency_efftrend_rank_63d_base_v108_signal,
    f07uef_f07_utility_efficiency_efftrend_rank_126d_base_v109_signal,
    f07uef_f07_utility_efficiency_efftrend_rank_252d_base_v110_signal,
    f07uef_f07_utility_efficiency_efftrend_diff_5d_base_v111_signal,
    f07uef_f07_utility_efficiency_efftrend_diff_21d_base_v112_signal,
    f07uef_f07_utility_efficiency_efftrend_diff_63d_base_v113_signal,
    f07uef_f07_utility_efficiency_efftrend_diff_126d_base_v114_signal,
    f07uef_f07_utility_efficiency_efftrend_diff_252d_base_v115_signal,
    f07uef_f07_utility_efficiency_efftrend_logc_5d_base_v116_signal,
    f07uef_f07_utility_efficiency_efftrend_logc_21d_base_v117_signal,
    f07uef_f07_utility_efficiency_efftrend_logc_63d_base_v118_signal,
    f07uef_f07_utility_efficiency_efftrend_logc_126d_base_v119_signal,
    f07uef_f07_utility_efficiency_efftrend_logc_252d_base_v120_signal,
    f07uef_f07_utility_efficiency_efftrend_tanhsig_5d_base_v121_signal,
    f07uef_f07_utility_efficiency_efftrend_tanhsig_21d_base_v122_signal,
    f07uef_f07_utility_efficiency_efftrend_tanhsig_63d_base_v123_signal,
    f07uef_f07_utility_efficiency_efftrend_tanhsig_126d_base_v124_signal,
    f07uef_f07_utility_efficiency_efftrend_tanhsig_252d_base_v125_signal,
    f07uef_f07_utility_efficiency_effsc_median_5d_base_v126_signal,
    f07uef_f07_utility_efficiency_effsc_median_21d_base_v127_signal,
    f07uef_f07_utility_efficiency_effsc_median_63d_base_v128_signal,
    f07uef_f07_utility_efficiency_effsc_median_126d_base_v129_signal,
    f07uef_f07_utility_efficiency_effsc_median_252d_base_v130_signal,
    f07uef_f07_utility_efficiency_effsc_rank_5d_base_v131_signal,
    f07uef_f07_utility_efficiency_effsc_rank_21d_base_v132_signal,
    f07uef_f07_utility_efficiency_effsc_rank_63d_base_v133_signal,
    f07uef_f07_utility_efficiency_effsc_rank_126d_base_v134_signal,
    f07uef_f07_utility_efficiency_effsc_rank_252d_base_v135_signal,
    f07uef_f07_utility_efficiency_effsc_diff_5d_base_v136_signal,
    f07uef_f07_utility_efficiency_effsc_diff_21d_base_v137_signal,
    f07uef_f07_utility_efficiency_effsc_diff_63d_base_v138_signal,
    f07uef_f07_utility_efficiency_effsc_diff_126d_base_v139_signal,
    f07uef_f07_utility_efficiency_effsc_diff_252d_base_v140_signal,
    f07uef_f07_utility_efficiency_effsc_logc_5d_base_v141_signal,
    f07uef_f07_utility_efficiency_effsc_logc_21d_base_v142_signal,
    f07uef_f07_utility_efficiency_effsc_logc_63d_base_v143_signal,
    f07uef_f07_utility_efficiency_effsc_logc_126d_base_v144_signal,
    f07uef_f07_utility_efficiency_effsc_logc_252d_base_v145_signal,
    f07uef_f07_utility_efficiency_effsc_tanhsig_5d_base_v146_signal,
    f07uef_f07_utility_efficiency_effsc_tanhsig_21d_base_v147_signal,
    f07uef_f07_utility_efficiency_effsc_tanhsig_63d_base_v148_signal,
    f07uef_f07_utility_efficiency_effsc_tanhsig_126d_base_v149_signal,
    f07uef_f07_utility_efficiency_effsc_tanhsig_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_UTILITY_EFFICIENCY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    sgna = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "sgna": sgna, "opex": opex,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f07_opex_intensity", "_f07_efficiency_trend", "_f07_efficiency_score",)
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
    print(f"OK f07_utility_efficiency_base_076_150_claude: {n_features} features pass")
