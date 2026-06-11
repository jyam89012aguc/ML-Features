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

def _f37_gm_floor(grossmargin, w):
    floor = grossmargin.rolling(w, min_periods=max(1, w // 2)).min()
    return (grossmargin - floor)


def _f37_gm_consistency(grossmargin, w):
    sd = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    m = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean().abs()
    return 1.0 / (sd / m.replace(0, np.nan)).replace(0, np.nan)


def _f37_gm_quality_score(grossmargin, ebitdamargin, w):
    gm = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    em = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    return (gm * em) / sd.replace(0, np.nan)




def f37hgm_f37_healthcare_gross_margin_quality_cnsdivclose_126d_base_v076_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 126)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsdivclose_189d_base_v077_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 189)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsdivclose_252d_base_v078_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 252)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsdivclose_378d_base_v079_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 378)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_cnsdivclose_504d_base_v080_signal(grossmargin, closeadj):
    base = _f37_gm_consistency(grossmargin, 504)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscdivclose_5d_base_v081_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 5)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscdivclose_10d_base_v082_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 10)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscdivclose_21d_base_v083_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 21)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscdivclose_42d_base_v084_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 42)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscdivclose_63d_base_v085_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 63)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscdivclose_126d_base_v086_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 126)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscdivclose_189d_base_v087_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 189)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscdivclose_252d_base_v088_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 252)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscdivclose_378d_base_v089_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 378)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_qscdivclose_504d_base_v090_signal(grossmargin, ebitdamargin, closeadj):
    base = _f37_gm_quality_score(grossmargin, ebitdamargin, 504)
    result = (base) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_5d5d_base_v091_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 5)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_5d10d_base_v092_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 5)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_5d21d_base_v093_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 5)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_5d42d_base_v094_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 5)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_5d63d_base_v095_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_5d126d_base_v096_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 5)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_5d189d_base_v097_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 5)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_5d252d_base_v098_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 5)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_5d378d_base_v099_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 5)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_5d504d_base_v100_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 5)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_10d5d_base_v101_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 10)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_10d10d_base_v102_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 10)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_10d21d_base_v103_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 10)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_10d42d_base_v104_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 10)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_10d63d_base_v105_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 10)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_10d126d_base_v106_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 10)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_10d189d_base_v107_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 10)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_10d252d_base_v108_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 10)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_10d378d_base_v109_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 10)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_10d504d_base_v110_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 10)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_21d5d_base_v111_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 21)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_21d10d_base_v112_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 21)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_21d21d_base_v113_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_21d42d_base_v114_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 21)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_21d63d_base_v115_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_21d126d_base_v116_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_21d189d_base_v117_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 21)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_21d252d_base_v118_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 21)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_21d378d_base_v119_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 21)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_21d504d_base_v120_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 21)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_42d5d_base_v121_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 42)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_42d10d_base_v122_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 42)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_42d21d_base_v123_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 42)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_42d42d_base_v124_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 42)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_42d63d_base_v125_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 42)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_42d126d_base_v126_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 42)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_42d189d_base_v127_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 42)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_42d252d_base_v128_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 42)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_42d378d_base_v129_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 42)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_42d504d_base_v130_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 42)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_63d5d_base_v131_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 63)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_63d10d_base_v132_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 63)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_63d21d_base_v133_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_63d42d_base_v134_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 63)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_63d63d_base_v135_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_63d126d_base_v136_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_63d189d_base_v137_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 63)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_63d252d_base_v138_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_63d378d_base_v139_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 63)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_63d504d_base_v140_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_126d5d_base_v141_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 126)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_126d10d_base_v142_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 126)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_126d21d_base_v143_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 126)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_126d42d_base_v144_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 126)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_126d63d_base_v145_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 126)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_126d126d_base_v146_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 126)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_126d189d_base_v147_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 126)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_126d252d_base_v148_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 126)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_126d378d_base_v149_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 126)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_126d504d_base_v150_signal(grossmargin, closeadj):
    base = _f37_gm_floor(grossmargin, 126)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f37hgm_f37_healthcare_gross_margin_quality_cnsdivclose_126d_base_v076_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsdivclose_189d_base_v077_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsdivclose_252d_base_v078_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsdivclose_378d_base_v079_signal,
    f37hgm_f37_healthcare_gross_margin_quality_cnsdivclose_504d_base_v080_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscdivclose_5d_base_v081_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscdivclose_10d_base_v082_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscdivclose_21d_base_v083_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscdivclose_42d_base_v084_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscdivclose_63d_base_v085_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscdivclose_126d_base_v086_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscdivclose_189d_base_v087_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscdivclose_252d_base_v088_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscdivclose_378d_base_v089_signal,
    f37hgm_f37_healthcare_gross_margin_quality_qscdivclose_504d_base_v090_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_5d5d_base_v091_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_5d10d_base_v092_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_5d21d_base_v093_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_5d42d_base_v094_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_5d63d_base_v095_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_5d126d_base_v096_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_5d189d_base_v097_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_5d252d_base_v098_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_5d378d_base_v099_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_5d504d_base_v100_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_10d5d_base_v101_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_10d10d_base_v102_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_10d21d_base_v103_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_10d42d_base_v104_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_10d63d_base_v105_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_10d126d_base_v106_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_10d189d_base_v107_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_10d252d_base_v108_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_10d378d_base_v109_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_10d504d_base_v110_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_21d5d_base_v111_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_21d10d_base_v112_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_21d21d_base_v113_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_21d42d_base_v114_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_21d63d_base_v115_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_21d126d_base_v116_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_21d189d_base_v117_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_21d252d_base_v118_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_21d378d_base_v119_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_21d504d_base_v120_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_42d5d_base_v121_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_42d10d_base_v122_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_42d21d_base_v123_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_42d42d_base_v124_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_42d63d_base_v125_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_42d126d_base_v126_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_42d189d_base_v127_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_42d252d_base_v128_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_42d378d_base_v129_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_42d504d_base_v130_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_63d5d_base_v131_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_63d10d_base_v132_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_63d21d_base_v133_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_63d42d_base_v134_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_63d63d_base_v135_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_63d126d_base_v136_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_63d189d_base_v137_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_63d252d_base_v138_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_63d378d_base_v139_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_63d504d_base_v140_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_126d5d_base_v141_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_126d10d_base_v142_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_126d21d_base_v143_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_126d42d_base_v144_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_126d63d_base_v145_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_126d126d_base_v146_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_126d189d_base_v147_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_126d252d_base_v148_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_126d378d_base_v149_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanmulclose_126d504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}

F37_HEALTHCARE_GROSS_MARGIN_QUALITY_REGISTRY_076_150 = REGISTRY



if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit,
        "sgna": sgna, "opex": opex, "rnd": rnd,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f37_gm_floor", "_f37_gm_consistency", "_f37_gm_quality_score")
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
    print(f"OK f37_healthcare_gross_margin_quality_base_076_150_claude: {n_features} features pass")
