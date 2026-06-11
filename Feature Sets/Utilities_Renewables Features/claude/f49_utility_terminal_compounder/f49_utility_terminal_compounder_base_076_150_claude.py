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


# ===== folder domain primitives =====
def _f49_quality_composite(roic, fcf, revenue, w):
    rq = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    fy = fcf / revenue.replace(0, np.nan)
    fy_m = fy.rolling(w, min_periods=max(1, w // 2)).mean()
    return rq * fy_m


def _f49_compounder_score(roic, ebitdamargin, w):
    rq = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    eq = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return rq + eq


def _f49_terminal_quality(fcf, revenue, dps, w):
    fg = fcf.rolling(w, min_periods=max(1, w // 2)).mean()
    rg = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    dg = dps.rolling(w, min_periods=max(1, w // 2)).mean()
    return (fg / rg.replace(0, np.nan)) * dg


# ===== features =====
def f49utc_f49_utility_terminal_compounder_tq_frd_84d_s01_base_v076_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 84)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_84d_s01_base_v077_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 84)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_84d_s01_base_v078_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 84)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_84d_s01_base_v079_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 84)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_105d_s01_base_v080_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 105)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_105d_s01_base_v081_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 105)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_105d_s01_base_v082_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 105)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_105d_s01_base_v083_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 105)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_105d_s01_base_v084_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 105)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_105d_s01_base_v085_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 105)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_105d_s01_base_v086_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 105)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_105d_s01_base_v087_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 105)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_105d_s01_base_v088_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 105)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_105d_s01_base_v089_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 105)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_105d_s01_base_v090_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 105)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_105d_s01_base_v091_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 105)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_105d_s01_base_v092_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 105)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_105d_s01_base_v093_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 105)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_105d_s01_base_v094_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 105)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_105d_s01_base_v095_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 105)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_105d_s01_base_v096_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 105)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_105d_s01_base_v097_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 105)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_105d_s01_base_v098_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 105)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_105d_s01_base_v099_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 105)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_105d_s01_base_v100_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 105)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_105d_s01_base_v101_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 105)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_105d_s01_base_v102_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 105)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_105d_s01_base_v103_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 105)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_126d_s01_base_v104_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 126)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_126d_s01_base_v105_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 126)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_126d_s01_base_v106_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_126d_s01_base_v107_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 126)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_126d_s01_base_v108_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 126)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_126d_s01_base_v109_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 126)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_126d_s01_base_v110_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 126)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_126d_s01_base_v111_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 126)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_126d_s01_base_v112_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 126)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_126d_s01_base_v113_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 126)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_126d_s01_base_v114_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_126d_s01_base_v115_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 126)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_126d_s01_base_v116_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 126)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_126d_s01_base_v117_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 126)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_126d_s01_base_v118_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 126)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_126d_s01_base_v119_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 126)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_126d_s01_base_v120_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 126)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_126d_s01_base_v121_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 126)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_126d_s01_base_v122_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_126d_s01_base_v123_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 126)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_126d_s01_base_v124_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 126)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_126d_s01_base_v125_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 126)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_126d_s01_base_v126_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 126)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_126d_s01_base_v127_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 126)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_147d_s01_base_v128_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 147)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_147d_s01_base_v129_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 147)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_147d_s01_base_v130_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 147)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_147d_s01_base_v131_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 147)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_147d_s01_base_v132_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 147)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_147d_s01_base_v133_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 147)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_147d_s01_base_v134_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 147)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_147d_s01_base_v135_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 147)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_147d_s01_base_v136_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 147)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_147d_s01_base_v137_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 147)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_147d_s01_base_v138_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 147)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_147d_s01_base_v139_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 147)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_147d_s01_base_v140_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 147)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_147d_s01_base_v141_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 147)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_147d_s01_base_v142_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 147)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_147d_s01_base_v143_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 147)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_147d_s01_base_v144_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 147)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_147d_s01_base_v145_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 147)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_147d_s01_base_v146_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 147)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_147d_s01_base_v147_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 147)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_147d_s01_base_v148_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 147)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_147d_s01_base_v149_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 147)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_147d_s01_base_v150_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 147)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f49utc_f49_utility_terminal_compounder_tq_frd_84d_s01_base_v076_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_84d_s01_base_v077_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_84d_s01_base_v078_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_84d_s01_base_v079_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_105d_s01_base_v080_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_105d_s01_base_v081_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_105d_s01_base_v082_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_105d_s01_base_v083_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_105d_s01_base_v084_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_105d_s01_base_v085_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_105d_s01_base_v086_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_105d_s01_base_v087_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_105d_s01_base_v088_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_105d_s01_base_v089_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_105d_s01_base_v090_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_105d_s01_base_v091_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_105d_s01_base_v092_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_105d_s01_base_v093_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_105d_s01_base_v094_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_105d_s01_base_v095_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_105d_s01_base_v096_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_105d_s01_base_v097_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_105d_s01_base_v098_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_105d_s01_base_v099_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_105d_s01_base_v100_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_105d_s01_base_v101_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_105d_s01_base_v102_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_105d_s01_base_v103_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_126d_s01_base_v104_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_126d_s01_base_v105_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_126d_s01_base_v106_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_126d_s01_base_v107_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_126d_s01_base_v108_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_126d_s01_base_v109_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_126d_s01_base_v110_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_126d_s01_base_v111_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_126d_s01_base_v112_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_126d_s01_base_v113_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_126d_s01_base_v114_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_126d_s01_base_v115_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_126d_s01_base_v116_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_126d_s01_base_v117_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_126d_s01_base_v118_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_126d_s01_base_v119_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_126d_s01_base_v120_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_126d_s01_base_v121_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_126d_s01_base_v122_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_126d_s01_base_v123_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_126d_s01_base_v124_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_126d_s01_base_v125_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_126d_s01_base_v126_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_126d_s01_base_v127_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_147d_s01_base_v128_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_147d_s01_base_v129_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_147d_s01_base_v130_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_147d_s01_base_v131_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_147d_s01_base_v132_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_147d_s01_base_v133_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_147d_s01_base_v134_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_147d_s01_base_v135_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_147d_s01_base_v136_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_147d_s01_base_v137_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_147d_s01_base_v138_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_147d_s01_base_v139_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_147d_s01_base_v140_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_147d_s01_base_v141_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_147d_s01_base_v142_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_147d_s01_base_v143_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_147d_s01_base_v144_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_147d_s01_base_v145_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_147d_s01_base_v146_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_147d_s01_base_v147_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_147d_s01_base_v148_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_147d_s01_base_v149_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_147d_s01_base_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F49_UTILITY_TERMINAL_COMPOUNDER_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    dps     = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    roic    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    cols = {"closeadj": closeadj, "dps": dps, "ebitdamargin": ebitdamargin, "fcf": fcf, "revenue": revenue, "roic": roic}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f49_quality_composite", "_f49_compounder_score", "_f49_terminal_quality",)
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
    print(f"OK f49_utility_terminal_compounder_base_076_150_claude: {n_features} features pass")
