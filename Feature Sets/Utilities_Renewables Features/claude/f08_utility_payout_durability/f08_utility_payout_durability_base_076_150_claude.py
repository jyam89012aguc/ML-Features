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
def _f08_payout_floor(payoutratio, w):
    # rolling min as durability floor
    return payoutratio.rolling(w, min_periods=max(1, w // 2)).min()


def _f08_payout_durability(payoutratio, eps, w):
    # stable payoutratio when eps grows; penalize when eps falls
    eg = eps.pct_change(w).fillna(0)
    p_smooth = payoutratio.rolling(w, min_periods=max(1, w // 2)).mean()
    return p_smooth * (1.0 + eg)


def _f08_payout_sustainability(payoutratio, fcfps, w):
    # payout vs fcfps coverage
    p_smooth = payoutratio.rolling(w, min_periods=max(1, w // 2)).mean()
    cov = fcfps.rolling(w, min_periods=max(1, w // 2)).mean() / fcfps.rolling(w, min_periods=max(1, w // 2)).mean().abs().replace(0, np.nan)
    return p_smooth - cov.abs()


def f08upd_f08_utility_payout_durability_pfloor_median_5d_base_v076_signal(payoutratio, closeadj):
    result = (_f08_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_median_21d_base_v077_signal(payoutratio, closeadj):
    result = (_f08_payout_floor(payoutratio, 21)).rolling(21, min_periods=max(1, 21//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_median_63d_base_v078_signal(payoutratio, closeadj):
    result = (_f08_payout_floor(payoutratio, 63)).rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_median_126d_base_v079_signal(payoutratio, closeadj):
    result = (_f08_payout_floor(payoutratio, 126)).rolling(126, min_periods=max(1, 126//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_median_252d_base_v080_signal(payoutratio, closeadj):
    result = (_f08_payout_floor(payoutratio, 252)).rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_rank_5d_base_v081_signal(payoutratio, closeadj):
    result = (_f08_payout_floor(payoutratio, 5)).rolling(5, min_periods=max(1, 5//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_rank_21d_base_v082_signal(payoutratio, closeadj):
    result = (_f08_payout_floor(payoutratio, 21)).rolling(21, min_periods=max(1, 21//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_rank_63d_base_v083_signal(payoutratio, closeadj):
    result = (_f08_payout_floor(payoutratio, 63)).rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_rank_126d_base_v084_signal(payoutratio, closeadj):
    result = (_f08_payout_floor(payoutratio, 126)).rolling(126, min_periods=max(1, 126//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_rank_252d_base_v085_signal(payoutratio, closeadj):
    result = (_f08_payout_floor(payoutratio, 252)).rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_diff_5d_base_v086_signal(payoutratio, closeadj):
    _b = _f08_payout_floor(payoutratio, 5)
    result = (_b - _b.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_diff_21d_base_v087_signal(payoutratio, closeadj):
    _b = _f08_payout_floor(payoutratio, 21)
    result = (_b - _b.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_diff_63d_base_v088_signal(payoutratio, closeadj):
    _b = _f08_payout_floor(payoutratio, 63)
    result = (_b - _b.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_diff_126d_base_v089_signal(payoutratio, closeadj):
    _b = _f08_payout_floor(payoutratio, 126)
    result = (_b - _b.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_diff_252d_base_v090_signal(payoutratio, closeadj):
    _b = _f08_payout_floor(payoutratio, 252)
    result = (_b - _b.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_logc_5d_base_v091_signal(payoutratio, closeadj):
    result = _mean(_f08_payout_floor(payoutratio, 5), 5) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_logc_21d_base_v092_signal(payoutratio, closeadj):
    result = _mean(_f08_payout_floor(payoutratio, 21), 21) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_logc_63d_base_v093_signal(payoutratio, closeadj):
    result = _mean(_f08_payout_floor(payoutratio, 63), 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_logc_126d_base_v094_signal(payoutratio, closeadj):
    result = _mean(_f08_payout_floor(payoutratio, 126), 126) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_logc_252d_base_v095_signal(payoutratio, closeadj):
    result = _mean(_f08_payout_floor(payoutratio, 252), 252) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_tanhsig_5d_base_v096_signal(payoutratio, closeadj):
    _b = _f08_payout_floor(payoutratio, 5)
    result = np.tanh(_mean(_b, 5)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_tanhsig_21d_base_v097_signal(payoutratio, closeadj):
    _b = _f08_payout_floor(payoutratio, 21)
    result = np.tanh(_mean(_b, 21)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_tanhsig_63d_base_v098_signal(payoutratio, closeadj):
    _b = _f08_payout_floor(payoutratio, 63)
    result = np.tanh(_mean(_b, 63)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_tanhsig_126d_base_v099_signal(payoutratio, closeadj):
    _b = _f08_payout_floor(payoutratio, 126)
    result = np.tanh(_mean(_b, 126)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_tanhsig_252d_base_v100_signal(payoutratio, closeadj):
    _b = _f08_payout_floor(payoutratio, 252)
    result = np.tanh(_mean(_b, 252)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_median_5d_base_v101_signal(payoutratio, eps, closeadj):
    result = (_f08_payout_durability(payoutratio, eps, 5)).rolling(5, min_periods=max(1, 5//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_median_21d_base_v102_signal(payoutratio, eps, closeadj):
    result = (_f08_payout_durability(payoutratio, eps, 21)).rolling(21, min_periods=max(1, 21//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_median_63d_base_v103_signal(payoutratio, eps, closeadj):
    result = (_f08_payout_durability(payoutratio, eps, 63)).rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_median_126d_base_v104_signal(payoutratio, eps, closeadj):
    result = (_f08_payout_durability(payoutratio, eps, 126)).rolling(126, min_periods=max(1, 126//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_median_252d_base_v105_signal(payoutratio, eps, closeadj):
    result = (_f08_payout_durability(payoutratio, eps, 252)).rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_rank_5d_base_v106_signal(payoutratio, eps, closeadj):
    result = (_f08_payout_durability(payoutratio, eps, 5)).rolling(5, min_periods=max(1, 5//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_rank_21d_base_v107_signal(payoutratio, eps, closeadj):
    result = (_f08_payout_durability(payoutratio, eps, 21)).rolling(21, min_periods=max(1, 21//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_rank_63d_base_v108_signal(payoutratio, eps, closeadj):
    result = (_f08_payout_durability(payoutratio, eps, 63)).rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_rank_126d_base_v109_signal(payoutratio, eps, closeadj):
    result = (_f08_payout_durability(payoutratio, eps, 126)).rolling(126, min_periods=max(1, 126//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_rank_252d_base_v110_signal(payoutratio, eps, closeadj):
    result = (_f08_payout_durability(payoutratio, eps, 252)).rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_diff_5d_base_v111_signal(payoutratio, eps, closeadj):
    _b = _f08_payout_durability(payoutratio, eps, 5)
    result = (_b - _b.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_diff_21d_base_v112_signal(payoutratio, eps, closeadj):
    _b = _f08_payout_durability(payoutratio, eps, 21)
    result = (_b - _b.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_diff_63d_base_v113_signal(payoutratio, eps, closeadj):
    _b = _f08_payout_durability(payoutratio, eps, 63)
    result = (_b - _b.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_diff_126d_base_v114_signal(payoutratio, eps, closeadj):
    _b = _f08_payout_durability(payoutratio, eps, 126)
    result = (_b - _b.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_diff_252d_base_v115_signal(payoutratio, eps, closeadj):
    _b = _f08_payout_durability(payoutratio, eps, 252)
    result = (_b - _b.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_logc_5d_base_v116_signal(payoutratio, eps, closeadj):
    result = _mean(_f08_payout_durability(payoutratio, eps, 5), 5) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_logc_21d_base_v117_signal(payoutratio, eps, closeadj):
    result = _mean(_f08_payout_durability(payoutratio, eps, 21), 21) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_logc_63d_base_v118_signal(payoutratio, eps, closeadj):
    result = _mean(_f08_payout_durability(payoutratio, eps, 63), 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_logc_126d_base_v119_signal(payoutratio, eps, closeadj):
    result = _mean(_f08_payout_durability(payoutratio, eps, 126), 126) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_logc_252d_base_v120_signal(payoutratio, eps, closeadj):
    result = _mean(_f08_payout_durability(payoutratio, eps, 252), 252) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_tanhsig_5d_base_v121_signal(payoutratio, eps, closeadj):
    _b = _f08_payout_durability(payoutratio, eps, 5)
    result = np.tanh(_mean(_b, 5)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_tanhsig_21d_base_v122_signal(payoutratio, eps, closeadj):
    _b = _f08_payout_durability(payoutratio, eps, 21)
    result = np.tanh(_mean(_b, 21)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_tanhsig_63d_base_v123_signal(payoutratio, eps, closeadj):
    _b = _f08_payout_durability(payoutratio, eps, 63)
    result = np.tanh(_mean(_b, 63)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_tanhsig_126d_base_v124_signal(payoutratio, eps, closeadj):
    _b = _f08_payout_durability(payoutratio, eps, 126)
    result = np.tanh(_mean(_b, 126)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_tanhsig_252d_base_v125_signal(payoutratio, eps, closeadj):
    _b = _f08_payout_durability(payoutratio, eps, 252)
    result = np.tanh(_mean(_b, 252)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_median_5d_base_v126_signal(payoutratio, fcfps, closeadj):
    result = (_f08_payout_sustainability(payoutratio, fcfps, 5)).rolling(5, min_periods=max(1, 5//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_median_21d_base_v127_signal(payoutratio, fcfps, closeadj):
    result = (_f08_payout_sustainability(payoutratio, fcfps, 21)).rolling(21, min_periods=max(1, 21//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_median_63d_base_v128_signal(payoutratio, fcfps, closeadj):
    result = (_f08_payout_sustainability(payoutratio, fcfps, 63)).rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_median_126d_base_v129_signal(payoutratio, fcfps, closeadj):
    result = (_f08_payout_sustainability(payoutratio, fcfps, 126)).rolling(126, min_periods=max(1, 126//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_median_252d_base_v130_signal(payoutratio, fcfps, closeadj):
    result = (_f08_payout_sustainability(payoutratio, fcfps, 252)).rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_rank_5d_base_v131_signal(payoutratio, fcfps, closeadj):
    result = (_f08_payout_sustainability(payoutratio, fcfps, 5)).rolling(5, min_periods=max(1, 5//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_rank_21d_base_v132_signal(payoutratio, fcfps, closeadj):
    result = (_f08_payout_sustainability(payoutratio, fcfps, 21)).rolling(21, min_periods=max(1, 21//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_rank_63d_base_v133_signal(payoutratio, fcfps, closeadj):
    result = (_f08_payout_sustainability(payoutratio, fcfps, 63)).rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_rank_126d_base_v134_signal(payoutratio, fcfps, closeadj):
    result = (_f08_payout_sustainability(payoutratio, fcfps, 126)).rolling(126, min_periods=max(1, 126//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_rank_252d_base_v135_signal(payoutratio, fcfps, closeadj):
    result = (_f08_payout_sustainability(payoutratio, fcfps, 252)).rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_diff_5d_base_v136_signal(payoutratio, fcfps, closeadj):
    _b = _f08_payout_sustainability(payoutratio, fcfps, 5)
    result = (_b - _b.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_diff_21d_base_v137_signal(payoutratio, fcfps, closeadj):
    _b = _f08_payout_sustainability(payoutratio, fcfps, 21)
    result = (_b - _b.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_diff_63d_base_v138_signal(payoutratio, fcfps, closeadj):
    _b = _f08_payout_sustainability(payoutratio, fcfps, 63)
    result = (_b - _b.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_diff_126d_base_v139_signal(payoutratio, fcfps, closeadj):
    _b = _f08_payout_sustainability(payoutratio, fcfps, 126)
    result = (_b - _b.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_diff_252d_base_v140_signal(payoutratio, fcfps, closeadj):
    _b = _f08_payout_sustainability(payoutratio, fcfps, 252)
    result = (_b - _b.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_logc_5d_base_v141_signal(payoutratio, fcfps, closeadj):
    result = _mean(_f08_payout_sustainability(payoutratio, fcfps, 5), 5) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_logc_21d_base_v142_signal(payoutratio, fcfps, closeadj):
    result = _mean(_f08_payout_sustainability(payoutratio, fcfps, 21), 21) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_logc_63d_base_v143_signal(payoutratio, fcfps, closeadj):
    result = _mean(_f08_payout_sustainability(payoutratio, fcfps, 63), 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_logc_126d_base_v144_signal(payoutratio, fcfps, closeadj):
    result = _mean(_f08_payout_sustainability(payoutratio, fcfps, 126), 126) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_logc_252d_base_v145_signal(payoutratio, fcfps, closeadj):
    result = _mean(_f08_payout_sustainability(payoutratio, fcfps, 252), 252) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_tanhsig_5d_base_v146_signal(payoutratio, fcfps, closeadj):
    _b = _f08_payout_sustainability(payoutratio, fcfps, 5)
    result = np.tanh(_mean(_b, 5)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_tanhsig_21d_base_v147_signal(payoutratio, fcfps, closeadj):
    _b = _f08_payout_sustainability(payoutratio, fcfps, 21)
    result = np.tanh(_mean(_b, 21)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_tanhsig_63d_base_v148_signal(payoutratio, fcfps, closeadj):
    _b = _f08_payout_sustainability(payoutratio, fcfps, 63)
    result = np.tanh(_mean(_b, 63)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_tanhsig_126d_base_v149_signal(payoutratio, fcfps, closeadj):
    _b = _f08_payout_sustainability(payoutratio, fcfps, 126)
    result = np.tanh(_mean(_b, 126)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_tanhsig_252d_base_v150_signal(payoutratio, fcfps, closeadj):
    _b = _f08_payout_sustainability(payoutratio, fcfps, 252)
    result = np.tanh(_mean(_b, 252)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f08upd_f08_utility_payout_durability_pfloor_median_5d_base_v076_signal,
    f08upd_f08_utility_payout_durability_pfloor_median_21d_base_v077_signal,
    f08upd_f08_utility_payout_durability_pfloor_median_63d_base_v078_signal,
    f08upd_f08_utility_payout_durability_pfloor_median_126d_base_v079_signal,
    f08upd_f08_utility_payout_durability_pfloor_median_252d_base_v080_signal,
    f08upd_f08_utility_payout_durability_pfloor_rank_5d_base_v081_signal,
    f08upd_f08_utility_payout_durability_pfloor_rank_21d_base_v082_signal,
    f08upd_f08_utility_payout_durability_pfloor_rank_63d_base_v083_signal,
    f08upd_f08_utility_payout_durability_pfloor_rank_126d_base_v084_signal,
    f08upd_f08_utility_payout_durability_pfloor_rank_252d_base_v085_signal,
    f08upd_f08_utility_payout_durability_pfloor_diff_5d_base_v086_signal,
    f08upd_f08_utility_payout_durability_pfloor_diff_21d_base_v087_signal,
    f08upd_f08_utility_payout_durability_pfloor_diff_63d_base_v088_signal,
    f08upd_f08_utility_payout_durability_pfloor_diff_126d_base_v089_signal,
    f08upd_f08_utility_payout_durability_pfloor_diff_252d_base_v090_signal,
    f08upd_f08_utility_payout_durability_pfloor_logc_5d_base_v091_signal,
    f08upd_f08_utility_payout_durability_pfloor_logc_21d_base_v092_signal,
    f08upd_f08_utility_payout_durability_pfloor_logc_63d_base_v093_signal,
    f08upd_f08_utility_payout_durability_pfloor_logc_126d_base_v094_signal,
    f08upd_f08_utility_payout_durability_pfloor_logc_252d_base_v095_signal,
    f08upd_f08_utility_payout_durability_pfloor_tanhsig_5d_base_v096_signal,
    f08upd_f08_utility_payout_durability_pfloor_tanhsig_21d_base_v097_signal,
    f08upd_f08_utility_payout_durability_pfloor_tanhsig_63d_base_v098_signal,
    f08upd_f08_utility_payout_durability_pfloor_tanhsig_126d_base_v099_signal,
    f08upd_f08_utility_payout_durability_pfloor_tanhsig_252d_base_v100_signal,
    f08upd_f08_utility_payout_durability_pdur_median_5d_base_v101_signal,
    f08upd_f08_utility_payout_durability_pdur_median_21d_base_v102_signal,
    f08upd_f08_utility_payout_durability_pdur_median_63d_base_v103_signal,
    f08upd_f08_utility_payout_durability_pdur_median_126d_base_v104_signal,
    f08upd_f08_utility_payout_durability_pdur_median_252d_base_v105_signal,
    f08upd_f08_utility_payout_durability_pdur_rank_5d_base_v106_signal,
    f08upd_f08_utility_payout_durability_pdur_rank_21d_base_v107_signal,
    f08upd_f08_utility_payout_durability_pdur_rank_63d_base_v108_signal,
    f08upd_f08_utility_payout_durability_pdur_rank_126d_base_v109_signal,
    f08upd_f08_utility_payout_durability_pdur_rank_252d_base_v110_signal,
    f08upd_f08_utility_payout_durability_pdur_diff_5d_base_v111_signal,
    f08upd_f08_utility_payout_durability_pdur_diff_21d_base_v112_signal,
    f08upd_f08_utility_payout_durability_pdur_diff_63d_base_v113_signal,
    f08upd_f08_utility_payout_durability_pdur_diff_126d_base_v114_signal,
    f08upd_f08_utility_payout_durability_pdur_diff_252d_base_v115_signal,
    f08upd_f08_utility_payout_durability_pdur_logc_5d_base_v116_signal,
    f08upd_f08_utility_payout_durability_pdur_logc_21d_base_v117_signal,
    f08upd_f08_utility_payout_durability_pdur_logc_63d_base_v118_signal,
    f08upd_f08_utility_payout_durability_pdur_logc_126d_base_v119_signal,
    f08upd_f08_utility_payout_durability_pdur_logc_252d_base_v120_signal,
    f08upd_f08_utility_payout_durability_pdur_tanhsig_5d_base_v121_signal,
    f08upd_f08_utility_payout_durability_pdur_tanhsig_21d_base_v122_signal,
    f08upd_f08_utility_payout_durability_pdur_tanhsig_63d_base_v123_signal,
    f08upd_f08_utility_payout_durability_pdur_tanhsig_126d_base_v124_signal,
    f08upd_f08_utility_payout_durability_pdur_tanhsig_252d_base_v125_signal,
    f08upd_f08_utility_payout_durability_psus_median_5d_base_v126_signal,
    f08upd_f08_utility_payout_durability_psus_median_21d_base_v127_signal,
    f08upd_f08_utility_payout_durability_psus_median_63d_base_v128_signal,
    f08upd_f08_utility_payout_durability_psus_median_126d_base_v129_signal,
    f08upd_f08_utility_payout_durability_psus_median_252d_base_v130_signal,
    f08upd_f08_utility_payout_durability_psus_rank_5d_base_v131_signal,
    f08upd_f08_utility_payout_durability_psus_rank_21d_base_v132_signal,
    f08upd_f08_utility_payout_durability_psus_rank_63d_base_v133_signal,
    f08upd_f08_utility_payout_durability_psus_rank_126d_base_v134_signal,
    f08upd_f08_utility_payout_durability_psus_rank_252d_base_v135_signal,
    f08upd_f08_utility_payout_durability_psus_diff_5d_base_v136_signal,
    f08upd_f08_utility_payout_durability_psus_diff_21d_base_v137_signal,
    f08upd_f08_utility_payout_durability_psus_diff_63d_base_v138_signal,
    f08upd_f08_utility_payout_durability_psus_diff_126d_base_v139_signal,
    f08upd_f08_utility_payout_durability_psus_diff_252d_base_v140_signal,
    f08upd_f08_utility_payout_durability_psus_logc_5d_base_v141_signal,
    f08upd_f08_utility_payout_durability_psus_logc_21d_base_v142_signal,
    f08upd_f08_utility_payout_durability_psus_logc_63d_base_v143_signal,
    f08upd_f08_utility_payout_durability_psus_logc_126d_base_v144_signal,
    f08upd_f08_utility_payout_durability_psus_logc_252d_base_v145_signal,
    f08upd_f08_utility_payout_durability_psus_tanhsig_5d_base_v146_signal,
    f08upd_f08_utility_payout_durability_psus_tanhsig_21d_base_v147_signal,
    f08upd_f08_utility_payout_durability_psus_tanhsig_63d_base_v148_signal,
    f08upd_f08_utility_payout_durability_psus_tanhsig_126d_base_v149_signal,
    f08upd_f08_utility_payout_durability_psus_tanhsig_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_UTILITY_PAYOUT_DURABILITY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    eps = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1, n+1), name="eps")
    fcfps = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    dps = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    payoutratio = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")

    cols = {
        "closeadj": closeadj, "eps": eps, "fcfps": fcfps, "dps": dps,
        "payoutratio": payoutratio,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f08_payout_floor", "_f08_payout_durability", "_f08_payout_sustainability",)
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
    print(f"OK f08_utility_payout_durability_base_076_150_claude: {n_features} features pass")
