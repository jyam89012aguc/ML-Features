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
def _f50_quality_composite(roic, fcf, revenue, w):
    rq = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    fy = fcf / revenue.replace(0, np.nan)
    fy_m = fy.rolling(w, min_periods=max(1, w // 2)).mean()
    return rq + fy_m


def _f50_idiosyncratic_signal(closeadj, revenue, w):
    pr = closeadj.pct_change(w)
    rg = revenue.pct_change(w)
    return pr - rg


def _f50_alpha_score(roic, ebitdamargin, w):
    rq = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    em = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return rq * em


# ===== features =====
def f50ria_f50_renewable_idiosyncratic_alpha_as_re_84d_s01_base_v076_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 84)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_84d_s01_base_v077_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 84)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_84d_s01_base_v078_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 84)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_84d_s01_base_v079_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 84)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_105d_s01_base_v080_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 105)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_105d_s01_base_v081_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 105)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_105d_s01_base_v082_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 105)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_105d_s01_base_v083_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 105)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_105d_s01_base_v084_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 105)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_105d_s01_base_v085_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 105)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_105d_s01_base_v086_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 105)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_105d_s01_base_v087_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 105)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_105d_s01_base_v088_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 105)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_105d_s01_base_v089_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 105)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_105d_s01_base_v090_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 105)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_105d_s01_base_v091_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 105)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_105d_s01_base_v092_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 105)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_105d_s01_base_v093_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 105)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_105d_s01_base_v094_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 105)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_105d_s01_base_v095_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 105)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_105d_s01_base_v096_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 105)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_105d_s01_base_v097_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 105)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_105d_s01_base_v098_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 105)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_105d_s01_base_v099_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 105)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_105d_s01_base_v100_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 105)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_105d_s01_base_v101_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 105)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_105d_s01_base_v102_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 105)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_105d_s01_base_v103_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 105)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_126d_s01_base_v104_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_126d_s01_base_v105_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_126d_s01_base_v106_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_126d_s01_base_v107_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_126d_s01_base_v108_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_126d_s01_base_v109_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_126d_s01_base_v110_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_126d_s01_base_v111_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_126d_s01_base_v112_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 126)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_126d_s01_base_v113_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 126)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_126d_s01_base_v114_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_126d_s01_base_v115_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 126)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_126d_s01_base_v116_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 126)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_126d_s01_base_v117_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 126)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_126d_s01_base_v118_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 126)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_126d_s01_base_v119_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 126)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_126d_s01_base_v120_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 126)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_126d_s01_base_v121_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 126)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_126d_s01_base_v122_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_126d_s01_base_v123_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 126)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_126d_s01_base_v124_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 126)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_126d_s01_base_v125_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 126)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_126d_s01_base_v126_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 126)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_126d_s01_base_v127_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 126)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_147d_s01_base_v128_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 147)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_147d_s01_base_v129_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 147)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_147d_s01_base_v130_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 147)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_147d_s01_base_v131_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 147)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_147d_s01_base_v132_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 147)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_147d_s01_base_v133_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 147)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_147d_s01_base_v134_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 147)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_147d_s01_base_v135_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 147)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_147d_s01_base_v136_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 147)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_147d_s01_base_v137_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 147)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_147d_s01_base_v138_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 147)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_147d_s01_base_v139_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 147)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_147d_s01_base_v140_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 147)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_147d_s01_base_v141_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 147)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_147d_s01_base_v142_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 147)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_147d_s01_base_v143_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 147)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_147d_s01_base_v144_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 147)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_147d_s01_base_v145_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 147)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_147d_s01_base_v146_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 147)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_147d_s01_base_v147_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 147)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_147d_s01_base_v148_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 147)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_147d_s01_base_v149_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 147)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_147d_s01_base_v150_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 147)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_84d_s01_base_v076_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_84d_s01_base_v077_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_84d_s01_base_v078_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_84d_s01_base_v079_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_105d_s01_base_v080_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_105d_s01_base_v081_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_105d_s01_base_v082_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_105d_s01_base_v083_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_105d_s01_base_v084_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_105d_s01_base_v085_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_105d_s01_base_v086_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_105d_s01_base_v087_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_105d_s01_base_v088_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_105d_s01_base_v089_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_105d_s01_base_v090_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_105d_s01_base_v091_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_105d_s01_base_v092_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_105d_s01_base_v093_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_105d_s01_base_v094_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_105d_s01_base_v095_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_105d_s01_base_v096_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_105d_s01_base_v097_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_105d_s01_base_v098_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_105d_s01_base_v099_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_105d_s01_base_v100_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_105d_s01_base_v101_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_105d_s01_base_v102_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_105d_s01_base_v103_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_126d_s01_base_v104_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_126d_s01_base_v105_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_126d_s01_base_v106_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_126d_s01_base_v107_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_126d_s01_base_v108_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_126d_s01_base_v109_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_126d_s01_base_v110_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_126d_s01_base_v111_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_126d_s01_base_v112_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_126d_s01_base_v113_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_126d_s01_base_v114_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_126d_s01_base_v115_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_126d_s01_base_v116_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_126d_s01_base_v117_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_126d_s01_base_v118_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_126d_s01_base_v119_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_126d_s01_base_v120_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_126d_s01_base_v121_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_126d_s01_base_v122_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_126d_s01_base_v123_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_126d_s01_base_v124_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_126d_s01_base_v125_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_126d_s01_base_v126_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_126d_s01_base_v127_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_147d_s01_base_v128_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_147d_s01_base_v129_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_147d_s01_base_v130_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_147d_s01_base_v131_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_147d_s01_base_v132_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_147d_s01_base_v133_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_147d_s01_base_v134_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_147d_s01_base_v135_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_147d_s01_base_v136_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_147d_s01_base_v137_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_147d_s01_base_v138_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_147d_s01_base_v139_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_147d_s01_base_v140_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_147d_s01_base_v141_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_147d_s01_base_v142_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_147d_s01_base_v143_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_147d_s01_base_v144_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_147d_s01_base_v145_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_147d_s01_base_v146_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_147d_s01_base_v147_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_147d_s01_base_v148_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_147d_s01_base_v149_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_147d_s01_base_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F50_RENEWABLE_IDIOSYNCRATIC_ALPHA_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    roic    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    cols = {"closeadj": closeadj, "ebitdamargin": ebitdamargin, "fcf": fcf, "revenue": revenue, "roic": roic}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f50_quality_composite", "_f50_idiosyncratic_signal", "_f50_alpha_score",)
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
    print(f"OK f50_renewable_idiosyncratic_alpha_base_076_150_claude: {n_features} features pass")
