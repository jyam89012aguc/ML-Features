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
def _f10_long_cycle_growth(revenue, w):
    return revenue.pct_change(periods=w)


def _f10_compounding_quality(revenue, w):
    g = revenue.pct_change(periods=w)
    g_mean = g.rolling(w, min_periods=max(1, w // 2)).mean()
    g_std = g.rolling(w, min_periods=max(1, w // 2)).std()
    return g_mean / g_std.replace(0, np.nan)


def _f10_revenue_compound(revenue, ebitda, w):
    rg = revenue.pct_change(periods=w)
    eg = ebitda.pct_change(periods=w)
    return (rg + eg) * 0.5


def f10urg_f10_utility_regulated_growth_longg_median_5d_base_v076_signal(revenue, closeadj):
    result = (_f10_long_cycle_growth(revenue, 5)).rolling(5, min_periods=max(1, 5//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_median_21d_base_v077_signal(revenue, closeadj):
    result = (_f10_long_cycle_growth(revenue, 21)).rolling(21, min_periods=max(1, 21//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_median_63d_base_v078_signal(revenue, closeadj):
    result = (_f10_long_cycle_growth(revenue, 63)).rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_median_126d_base_v079_signal(revenue, closeadj):
    result = (_f10_long_cycle_growth(revenue, 126)).rolling(126, min_periods=max(1, 126//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_median_252d_base_v080_signal(revenue, closeadj):
    result = (_f10_long_cycle_growth(revenue, 252)).rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_rank_5d_base_v081_signal(revenue, closeadj):
    result = (_f10_long_cycle_growth(revenue, 5)).rolling(5, min_periods=max(1, 5//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_rank_21d_base_v082_signal(revenue, closeadj):
    result = (_f10_long_cycle_growth(revenue, 21)).rolling(21, min_periods=max(1, 21//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_rank_63d_base_v083_signal(revenue, closeadj):
    result = (_f10_long_cycle_growth(revenue, 63)).rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_rank_126d_base_v084_signal(revenue, closeadj):
    result = (_f10_long_cycle_growth(revenue, 126)).rolling(126, min_periods=max(1, 126//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_rank_252d_base_v085_signal(revenue, closeadj):
    result = (_f10_long_cycle_growth(revenue, 252)).rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_diff_5d_base_v086_signal(revenue, closeadj):
    _b = _f10_long_cycle_growth(revenue, 5)
    result = (_b - _b.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_diff_21d_base_v087_signal(revenue, closeadj):
    _b = _f10_long_cycle_growth(revenue, 21)
    result = (_b - _b.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_diff_63d_base_v088_signal(revenue, closeadj):
    _b = _f10_long_cycle_growth(revenue, 63)
    result = (_b - _b.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_diff_126d_base_v089_signal(revenue, closeadj):
    _b = _f10_long_cycle_growth(revenue, 126)
    result = (_b - _b.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_diff_252d_base_v090_signal(revenue, closeadj):
    _b = _f10_long_cycle_growth(revenue, 252)
    result = (_b - _b.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_logc_5d_base_v091_signal(revenue, closeadj):
    result = _mean(_f10_long_cycle_growth(revenue, 5), 5) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_logc_21d_base_v092_signal(revenue, closeadj):
    result = _mean(_f10_long_cycle_growth(revenue, 21), 21) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_logc_63d_base_v093_signal(revenue, closeadj):
    result = _mean(_f10_long_cycle_growth(revenue, 63), 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_logc_126d_base_v094_signal(revenue, closeadj):
    result = _mean(_f10_long_cycle_growth(revenue, 126), 126) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_logc_252d_base_v095_signal(revenue, closeadj):
    result = _mean(_f10_long_cycle_growth(revenue, 252), 252) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_tanhsig_5d_base_v096_signal(revenue, closeadj):
    _b = _f10_long_cycle_growth(revenue, 5)
    result = np.tanh(_mean(_b, 5)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_tanhsig_21d_base_v097_signal(revenue, closeadj):
    _b = _f10_long_cycle_growth(revenue, 21)
    result = np.tanh(_mean(_b, 21)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_tanhsig_63d_base_v098_signal(revenue, closeadj):
    _b = _f10_long_cycle_growth(revenue, 63)
    result = np.tanh(_mean(_b, 63)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_tanhsig_126d_base_v099_signal(revenue, closeadj):
    _b = _f10_long_cycle_growth(revenue, 126)
    result = np.tanh(_mean(_b, 126)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_tanhsig_252d_base_v100_signal(revenue, closeadj):
    _b = _f10_long_cycle_growth(revenue, 252)
    result = np.tanh(_mean(_b, 252)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_median_5d_base_v101_signal(revenue, closeadj):
    result = (_f10_compounding_quality(revenue, 5)).rolling(5, min_periods=max(1, 5//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_median_21d_base_v102_signal(revenue, closeadj):
    result = (_f10_compounding_quality(revenue, 21)).rolling(21, min_periods=max(1, 21//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_median_63d_base_v103_signal(revenue, closeadj):
    result = (_f10_compounding_quality(revenue, 63)).rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_median_126d_base_v104_signal(revenue, closeadj):
    result = (_f10_compounding_quality(revenue, 126)).rolling(126, min_periods=max(1, 126//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_median_252d_base_v105_signal(revenue, closeadj):
    result = (_f10_compounding_quality(revenue, 252)).rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_rank_5d_base_v106_signal(revenue, closeadj):
    result = (_f10_compounding_quality(revenue, 5)).rolling(5, min_periods=max(1, 5//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_rank_21d_base_v107_signal(revenue, closeadj):
    result = (_f10_compounding_quality(revenue, 21)).rolling(21, min_periods=max(1, 21//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_rank_63d_base_v108_signal(revenue, closeadj):
    result = (_f10_compounding_quality(revenue, 63)).rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_rank_126d_base_v109_signal(revenue, closeadj):
    result = (_f10_compounding_quality(revenue, 126)).rolling(126, min_periods=max(1, 126//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_rank_252d_base_v110_signal(revenue, closeadj):
    result = (_f10_compounding_quality(revenue, 252)).rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_diff_5d_base_v111_signal(revenue, closeadj):
    _b = _f10_compounding_quality(revenue, 5)
    result = (_b - _b.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_diff_21d_base_v112_signal(revenue, closeadj):
    _b = _f10_compounding_quality(revenue, 21)
    result = (_b - _b.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_diff_63d_base_v113_signal(revenue, closeadj):
    _b = _f10_compounding_quality(revenue, 63)
    result = (_b - _b.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_diff_126d_base_v114_signal(revenue, closeadj):
    _b = _f10_compounding_quality(revenue, 126)
    result = (_b - _b.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_diff_252d_base_v115_signal(revenue, closeadj):
    _b = _f10_compounding_quality(revenue, 252)
    result = (_b - _b.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_logc_5d_base_v116_signal(revenue, closeadj):
    result = _mean(_f10_compounding_quality(revenue, 5), 5) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_logc_21d_base_v117_signal(revenue, closeadj):
    result = _mean(_f10_compounding_quality(revenue, 21), 21) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_logc_63d_base_v118_signal(revenue, closeadj):
    result = _mean(_f10_compounding_quality(revenue, 63), 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_logc_126d_base_v119_signal(revenue, closeadj):
    result = _mean(_f10_compounding_quality(revenue, 126), 126) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_logc_252d_base_v120_signal(revenue, closeadj):
    result = _mean(_f10_compounding_quality(revenue, 252), 252) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_tanhsig_5d_base_v121_signal(revenue, closeadj):
    _b = _f10_compounding_quality(revenue, 5)
    result = np.tanh(_mean(_b, 5)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_tanhsig_21d_base_v122_signal(revenue, closeadj):
    _b = _f10_compounding_quality(revenue, 21)
    result = np.tanh(_mean(_b, 21)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_tanhsig_63d_base_v123_signal(revenue, closeadj):
    _b = _f10_compounding_quality(revenue, 63)
    result = np.tanh(_mean(_b, 63)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_tanhsig_126d_base_v124_signal(revenue, closeadj):
    _b = _f10_compounding_quality(revenue, 126)
    result = np.tanh(_mean(_b, 126)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_tanhsig_252d_base_v125_signal(revenue, closeadj):
    _b = _f10_compounding_quality(revenue, 252)
    result = np.tanh(_mean(_b, 252)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_median_5d_base_v126_signal(revenue, ebitda, closeadj):
    result = (_f10_revenue_compound(revenue, ebitda, 5)).rolling(5, min_periods=max(1, 5//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_median_21d_base_v127_signal(revenue, ebitda, closeadj):
    result = (_f10_revenue_compound(revenue, ebitda, 21)).rolling(21, min_periods=max(1, 21//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_median_63d_base_v128_signal(revenue, ebitda, closeadj):
    result = (_f10_revenue_compound(revenue, ebitda, 63)).rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_median_126d_base_v129_signal(revenue, ebitda, closeadj):
    result = (_f10_revenue_compound(revenue, ebitda, 126)).rolling(126, min_periods=max(1, 126//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_median_252d_base_v130_signal(revenue, ebitda, closeadj):
    result = (_f10_revenue_compound(revenue, ebitda, 252)).rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_rank_5d_base_v131_signal(revenue, ebitda, closeadj):
    result = (_f10_revenue_compound(revenue, ebitda, 5)).rolling(5, min_periods=max(1, 5//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_rank_21d_base_v132_signal(revenue, ebitda, closeadj):
    result = (_f10_revenue_compound(revenue, ebitda, 21)).rolling(21, min_periods=max(1, 21//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_rank_63d_base_v133_signal(revenue, ebitda, closeadj):
    result = (_f10_revenue_compound(revenue, ebitda, 63)).rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_rank_126d_base_v134_signal(revenue, ebitda, closeadj):
    result = (_f10_revenue_compound(revenue, ebitda, 126)).rolling(126, min_periods=max(1, 126//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_rank_252d_base_v135_signal(revenue, ebitda, closeadj):
    result = (_f10_revenue_compound(revenue, ebitda, 252)).rolling(252, min_periods=max(1, 252//2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_diff_5d_base_v136_signal(revenue, ebitda, closeadj):
    _b = _f10_revenue_compound(revenue, ebitda, 5)
    result = (_b - _b.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_diff_21d_base_v137_signal(revenue, ebitda, closeadj):
    _b = _f10_revenue_compound(revenue, ebitda, 21)
    result = (_b - _b.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_diff_63d_base_v138_signal(revenue, ebitda, closeadj):
    _b = _f10_revenue_compound(revenue, ebitda, 63)
    result = (_b - _b.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_diff_126d_base_v139_signal(revenue, ebitda, closeadj):
    _b = _f10_revenue_compound(revenue, ebitda, 126)
    result = (_b - _b.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_diff_252d_base_v140_signal(revenue, ebitda, closeadj):
    _b = _f10_revenue_compound(revenue, ebitda, 252)
    result = (_b - _b.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_logc_5d_base_v141_signal(revenue, ebitda, closeadj):
    result = _mean(_f10_revenue_compound(revenue, ebitda, 5), 5) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_logc_21d_base_v142_signal(revenue, ebitda, closeadj):
    result = _mean(_f10_revenue_compound(revenue, ebitda, 21), 21) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_logc_63d_base_v143_signal(revenue, ebitda, closeadj):
    result = _mean(_f10_revenue_compound(revenue, ebitda, 63), 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_logc_126d_base_v144_signal(revenue, ebitda, closeadj):
    result = _mean(_f10_revenue_compound(revenue, ebitda, 126), 126) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_logc_252d_base_v145_signal(revenue, ebitda, closeadj):
    result = _mean(_f10_revenue_compound(revenue, ebitda, 252), 252) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_tanhsig_5d_base_v146_signal(revenue, ebitda, closeadj):
    _b = _f10_revenue_compound(revenue, ebitda, 5)
    result = np.tanh(_mean(_b, 5)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_tanhsig_21d_base_v147_signal(revenue, ebitda, closeadj):
    _b = _f10_revenue_compound(revenue, ebitda, 21)
    result = np.tanh(_mean(_b, 21)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_tanhsig_63d_base_v148_signal(revenue, ebitda, closeadj):
    _b = _f10_revenue_compound(revenue, ebitda, 63)
    result = np.tanh(_mean(_b, 63)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_tanhsig_126d_base_v149_signal(revenue, ebitda, closeadj):
    _b = _f10_revenue_compound(revenue, ebitda, 126)
    result = np.tanh(_mean(_b, 126)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_tanhsig_252d_base_v150_signal(revenue, ebitda, closeadj):
    _b = _f10_revenue_compound(revenue, ebitda, 252)
    result = np.tanh(_mean(_b, 252)) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f10urg_f10_utility_regulated_growth_longg_median_5d_base_v076_signal,
    f10urg_f10_utility_regulated_growth_longg_median_21d_base_v077_signal,
    f10urg_f10_utility_regulated_growth_longg_median_63d_base_v078_signal,
    f10urg_f10_utility_regulated_growth_longg_median_126d_base_v079_signal,
    f10urg_f10_utility_regulated_growth_longg_median_252d_base_v080_signal,
    f10urg_f10_utility_regulated_growth_longg_rank_5d_base_v081_signal,
    f10urg_f10_utility_regulated_growth_longg_rank_21d_base_v082_signal,
    f10urg_f10_utility_regulated_growth_longg_rank_63d_base_v083_signal,
    f10urg_f10_utility_regulated_growth_longg_rank_126d_base_v084_signal,
    f10urg_f10_utility_regulated_growth_longg_rank_252d_base_v085_signal,
    f10urg_f10_utility_regulated_growth_longg_diff_5d_base_v086_signal,
    f10urg_f10_utility_regulated_growth_longg_diff_21d_base_v087_signal,
    f10urg_f10_utility_regulated_growth_longg_diff_63d_base_v088_signal,
    f10urg_f10_utility_regulated_growth_longg_diff_126d_base_v089_signal,
    f10urg_f10_utility_regulated_growth_longg_diff_252d_base_v090_signal,
    f10urg_f10_utility_regulated_growth_longg_logc_5d_base_v091_signal,
    f10urg_f10_utility_regulated_growth_longg_logc_21d_base_v092_signal,
    f10urg_f10_utility_regulated_growth_longg_logc_63d_base_v093_signal,
    f10urg_f10_utility_regulated_growth_longg_logc_126d_base_v094_signal,
    f10urg_f10_utility_regulated_growth_longg_logc_252d_base_v095_signal,
    f10urg_f10_utility_regulated_growth_longg_tanhsig_5d_base_v096_signal,
    f10urg_f10_utility_regulated_growth_longg_tanhsig_21d_base_v097_signal,
    f10urg_f10_utility_regulated_growth_longg_tanhsig_63d_base_v098_signal,
    f10urg_f10_utility_regulated_growth_longg_tanhsig_126d_base_v099_signal,
    f10urg_f10_utility_regulated_growth_longg_tanhsig_252d_base_v100_signal,
    f10urg_f10_utility_regulated_growth_compq_median_5d_base_v101_signal,
    f10urg_f10_utility_regulated_growth_compq_median_21d_base_v102_signal,
    f10urg_f10_utility_regulated_growth_compq_median_63d_base_v103_signal,
    f10urg_f10_utility_regulated_growth_compq_median_126d_base_v104_signal,
    f10urg_f10_utility_regulated_growth_compq_median_252d_base_v105_signal,
    f10urg_f10_utility_regulated_growth_compq_rank_5d_base_v106_signal,
    f10urg_f10_utility_regulated_growth_compq_rank_21d_base_v107_signal,
    f10urg_f10_utility_regulated_growth_compq_rank_63d_base_v108_signal,
    f10urg_f10_utility_regulated_growth_compq_rank_126d_base_v109_signal,
    f10urg_f10_utility_regulated_growth_compq_rank_252d_base_v110_signal,
    f10urg_f10_utility_regulated_growth_compq_diff_5d_base_v111_signal,
    f10urg_f10_utility_regulated_growth_compq_diff_21d_base_v112_signal,
    f10urg_f10_utility_regulated_growth_compq_diff_63d_base_v113_signal,
    f10urg_f10_utility_regulated_growth_compq_diff_126d_base_v114_signal,
    f10urg_f10_utility_regulated_growth_compq_diff_252d_base_v115_signal,
    f10urg_f10_utility_regulated_growth_compq_logc_5d_base_v116_signal,
    f10urg_f10_utility_regulated_growth_compq_logc_21d_base_v117_signal,
    f10urg_f10_utility_regulated_growth_compq_logc_63d_base_v118_signal,
    f10urg_f10_utility_regulated_growth_compq_logc_126d_base_v119_signal,
    f10urg_f10_utility_regulated_growth_compq_logc_252d_base_v120_signal,
    f10urg_f10_utility_regulated_growth_compq_tanhsig_5d_base_v121_signal,
    f10urg_f10_utility_regulated_growth_compq_tanhsig_21d_base_v122_signal,
    f10urg_f10_utility_regulated_growth_compq_tanhsig_63d_base_v123_signal,
    f10urg_f10_utility_regulated_growth_compq_tanhsig_126d_base_v124_signal,
    f10urg_f10_utility_regulated_growth_compq_tanhsig_252d_base_v125_signal,
    f10urg_f10_utility_regulated_growth_revcomp_median_5d_base_v126_signal,
    f10urg_f10_utility_regulated_growth_revcomp_median_21d_base_v127_signal,
    f10urg_f10_utility_regulated_growth_revcomp_median_63d_base_v128_signal,
    f10urg_f10_utility_regulated_growth_revcomp_median_126d_base_v129_signal,
    f10urg_f10_utility_regulated_growth_revcomp_median_252d_base_v130_signal,
    f10urg_f10_utility_regulated_growth_revcomp_rank_5d_base_v131_signal,
    f10urg_f10_utility_regulated_growth_revcomp_rank_21d_base_v132_signal,
    f10urg_f10_utility_regulated_growth_revcomp_rank_63d_base_v133_signal,
    f10urg_f10_utility_regulated_growth_revcomp_rank_126d_base_v134_signal,
    f10urg_f10_utility_regulated_growth_revcomp_rank_252d_base_v135_signal,
    f10urg_f10_utility_regulated_growth_revcomp_diff_5d_base_v136_signal,
    f10urg_f10_utility_regulated_growth_revcomp_diff_21d_base_v137_signal,
    f10urg_f10_utility_regulated_growth_revcomp_diff_63d_base_v138_signal,
    f10urg_f10_utility_regulated_growth_revcomp_diff_126d_base_v139_signal,
    f10urg_f10_utility_regulated_growth_revcomp_diff_252d_base_v140_signal,
    f10urg_f10_utility_regulated_growth_revcomp_logc_5d_base_v141_signal,
    f10urg_f10_utility_regulated_growth_revcomp_logc_21d_base_v142_signal,
    f10urg_f10_utility_regulated_growth_revcomp_logc_63d_base_v143_signal,
    f10urg_f10_utility_regulated_growth_revcomp_logc_126d_base_v144_signal,
    f10urg_f10_utility_regulated_growth_revcomp_logc_252d_base_v145_signal,
    f10urg_f10_utility_regulated_growth_revcomp_tanhsig_5d_base_v146_signal,
    f10urg_f10_utility_regulated_growth_revcomp_tanhsig_21d_base_v147_signal,
    f10urg_f10_utility_regulated_growth_revcomp_tanhsig_63d_base_v148_signal,
    f10urg_f10_utility_regulated_growth_revcomp_tanhsig_126d_base_v149_signal,
    f10urg_f10_utility_regulated_growth_revcomp_tanhsig_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_UTILITY_REGULATED_GROWTH_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "ebitda": ebitda,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f10_long_cycle_growth", "_f10_compounding_quality", "_f10_revenue_compound",)
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
    print(f"OK f10_utility_regulated_growth_base_076_150_claude: {n_features} features pass")
