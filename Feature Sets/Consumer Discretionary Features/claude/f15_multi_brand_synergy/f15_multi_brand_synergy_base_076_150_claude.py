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


# ===== folder domain primitives =====

def _f15_revenue_compound(revenue, w):
    return revenue.pct_change(periods=w)


def _f15_compounding_smoothness(revenue, ebitda, w):
    rg = revenue.pct_change(periods=w)
    eg = ebitda.pct_change(periods=w)
    rgsd = rg.rolling(w, min_periods=max(1, w // 2)).std()
    return (rg + eg) / rgsd.replace(0, np.nan)


def _f15_synergy_score(revenue, ebitdamargin, w):
    rg = revenue.pct_change(periods=w)
    em = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    emsd = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return rg * em / emsd.replace(0, np.nan)


# ===== features =====

def f15mbs_f15_multi_brand_synergy_cs_sclose_378d_base_v076_signal(revenue, ebitda, closeadj):
    result = _f15_compounding_smoothness(revenue, ebitda, 378) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_xclose_504d_base_v077_signal(revenue, ebitda, closeadj):
    result = _f15_compounding_smoothness(revenue, ebitda, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_zclose_504d_base_v078_signal(revenue, ebitda, closeadj):
    result = _f15_compounding_smoothness(revenue, ebitda, 504) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_mclose_504d_base_v079_signal(revenue, ebitda, closeadj):
    result = _f15_compounding_smoothness(revenue, ebitda, 504) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_sclose_504d_base_v080_signal(revenue, ebitda, closeadj):
    result = _f15_compounding_smoothness(revenue, ebitda, 504) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_xclose_5d_base_v081_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_zclose_5d_base_v082_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_mclose_5d_base_v083_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_sclose_5d_base_v084_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_xclose_10d_base_v085_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_zclose_10d_base_v086_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_mclose_10d_base_v087_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_sclose_10d_base_v088_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_xclose_21d_base_v089_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_zclose_21d_base_v090_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_mclose_21d_base_v091_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_sclose_21d_base_v092_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_xclose_42d_base_v093_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_zclose_42d_base_v094_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_mclose_42d_base_v095_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_sclose_42d_base_v096_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_xclose_63d_base_v097_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_zclose_63d_base_v098_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_mclose_63d_base_v099_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_sclose_63d_base_v100_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_xclose_126d_base_v101_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_zclose_126d_base_v102_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 126) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_mclose_126d_base_v103_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 126) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_sclose_126d_base_v104_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_xclose_189d_base_v105_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_zclose_189d_base_v106_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 189) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_mclose_189d_base_v107_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 189) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_sclose_189d_base_v108_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 189) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_xclose_252d_base_v109_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_zclose_252d_base_v110_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 252) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_mclose_252d_base_v111_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 252) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_sclose_252d_base_v112_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 252) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_xclose_378d_base_v113_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_zclose_378d_base_v114_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 378) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_mclose_378d_base_v115_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 378) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_sclose_378d_base_v116_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 378) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_xclose_504d_base_v117_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_zclose_504d_base_v118_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 504) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_mclose_504d_base_v119_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 504) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_sclose_504d_base_v120_signal(revenue, ebitdamargin, closeadj):
    result = _f15_synergy_score(revenue, ebitdamargin, 504) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rcm0_21d_base_v121_signal(revenue, closeadj):
    result = _mean(_f15_revenue_compound(revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rcm1_42d_base_v122_signal(revenue, closeadj):
    result = _mean(_f15_revenue_compound(revenue, 42), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rcm2_63d_base_v123_signal(revenue, closeadj):
    result = _mean(_f15_revenue_compound(revenue, 63), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rcm3_126d_base_v124_signal(revenue, closeadj):
    result = _mean(_f15_revenue_compound(revenue, 126), 21) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rcm4_189d_base_v125_signal(revenue, closeadj):
    result = _mean(_f15_revenue_compound(revenue, 189), 21) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rcm5_252d_base_v126_signal(revenue, closeadj):
    result = _mean(_f15_revenue_compound(revenue, 252), 21) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rcm6_378d_base_v127_signal(revenue, closeadj):
    result = _mean(_f15_revenue_compound(revenue, 378), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rcm7_504d_base_v128_signal(revenue, closeadj):
    result = _mean(_f15_revenue_compound(revenue, 504), 21) * (closeadj - _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rcm8_10d_base_v129_signal(revenue, closeadj):
    result = _mean(_f15_revenue_compound(revenue, 10), 21) * (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rcm9_5d_base_v130_signal(revenue, closeadj):
    result = _mean(_f15_revenue_compound(revenue, 5), 21) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rcz0_21d_base_v131_signal(revenue, closeadj):
    result = _z(_f15_revenue_compound(revenue, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rcz1_42d_base_v132_signal(revenue, closeadj):
    result = _z(_f15_revenue_compound(revenue, 42), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rcz2_63d_base_v133_signal(revenue, closeadj):
    result = _z(_f15_revenue_compound(revenue, 63), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rcz3_126d_base_v134_signal(revenue, closeadj):
    result = _z(_f15_revenue_compound(revenue, 126), 63) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rcz4_189d_base_v135_signal(revenue, closeadj):
    result = _z(_f15_revenue_compound(revenue, 189), 63) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rcz5_252d_base_v136_signal(revenue, closeadj):
    result = _z(_f15_revenue_compound(revenue, 252), 63) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rcz6_378d_base_v137_signal(revenue, closeadj):
    result = _z(_f15_revenue_compound(revenue, 378), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rcz7_504d_base_v138_signal(revenue, closeadj):
    result = _z(_f15_revenue_compound(revenue, 504), 63) * (closeadj - _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rcz8_10d_base_v139_signal(revenue, closeadj):
    result = _z(_f15_revenue_compound(revenue, 10), 63) * (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rcz9_5d_base_v140_signal(revenue, closeadj):
    result = _z(_f15_revenue_compound(revenue, 5), 63) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ssm0_21d_base_v141_signal(revenue, ebitdamargin, closeadj):
    result = _mean(_f15_synergy_score(revenue, ebitdamargin, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ssm1_42d_base_v142_signal(revenue, ebitdamargin, closeadj):
    result = _mean(_f15_synergy_score(revenue, ebitdamargin, 42), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ssm2_63d_base_v143_signal(revenue, ebitdamargin, closeadj):
    result = _mean(_f15_synergy_score(revenue, ebitdamargin, 63), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ssm3_126d_base_v144_signal(revenue, ebitdamargin, closeadj):
    result = _mean(_f15_synergy_score(revenue, ebitdamargin, 126), 21) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ssm4_189d_base_v145_signal(revenue, ebitdamargin, closeadj):
    result = _mean(_f15_synergy_score(revenue, ebitdamargin, 189), 21) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ssm5_252d_base_v146_signal(revenue, ebitdamargin, closeadj):
    result = _mean(_f15_synergy_score(revenue, ebitdamargin, 252), 21) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ssm6_378d_base_v147_signal(revenue, ebitdamargin, closeadj):
    result = _mean(_f15_synergy_score(revenue, ebitdamargin, 378), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ssm7_504d_base_v148_signal(revenue, ebitdamargin, closeadj):
    result = _mean(_f15_synergy_score(revenue, ebitdamargin, 504), 21) * (closeadj - _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ssm8_10d_base_v149_signal(revenue, ebitdamargin, closeadj):
    result = _mean(_f15_synergy_score(revenue, ebitdamargin, 10), 21) * (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ssm9_5d_base_v150_signal(revenue, ebitdamargin, closeadj):
    result = _mean(_f15_synergy_score(revenue, ebitdamargin, 5), 21) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f15mbs_f15_multi_brand_synergy_cs_sclose_378d_base_v076_signal,
    f15mbs_f15_multi_brand_synergy_cs_xclose_504d_base_v077_signal,
    f15mbs_f15_multi_brand_synergy_cs_zclose_504d_base_v078_signal,
    f15mbs_f15_multi_brand_synergy_cs_mclose_504d_base_v079_signal,
    f15mbs_f15_multi_brand_synergy_cs_sclose_504d_base_v080_signal,
    f15mbs_f15_multi_brand_synergy_ss_xclose_5d_base_v081_signal,
    f15mbs_f15_multi_brand_synergy_ss_zclose_5d_base_v082_signal,
    f15mbs_f15_multi_brand_synergy_ss_mclose_5d_base_v083_signal,
    f15mbs_f15_multi_brand_synergy_ss_sclose_5d_base_v084_signal,
    f15mbs_f15_multi_brand_synergy_ss_xclose_10d_base_v085_signal,
    f15mbs_f15_multi_brand_synergy_ss_zclose_10d_base_v086_signal,
    f15mbs_f15_multi_brand_synergy_ss_mclose_10d_base_v087_signal,
    f15mbs_f15_multi_brand_synergy_ss_sclose_10d_base_v088_signal,
    f15mbs_f15_multi_brand_synergy_ss_xclose_21d_base_v089_signal,
    f15mbs_f15_multi_brand_synergy_ss_zclose_21d_base_v090_signal,
    f15mbs_f15_multi_brand_synergy_ss_mclose_21d_base_v091_signal,
    f15mbs_f15_multi_brand_synergy_ss_sclose_21d_base_v092_signal,
    f15mbs_f15_multi_brand_synergy_ss_xclose_42d_base_v093_signal,
    f15mbs_f15_multi_brand_synergy_ss_zclose_42d_base_v094_signal,
    f15mbs_f15_multi_brand_synergy_ss_mclose_42d_base_v095_signal,
    f15mbs_f15_multi_brand_synergy_ss_sclose_42d_base_v096_signal,
    f15mbs_f15_multi_brand_synergy_ss_xclose_63d_base_v097_signal,
    f15mbs_f15_multi_brand_synergy_ss_zclose_63d_base_v098_signal,
    f15mbs_f15_multi_brand_synergy_ss_mclose_63d_base_v099_signal,
    f15mbs_f15_multi_brand_synergy_ss_sclose_63d_base_v100_signal,
    f15mbs_f15_multi_brand_synergy_ss_xclose_126d_base_v101_signal,
    f15mbs_f15_multi_brand_synergy_ss_zclose_126d_base_v102_signal,
    f15mbs_f15_multi_brand_synergy_ss_mclose_126d_base_v103_signal,
    f15mbs_f15_multi_brand_synergy_ss_sclose_126d_base_v104_signal,
    f15mbs_f15_multi_brand_synergy_ss_xclose_189d_base_v105_signal,
    f15mbs_f15_multi_brand_synergy_ss_zclose_189d_base_v106_signal,
    f15mbs_f15_multi_brand_synergy_ss_mclose_189d_base_v107_signal,
    f15mbs_f15_multi_brand_synergy_ss_sclose_189d_base_v108_signal,
    f15mbs_f15_multi_brand_synergy_ss_xclose_252d_base_v109_signal,
    f15mbs_f15_multi_brand_synergy_ss_zclose_252d_base_v110_signal,
    f15mbs_f15_multi_brand_synergy_ss_mclose_252d_base_v111_signal,
    f15mbs_f15_multi_brand_synergy_ss_sclose_252d_base_v112_signal,
    f15mbs_f15_multi_brand_synergy_ss_xclose_378d_base_v113_signal,
    f15mbs_f15_multi_brand_synergy_ss_zclose_378d_base_v114_signal,
    f15mbs_f15_multi_brand_synergy_ss_mclose_378d_base_v115_signal,
    f15mbs_f15_multi_brand_synergy_ss_sclose_378d_base_v116_signal,
    f15mbs_f15_multi_brand_synergy_ss_xclose_504d_base_v117_signal,
    f15mbs_f15_multi_brand_synergy_ss_zclose_504d_base_v118_signal,
    f15mbs_f15_multi_brand_synergy_ss_mclose_504d_base_v119_signal,
    f15mbs_f15_multi_brand_synergy_ss_sclose_504d_base_v120_signal,
    f15mbs_f15_multi_brand_synergy_rcm0_21d_base_v121_signal,
    f15mbs_f15_multi_brand_synergy_rcm1_42d_base_v122_signal,
    f15mbs_f15_multi_brand_synergy_rcm2_63d_base_v123_signal,
    f15mbs_f15_multi_brand_synergy_rcm3_126d_base_v124_signal,
    f15mbs_f15_multi_brand_synergy_rcm4_189d_base_v125_signal,
    f15mbs_f15_multi_brand_synergy_rcm5_252d_base_v126_signal,
    f15mbs_f15_multi_brand_synergy_rcm6_378d_base_v127_signal,
    f15mbs_f15_multi_brand_synergy_rcm7_504d_base_v128_signal,
    f15mbs_f15_multi_brand_synergy_rcm8_10d_base_v129_signal,
    f15mbs_f15_multi_brand_synergy_rcm9_5d_base_v130_signal,
    f15mbs_f15_multi_brand_synergy_rcz0_21d_base_v131_signal,
    f15mbs_f15_multi_brand_synergy_rcz1_42d_base_v132_signal,
    f15mbs_f15_multi_brand_synergy_rcz2_63d_base_v133_signal,
    f15mbs_f15_multi_brand_synergy_rcz3_126d_base_v134_signal,
    f15mbs_f15_multi_brand_synergy_rcz4_189d_base_v135_signal,
    f15mbs_f15_multi_brand_synergy_rcz5_252d_base_v136_signal,
    f15mbs_f15_multi_brand_synergy_rcz6_378d_base_v137_signal,
    f15mbs_f15_multi_brand_synergy_rcz7_504d_base_v138_signal,
    f15mbs_f15_multi_brand_synergy_rcz8_10d_base_v139_signal,
    f15mbs_f15_multi_brand_synergy_rcz9_5d_base_v140_signal,
    f15mbs_f15_multi_brand_synergy_ssm0_21d_base_v141_signal,
    f15mbs_f15_multi_brand_synergy_ssm1_42d_base_v142_signal,
    f15mbs_f15_multi_brand_synergy_ssm2_63d_base_v143_signal,
    f15mbs_f15_multi_brand_synergy_ssm3_126d_base_v144_signal,
    f15mbs_f15_multi_brand_synergy_ssm4_189d_base_v145_signal,
    f15mbs_f15_multi_brand_synergy_ssm5_252d_base_v146_signal,
    f15mbs_f15_multi_brand_synergy_ssm6_378d_base_v147_signal,
    f15mbs_f15_multi_brand_synergy_ssm7_504d_base_v148_signal,
    f15mbs_f15_multi_brand_synergy_ssm8_10d_base_v149_signal,
    f15mbs_f15_multi_brand_synergy_ssm9_5d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F15_MULTI_BRAND_SYNERGY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":

    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    assets  = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "ebitda": ebitda, "capex": capex,
        "assets": assets, "ppnenet": ppnenet,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f15_revenue_compound", "_f15_compounding_smoothness", "_f15_synergy_score")
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
    print(f"OK f15_multi_brand_synergy_base_076_150_claude: {n_features} features pass")
