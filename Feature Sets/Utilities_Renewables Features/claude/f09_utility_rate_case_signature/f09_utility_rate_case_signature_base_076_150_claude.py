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
def _f09_margin_floor(ebitdamargin, w):
    return ebitdamargin.rolling(w, min_periods=max(1, w // 2)).min()


def _f09_margin_recovery(ebitdamargin, w):
    # current vs rolling min — how far margin recovered from trough
    trough = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).min()
    return ebitdamargin - trough


def _f09_margin_durability(grossmargin, ebitdamargin, w):
    gm = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    em = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    gm_std = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    em_std = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return (gm + em) - (gm_std + em_std)


def f09urc_f09_utility_rate_case_signature_mfloor_median_5d_base_v076_signal(ebitdamargin, closeadj):
    result = (_f09_margin_floor(ebitdamargin, 5)).rolling(5, min_periods=max(1, 5//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_median_21d_base_v077_signal(ebitdamargin, closeadj):
    result = (_f09_margin_floor(ebitdamargin, 21)).rolling(21, min_periods=max(1, 21//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_median_63d_base_v078_signal(ebitdamargin, closeadj):
    result = (_f09_margin_floor(ebitdamargin, 63)).rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_median_126d_base_v079_signal(ebitdamargin, closeadj):
    result = (_f09_margin_floor(ebitdamargin, 126)).rolling(126, min_periods=max(1, 126//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_median_252d_base_v080_signal(ebitdamargin, closeadj):
    result = (_f09_margin_floor(ebitdamargin, 252)).rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_rank_5d_base_v081_signal(ebitdamargin, closeadj):
    result = (_f09_margin_floor(ebitdamargin, 5)).rolling(5, min_periods=max(1, 5//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_rank_21d_base_v082_signal(ebitdamargin, closeadj):
    result = (_f09_margin_floor(ebitdamargin, 21)).rolling(21, min_periods=max(1, 21//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_rank_63d_base_v083_signal(ebitdamargin, closeadj):
    result = (_f09_margin_floor(ebitdamargin, 63)).rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_rank_126d_base_v084_signal(ebitdamargin, closeadj):
    result = (_f09_margin_floor(ebitdamargin, 126)).rolling(126, min_periods=max(1, 126//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_rank_252d_base_v085_signal(ebitdamargin, closeadj):
    result = (_f09_margin_floor(ebitdamargin, 252)).rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_diff_5d_base_v086_signal(ebitdamargin, closeadj):
    _b = _f09_margin_floor(ebitdamargin, 5)
    result = (_b - _b.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_diff_21d_base_v087_signal(ebitdamargin, closeadj):
    _b = _f09_margin_floor(ebitdamargin, 21)
    result = (_b - _b.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_diff_63d_base_v088_signal(ebitdamargin, closeadj):
    _b = _f09_margin_floor(ebitdamargin, 63)
    result = (_b - _b.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_diff_126d_base_v089_signal(ebitdamargin, closeadj):
    _b = _f09_margin_floor(ebitdamargin, 126)
    result = (_b - _b.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_diff_252d_base_v090_signal(ebitdamargin, closeadj):
    _b = _f09_margin_floor(ebitdamargin, 252)
    result = (_b - _b.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_logc_5d_base_v091_signal(ebitdamargin, closeadj):
    result = _mean(_f09_margin_floor(ebitdamargin, 5), 5) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_logc_21d_base_v092_signal(ebitdamargin, closeadj):
    result = _mean(_f09_margin_floor(ebitdamargin, 21), 21) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_logc_63d_base_v093_signal(ebitdamargin, closeadj):
    result = _mean(_f09_margin_floor(ebitdamargin, 63), 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_logc_126d_base_v094_signal(ebitdamargin, closeadj):
    result = _mean(_f09_margin_floor(ebitdamargin, 126), 126) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_logc_252d_base_v095_signal(ebitdamargin, closeadj):
    result = _mean(_f09_margin_floor(ebitdamargin, 252), 252) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_tanhsig_5d_base_v096_signal(ebitdamargin, closeadj):
    _b = _f09_margin_floor(ebitdamargin, 5)
    result = np.tanh(_mean(_b, 5)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_tanhsig_21d_base_v097_signal(ebitdamargin, closeadj):
    _b = _f09_margin_floor(ebitdamargin, 21)
    result = np.tanh(_mean(_b, 21)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_tanhsig_63d_base_v098_signal(ebitdamargin, closeadj):
    _b = _f09_margin_floor(ebitdamargin, 63)
    result = np.tanh(_mean(_b, 63)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_tanhsig_126d_base_v099_signal(ebitdamargin, closeadj):
    _b = _f09_margin_floor(ebitdamargin, 126)
    result = np.tanh(_mean(_b, 126)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_tanhsig_252d_base_v100_signal(ebitdamargin, closeadj):
    _b = _f09_margin_floor(ebitdamargin, 252)
    result = np.tanh(_mean(_b, 252)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_median_5d_base_v101_signal(ebitdamargin, closeadj):
    result = (_f09_margin_recovery(ebitdamargin, 5)).rolling(5, min_periods=max(1, 5//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_median_21d_base_v102_signal(ebitdamargin, closeadj):
    result = (_f09_margin_recovery(ebitdamargin, 21)).rolling(21, min_periods=max(1, 21//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_median_63d_base_v103_signal(ebitdamargin, closeadj):
    result = (_f09_margin_recovery(ebitdamargin, 63)).rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_median_126d_base_v104_signal(ebitdamargin, closeadj):
    result = (_f09_margin_recovery(ebitdamargin, 126)).rolling(126, min_periods=max(1, 126//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_median_252d_base_v105_signal(ebitdamargin, closeadj):
    result = (_f09_margin_recovery(ebitdamargin, 252)).rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_rank_5d_base_v106_signal(ebitdamargin, closeadj):
    result = (_f09_margin_recovery(ebitdamargin, 5)).rolling(5, min_periods=max(1, 5//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_rank_21d_base_v107_signal(ebitdamargin, closeadj):
    result = (_f09_margin_recovery(ebitdamargin, 21)).rolling(21, min_periods=max(1, 21//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_rank_63d_base_v108_signal(ebitdamargin, closeadj):
    result = (_f09_margin_recovery(ebitdamargin, 63)).rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_rank_126d_base_v109_signal(ebitdamargin, closeadj):
    result = (_f09_margin_recovery(ebitdamargin, 126)).rolling(126, min_periods=max(1, 126//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_rank_252d_base_v110_signal(ebitdamargin, closeadj):
    result = (_f09_margin_recovery(ebitdamargin, 252)).rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_diff_5d_base_v111_signal(ebitdamargin, closeadj):
    _b = _f09_margin_recovery(ebitdamargin, 5)
    result = (_b - _b.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_diff_21d_base_v112_signal(ebitdamargin, closeadj):
    _b = _f09_margin_recovery(ebitdamargin, 21)
    result = (_b - _b.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_diff_63d_base_v113_signal(ebitdamargin, closeadj):
    _b = _f09_margin_recovery(ebitdamargin, 63)
    result = (_b - _b.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_diff_126d_base_v114_signal(ebitdamargin, closeadj):
    _b = _f09_margin_recovery(ebitdamargin, 126)
    result = (_b - _b.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_diff_252d_base_v115_signal(ebitdamargin, closeadj):
    _b = _f09_margin_recovery(ebitdamargin, 252)
    result = (_b - _b.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_logc_5d_base_v116_signal(ebitdamargin, closeadj):
    result = _mean(_f09_margin_recovery(ebitdamargin, 5), 5) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_logc_21d_base_v117_signal(ebitdamargin, closeadj):
    result = _mean(_f09_margin_recovery(ebitdamargin, 21), 21) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_logc_63d_base_v118_signal(ebitdamargin, closeadj):
    result = _mean(_f09_margin_recovery(ebitdamargin, 63), 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_logc_126d_base_v119_signal(ebitdamargin, closeadj):
    result = _mean(_f09_margin_recovery(ebitdamargin, 126), 126) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_logc_252d_base_v120_signal(ebitdamargin, closeadj):
    result = _mean(_f09_margin_recovery(ebitdamargin, 252), 252) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_tanhsig_5d_base_v121_signal(ebitdamargin, closeadj):
    _b = _f09_margin_recovery(ebitdamargin, 5)
    result = np.tanh(_mean(_b, 5)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_tanhsig_21d_base_v122_signal(ebitdamargin, closeadj):
    _b = _f09_margin_recovery(ebitdamargin, 21)
    result = np.tanh(_mean(_b, 21)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_tanhsig_63d_base_v123_signal(ebitdamargin, closeadj):
    _b = _f09_margin_recovery(ebitdamargin, 63)
    result = np.tanh(_mean(_b, 63)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_tanhsig_126d_base_v124_signal(ebitdamargin, closeadj):
    _b = _f09_margin_recovery(ebitdamargin, 126)
    result = np.tanh(_mean(_b, 126)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_tanhsig_252d_base_v125_signal(ebitdamargin, closeadj):
    _b = _f09_margin_recovery(ebitdamargin, 252)
    result = np.tanh(_mean(_b, 252)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_median_5d_base_v126_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f09_margin_durability(grossmargin, ebitdamargin, 5)).rolling(5, min_periods=max(1, 5//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_median_21d_base_v127_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f09_margin_durability(grossmargin, ebitdamargin, 21)).rolling(21, min_periods=max(1, 21//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_median_63d_base_v128_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f09_margin_durability(grossmargin, ebitdamargin, 63)).rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_median_126d_base_v129_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f09_margin_durability(grossmargin, ebitdamargin, 126)).rolling(126, min_periods=max(1, 126//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_median_252d_base_v130_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f09_margin_durability(grossmargin, ebitdamargin, 252)).rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_rank_5d_base_v131_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f09_margin_durability(grossmargin, ebitdamargin, 5)).rolling(5, min_periods=max(1, 5//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_rank_21d_base_v132_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f09_margin_durability(grossmargin, ebitdamargin, 21)).rolling(21, min_periods=max(1, 21//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_rank_63d_base_v133_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f09_margin_durability(grossmargin, ebitdamargin, 63)).rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_rank_126d_base_v134_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f09_margin_durability(grossmargin, ebitdamargin, 126)).rolling(126, min_periods=max(1, 126//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_rank_252d_base_v135_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f09_margin_durability(grossmargin, ebitdamargin, 252)).rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_diff_5d_base_v136_signal(grossmargin, ebitdamargin, closeadj):
    _b = _f09_margin_durability(grossmargin, ebitdamargin, 5)
    result = (_b - _b.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_diff_21d_base_v137_signal(grossmargin, ebitdamargin, closeadj):
    _b = _f09_margin_durability(grossmargin, ebitdamargin, 21)
    result = (_b - _b.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_diff_63d_base_v138_signal(grossmargin, ebitdamargin, closeadj):
    _b = _f09_margin_durability(grossmargin, ebitdamargin, 63)
    result = (_b - _b.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_diff_126d_base_v139_signal(grossmargin, ebitdamargin, closeadj):
    _b = _f09_margin_durability(grossmargin, ebitdamargin, 126)
    result = (_b - _b.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_diff_252d_base_v140_signal(grossmargin, ebitdamargin, closeadj):
    _b = _f09_margin_durability(grossmargin, ebitdamargin, 252)
    result = (_b - _b.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_logc_5d_base_v141_signal(grossmargin, ebitdamargin, closeadj):
    result = _mean(_f09_margin_durability(grossmargin, ebitdamargin, 5), 5) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_logc_21d_base_v142_signal(grossmargin, ebitdamargin, closeadj):
    result = _mean(_f09_margin_durability(grossmargin, ebitdamargin, 21), 21) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_logc_63d_base_v143_signal(grossmargin, ebitdamargin, closeadj):
    result = _mean(_f09_margin_durability(grossmargin, ebitdamargin, 63), 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_logc_126d_base_v144_signal(grossmargin, ebitdamargin, closeadj):
    result = _mean(_f09_margin_durability(grossmargin, ebitdamargin, 126), 126) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_logc_252d_base_v145_signal(grossmargin, ebitdamargin, closeadj):
    result = _mean(_f09_margin_durability(grossmargin, ebitdamargin, 252), 252) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_tanhsig_5d_base_v146_signal(grossmargin, ebitdamargin, closeadj):
    _b = _f09_margin_durability(grossmargin, ebitdamargin, 5)
    result = np.tanh(_mean(_b, 5)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_tanhsig_21d_base_v147_signal(grossmargin, ebitdamargin, closeadj):
    _b = _f09_margin_durability(grossmargin, ebitdamargin, 21)
    result = np.tanh(_mean(_b, 21)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_tanhsig_63d_base_v148_signal(grossmargin, ebitdamargin, closeadj):
    _b = _f09_margin_durability(grossmargin, ebitdamargin, 63)
    result = np.tanh(_mean(_b, 63)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_tanhsig_126d_base_v149_signal(grossmargin, ebitdamargin, closeadj):
    _b = _f09_margin_durability(grossmargin, ebitdamargin, 126)
    result = np.tanh(_mean(_b, 126)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_tanhsig_252d_base_v150_signal(grossmargin, ebitdamargin, closeadj):
    _b = _f09_margin_durability(grossmargin, ebitdamargin, 252)
    result = np.tanh(_mean(_b, 252)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f09urc_f09_utility_rate_case_signature_mfloor_median_5d_base_v076_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_median_21d_base_v077_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_median_63d_base_v078_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_median_126d_base_v079_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_median_252d_base_v080_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_rank_5d_base_v081_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_rank_21d_base_v082_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_rank_63d_base_v083_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_rank_126d_base_v084_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_rank_252d_base_v085_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_diff_5d_base_v086_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_diff_21d_base_v087_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_diff_63d_base_v088_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_diff_126d_base_v089_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_diff_252d_base_v090_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_logc_5d_base_v091_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_logc_21d_base_v092_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_logc_63d_base_v093_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_logc_126d_base_v094_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_logc_252d_base_v095_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_tanhsig_5d_base_v096_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_tanhsig_21d_base_v097_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_tanhsig_63d_base_v098_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_tanhsig_126d_base_v099_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_tanhsig_252d_base_v100_signal,
    f09urc_f09_utility_rate_case_signature_mrec_median_5d_base_v101_signal,
    f09urc_f09_utility_rate_case_signature_mrec_median_21d_base_v102_signal,
    f09urc_f09_utility_rate_case_signature_mrec_median_63d_base_v103_signal,
    f09urc_f09_utility_rate_case_signature_mrec_median_126d_base_v104_signal,
    f09urc_f09_utility_rate_case_signature_mrec_median_252d_base_v105_signal,
    f09urc_f09_utility_rate_case_signature_mrec_rank_5d_base_v106_signal,
    f09urc_f09_utility_rate_case_signature_mrec_rank_21d_base_v107_signal,
    f09urc_f09_utility_rate_case_signature_mrec_rank_63d_base_v108_signal,
    f09urc_f09_utility_rate_case_signature_mrec_rank_126d_base_v109_signal,
    f09urc_f09_utility_rate_case_signature_mrec_rank_252d_base_v110_signal,
    f09urc_f09_utility_rate_case_signature_mrec_diff_5d_base_v111_signal,
    f09urc_f09_utility_rate_case_signature_mrec_diff_21d_base_v112_signal,
    f09urc_f09_utility_rate_case_signature_mrec_diff_63d_base_v113_signal,
    f09urc_f09_utility_rate_case_signature_mrec_diff_126d_base_v114_signal,
    f09urc_f09_utility_rate_case_signature_mrec_diff_252d_base_v115_signal,
    f09urc_f09_utility_rate_case_signature_mrec_logc_5d_base_v116_signal,
    f09urc_f09_utility_rate_case_signature_mrec_logc_21d_base_v117_signal,
    f09urc_f09_utility_rate_case_signature_mrec_logc_63d_base_v118_signal,
    f09urc_f09_utility_rate_case_signature_mrec_logc_126d_base_v119_signal,
    f09urc_f09_utility_rate_case_signature_mrec_logc_252d_base_v120_signal,
    f09urc_f09_utility_rate_case_signature_mrec_tanhsig_5d_base_v121_signal,
    f09urc_f09_utility_rate_case_signature_mrec_tanhsig_21d_base_v122_signal,
    f09urc_f09_utility_rate_case_signature_mrec_tanhsig_63d_base_v123_signal,
    f09urc_f09_utility_rate_case_signature_mrec_tanhsig_126d_base_v124_signal,
    f09urc_f09_utility_rate_case_signature_mrec_tanhsig_252d_base_v125_signal,
    f09urc_f09_utility_rate_case_signature_mdur_median_5d_base_v126_signal,
    f09urc_f09_utility_rate_case_signature_mdur_median_21d_base_v127_signal,
    f09urc_f09_utility_rate_case_signature_mdur_median_63d_base_v128_signal,
    f09urc_f09_utility_rate_case_signature_mdur_median_126d_base_v129_signal,
    f09urc_f09_utility_rate_case_signature_mdur_median_252d_base_v130_signal,
    f09urc_f09_utility_rate_case_signature_mdur_rank_5d_base_v131_signal,
    f09urc_f09_utility_rate_case_signature_mdur_rank_21d_base_v132_signal,
    f09urc_f09_utility_rate_case_signature_mdur_rank_63d_base_v133_signal,
    f09urc_f09_utility_rate_case_signature_mdur_rank_126d_base_v134_signal,
    f09urc_f09_utility_rate_case_signature_mdur_rank_252d_base_v135_signal,
    f09urc_f09_utility_rate_case_signature_mdur_diff_5d_base_v136_signal,
    f09urc_f09_utility_rate_case_signature_mdur_diff_21d_base_v137_signal,
    f09urc_f09_utility_rate_case_signature_mdur_diff_63d_base_v138_signal,
    f09urc_f09_utility_rate_case_signature_mdur_diff_126d_base_v139_signal,
    f09urc_f09_utility_rate_case_signature_mdur_diff_252d_base_v140_signal,
    f09urc_f09_utility_rate_case_signature_mdur_logc_5d_base_v141_signal,
    f09urc_f09_utility_rate_case_signature_mdur_logc_21d_base_v142_signal,
    f09urc_f09_utility_rate_case_signature_mdur_logc_63d_base_v143_signal,
    f09urc_f09_utility_rate_case_signature_mdur_logc_126d_base_v144_signal,
    f09urc_f09_utility_rate_case_signature_mdur_logc_252d_base_v145_signal,
    f09urc_f09_utility_rate_case_signature_mdur_tanhsig_5d_base_v146_signal,
    f09urc_f09_utility_rate_case_signature_mdur_tanhsig_21d_base_v147_signal,
    f09urc_f09_utility_rate_case_signature_mdur_tanhsig_63d_base_v148_signal,
    f09urc_f09_utility_rate_case_signature_mdur_tanhsig_126d_base_v149_signal,
    f09urc_f09_utility_rate_case_signature_mdur_tanhsig_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_UTILITY_RATE_CASE_SIGNATURE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    grossmargin = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {
        "closeadj": closeadj, "grossmargin": grossmargin,
        "ebitdamargin": ebitdamargin, "netmargin": netmargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f09_margin_floor", "_f09_margin_recovery", "_f09_margin_durability",)
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
    print(f"OK f09_utility_rate_case_signature_base_076_150_claude: {n_features} features pass")
