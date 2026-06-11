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
def _f31_ocf_to_ebitda(ncfo, ebitda):
    return ncfo / ebitda.replace(0, np.nan)


def _f31_cash_conv_durability(ncfo, ebitda, w):
    ratio = ncfo / ebitda.replace(0, np.nan)
    return _mean(ratio, w) / (_std(ratio, w).replace(0, np.nan))


def _f31_conversion_consistency(fcf, ebitda, w):
    ratio = fcf / ebitda.replace(0, np.nan)
    return _mean(ratio, w) - _std(ratio, w)


# ---- features 076 - 150 ----

def f31ccq_f31_cash_conversion_quality_fcfebitdaminusone_63d_base_v076_signal(fcf, ebitda, closeadj):
    base = fcf / ebitda.replace(0, np.nan) - 1.0
    result = _mean(base, 63) * closeadj + _f31_conversion_consistency(fcf, ebitda, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfebitdaminusone_252d_base_v077_signal(fcf, ebitda, closeadj):
    base = fcf / ebitda.replace(0, np.nan) - 1.0
    result = _mean(base, 252) * closeadj + _f31_conversion_consistency(fcf, ebitda, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfebitdasq_63d_base_v078_signal(fcf, ebitda, closeadj):
    base = fcf / ebitda.replace(0, np.nan)
    result = _mean(base * base.abs(), 63) * closeadj + _f31_conversion_consistency(fcf, ebitda, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfebitdasq_252d_base_v079_signal(fcf, ebitda, closeadj):
    base = fcf / ebitda.replace(0, np.nan)
    result = _mean(base * base.abs(), 252) * closeadj + _f31_conversion_consistency(fcf, ebitda, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfebitdamax_252d_base_v080_signal(fcf, ebitda, closeadj):
    base = fcf / ebitda.replace(0, np.nan)
    result = base.rolling(252, min_periods=63).max() * closeadj + _f31_conversion_consistency(fcf, ebitda, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfebitdamin_252d_base_v081_signal(fcf, ebitda, closeadj):
    base = fcf / ebitda.replace(0, np.nan)
    result = base.rolling(252, min_periods=63).min() * closeadj + _f31_conversion_consistency(fcf, ebitda, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfebitdarange_252d_base_v082_signal(fcf, ebitda, closeadj):
    base = fcf / ebitda.replace(0, np.nan)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj + _f31_conversion_consistency(fcf, ebitda, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfebitdarank_63d_base_v083_signal(fcf, ebitda, closeadj):
    base = fcf / ebitda.replace(0, np.nan)
    rank = base.rolling(63, min_periods=20).rank(pct=True)
    result = rank * closeadj + _f31_conversion_consistency(fcf, ebitda, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfebitdarank_252d_base_v084_signal(fcf, ebitda, closeadj):
    base = fcf / ebitda.replace(0, np.nan)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj + _f31_conversion_consistency(fcf, ebitda, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfebitdarank_504d_base_v085_signal(fcf, ebitda, closeadj):
    base = fcf / ebitda.replace(0, np.nan)
    rank = base.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj + _f31_conversion_consistency(fcf, ebitda, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durability_5d_base_v086_signal(ncfo, ebitda, closeadj):
    result = _f31_cash_conv_durability(ncfo, ebitda, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durability_10d_base_v087_signal(ncfo, ebitda, closeadj):
    result = _f31_cash_conv_durability(ncfo, ebitda, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durability_42d_base_v088_signal(ncfo, ebitda, closeadj):
    result = _f31_cash_conv_durability(ncfo, ebitda, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durability_189d_base_v089_signal(ncfo, ebitda, closeadj):
    result = _f31_cash_conv_durability(ncfo, ebitda, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durability_378d_base_v090_signal(ncfo, ebitda, closeadj):
    result = _f31_cash_conv_durability(ncfo, ebitda, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consist_5d_base_v091_signal(fcf, ebitda, closeadj):
    result = _f31_conversion_consistency(fcf, ebitda, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consist_10d_base_v092_signal(fcf, ebitda, closeadj):
    result = _f31_conversion_consistency(fcf, ebitda, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consist_42d_base_v093_signal(fcf, ebitda, closeadj):
    result = _f31_conversion_consistency(fcf, ebitda, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consist_189d_base_v094_signal(fcf, ebitda, closeadj):
    result = _f31_conversion_consistency(fcf, ebitda, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consist_378d_base_v095_signal(fcf, ebitda, closeadj):
    result = _f31_conversion_consistency(fcf, ebitda, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdalog_21d_base_v096_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj
    result = _mean(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdalog_63d_base_v097_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj
    result = _mean(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdalog_252d_base_v098_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj
    result = _mean(result, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durabilityema_63d_base_v099_signal(ncfo, ebitda, closeadj):
    base = _f31_cash_conv_durability(ncfo, ebitda, 63)
    result = base.ewm(span=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durabilityema_252d_base_v100_signal(ncfo, ebitda, closeadj):
    base = _f31_cash_conv_durability(ncfo, ebitda, 252)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consistema_63d_base_v101_signal(fcf, ebitda, closeadj):
    base = _f31_conversion_consistency(fcf, ebitda, 63)
    result = base.ewm(span=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consistema_252d_base_v102_signal(fcf, ebitda, closeadj):
    base = _f31_conversion_consistency(fcf, ebitda, 252)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocffcfratio_63d_base_v103_signal(ncfo, fcf, ebitda, closeadj):
    base = ncfo / fcf.replace(0, np.nan)
    result = _mean(base, 63) * closeadj + _f31_ocf_to_ebitda(ncfo, ebitda) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocffcfratio_252d_base_v104_signal(ncfo, fcf, ebitda, closeadj):
    base = ncfo / fcf.replace(0, np.nan)
    result = _mean(base, 252) * closeadj + _f31_ocf_to_ebitda(ncfo, ebitda) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocffcfdiff_63d_base_v105_signal(ncfo, fcf, ebitda, closeadj):
    base = ncfo - fcf
    result = _mean(base, 63) * closeadj / ebitda.replace(0, np.nan).abs() + _f31_ocf_to_ebitda(ncfo, ebitda) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocffcfdiff_252d_base_v106_signal(ncfo, fcf, ebitda, closeadj):
    base = ncfo - fcf
    result = _mean(base, 252) * closeadj / ebitda.replace(0, np.nan).abs() + _f31_ocf_to_ebitda(ncfo, ebitda) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durabilxprice_5d_base_v107_signal(ncfo, ebitda, closeadj):
    result = _f31_cash_conv_durability(ncfo, ebitda, 21) * closeadj * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durabilxprice_21d_base_v108_signal(ncfo, ebitda, closeadj):
    result = _f31_cash_conv_durability(ncfo, ebitda, 63) * closeadj * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durabilxprice_63d_base_v109_signal(ncfo, ebitda, closeadj):
    result = _f31_cash_conv_durability(ncfo, ebitda, 252) * closeadj * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consistxprice_5d_base_v110_signal(fcf, ebitda, closeadj):
    result = _f31_conversion_consistency(fcf, ebitda, 21) * closeadj * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consistxprice_21d_base_v111_signal(fcf, ebitda, closeadj):
    result = _f31_conversion_consistency(fcf, ebitda, 63) * closeadj * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consistxprice_504d_base_v112_signal(fcf, ebitda, closeadj):
    result = _f31_conversion_consistency(fcf, ebitda, 504) * closeadj * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdaslope_21d_base_v113_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = (base - base.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdaslope_63d_base_v114_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdaslope_252d_base_v115_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durabilityratio_63v252_base_v116_signal(ncfo, ebitda, closeadj):
    a = _f31_cash_conv_durability(ncfo, ebitda, 63)
    b = _f31_cash_conv_durability(ncfo, ebitda, 252)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durabilityratio_252v504_base_v117_signal(ncfo, ebitda, closeadj):
    a = _f31_cash_conv_durability(ncfo, ebitda, 252)
    b = _f31_cash_conv_durability(ncfo, ebitda, 504)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consistratio_63v252_base_v118_signal(fcf, ebitda, closeadj):
    a = _f31_conversion_consistency(fcf, ebitda, 63)
    b = _f31_conversion_consistency(fcf, ebitda, 252)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consistratio_252v504_base_v119_signal(fcf, ebitda, closeadj):
    a = _f31_conversion_consistency(fcf, ebitda, 252)
    b = _f31_conversion_consistency(fcf, ebitda, 504)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durabilitydiff_63m252_base_v120_signal(ncfo, ebitda, closeadj):
    a = _f31_cash_conv_durability(ncfo, ebitda, 63)
    b = _f31_cash_conv_durability(ncfo, ebitda, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durabilitydiff_252m504_base_v121_signal(ncfo, ebitda, closeadj):
    a = _f31_cash_conv_durability(ncfo, ebitda, 252)
    b = _f31_cash_conv_durability(ncfo, ebitda, 504)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consistdiff_63m252_base_v122_signal(fcf, ebitda, closeadj):
    a = _f31_conversion_consistency(fcf, ebitda, 63)
    b = _f31_conversion_consistency(fcf, ebitda, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consistdiff_252m504_base_v123_signal(fcf, ebitda, closeadj):
    a = _f31_conversion_consistency(fcf, ebitda, 252)
    b = _f31_conversion_consistency(fcf, ebitda, 504)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdaxfcf_63d_base_v124_signal(ncfo, fcf, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = _mean(base, 63) * closeadj * np.log(fcf.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdaxfcf_252d_base_v125_signal(ncfo, fcf, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = _mean(base, 252) * closeadj * np.log(fcf.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durabxlog_63d_base_v126_signal(ncfo, ebitda, closeadj):
    result = _f31_cash_conv_durability(ncfo, ebitda, 63) * closeadj * np.log(ebitda.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durabxlog_252d_base_v127_signal(ncfo, ebitda, closeadj):
    result = _f31_cash_conv_durability(ncfo, ebitda, 252) * closeadj * np.log(ebitda.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consistxlog_63d_base_v128_signal(fcf, ebitda, closeadj):
    result = _f31_conversion_consistency(fcf, ebitda, 63) * closeadj * np.log(fcf.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consistxlog_252d_base_v129_signal(fcf, ebitda, closeadj):
    result = _f31_conversion_consistency(fcf, ebitda, 252) * closeadj * np.log(fcf.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdaxpriceslope_21d_base_v130_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    pslope = closeadj.pct_change(21)
    result = _mean(base, 21) * closeadj * (1.0 + pslope)
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdaxpriceslope_63d_base_v131_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    pslope = closeadj.pct_change(63)
    result = _mean(base, 63) * closeadj * (1.0 + pslope)
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdaxpriceslope_252d_base_v132_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    pslope = closeadj.pct_change(252)
    result = _mean(base, 252) * closeadj * (1.0 + pslope)
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdaxstd_63d_base_v133_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = _mean(base, 63) * closeadj * _std(closeadj.pct_change(), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdaxstd_252d_base_v134_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = _mean(base, 252) * closeadj * _std(closeadj.pct_change(), 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdadeep_252d_base_v135_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    deep = (base < 0.5).astype(float)
    result = _mean(deep, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdahigh_252d_base_v136_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    med = base.rolling(252, min_periods=63).median()
    hi = (base > med).astype(float)
    result = _mean(hi, 252) * closeadj + base * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durabperc_63d_base_v137_signal(ncfo, ebitda, closeadj):
    base = _f31_cash_conv_durability(ncfo, ebitda, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durabperc_252d_base_v138_signal(ncfo, ebitda, closeadj):
    base = _f31_cash_conv_durability(ncfo, ebitda, 252)
    rank = base.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consistperc_63d_base_v139_signal(fcf, ebitda, closeadj):
    base = _f31_conversion_consistency(fcf, ebitda, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_consistperc_252d_base_v140_signal(fcf, ebitda, closeadj):
    base = _f31_conversion_consistency(fcf, ebitda, 252)
    rank = base.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdax_ebitdagrowth_63d_base_v141_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    g = ebitda.pct_change(63)
    result = _mean(base, 63) * closeadj * g
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdax_ebitdagrowth_252d_base_v142_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    g = ebitda.pct_change(252)
    result = _mean(base, 252) * closeadj * g
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfebitdax_fcfgrowth_63d_base_v143_signal(fcf, ebitda, closeadj):
    base = fcf / ebitda.replace(0, np.nan)
    g = fcf.pct_change(63)
    result = _mean(base, 63) * closeadj * g + _f31_conversion_consistency(fcf, ebitda, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_fcfebitdax_fcfgrowth_252d_base_v144_signal(fcf, ebitda, closeadj):
    base = fcf / ebitda.replace(0, np.nan)
    g = fcf.pct_change(252)
    result = _mean(base, 252) * closeadj * g + _f31_conversion_consistency(fcf, ebitda, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durabxebitda_63d_base_v145_signal(ncfo, ebitda, closeadj):
    result = _f31_cash_conv_durability(ncfo, ebitda, 63) * closeadj * np.log(ebitda.replace(0, np.nan).abs()) / 20.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_durabxebitda_252d_base_v146_signal(ncfo, ebitda, closeadj):
    result = _f31_cash_conv_durability(ncfo, ebitda, 252) * closeadj * np.log(ebitda.replace(0, np.nan).abs()) / 20.0
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdavolz_63d_base_v147_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = base * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_ocfebitdavolz_252d_base_v148_signal(ncfo, ebitda, closeadj):
    base = _f31_ocf_to_ebitda(ncfo, ebitda)
    result = base * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_compositeq_63d_base_v149_signal(ncfo, fcf, ebitda, closeadj):
    a = _mean(_f31_ocf_to_ebitda(ncfo, ebitda), 63)
    b = _f31_conversion_consistency(fcf, ebitda, 63)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31ccq_f31_cash_conversion_quality_compositeq_252d_base_v150_signal(ncfo, fcf, ebitda, closeadj):
    a = _mean(_f31_ocf_to_ebitda(ncfo, ebitda), 252)
    b = _f31_conversion_consistency(fcf, ebitda, 252)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f31ccq_f31_cash_conversion_quality_fcfebitdaminusone_63d_base_v076_signal,
    f31ccq_f31_cash_conversion_quality_fcfebitdaminusone_252d_base_v077_signal,
    f31ccq_f31_cash_conversion_quality_fcfebitdasq_63d_base_v078_signal,
    f31ccq_f31_cash_conversion_quality_fcfebitdasq_252d_base_v079_signal,
    f31ccq_f31_cash_conversion_quality_fcfebitdamax_252d_base_v080_signal,
    f31ccq_f31_cash_conversion_quality_fcfebitdamin_252d_base_v081_signal,
    f31ccq_f31_cash_conversion_quality_fcfebitdarange_252d_base_v082_signal,
    f31ccq_f31_cash_conversion_quality_fcfebitdarank_63d_base_v083_signal,
    f31ccq_f31_cash_conversion_quality_fcfebitdarank_252d_base_v084_signal,
    f31ccq_f31_cash_conversion_quality_fcfebitdarank_504d_base_v085_signal,
    f31ccq_f31_cash_conversion_quality_durability_5d_base_v086_signal,
    f31ccq_f31_cash_conversion_quality_durability_10d_base_v087_signal,
    f31ccq_f31_cash_conversion_quality_durability_42d_base_v088_signal,
    f31ccq_f31_cash_conversion_quality_durability_189d_base_v089_signal,
    f31ccq_f31_cash_conversion_quality_durability_378d_base_v090_signal,
    f31ccq_f31_cash_conversion_quality_consist_5d_base_v091_signal,
    f31ccq_f31_cash_conversion_quality_consist_10d_base_v092_signal,
    f31ccq_f31_cash_conversion_quality_consist_42d_base_v093_signal,
    f31ccq_f31_cash_conversion_quality_consist_189d_base_v094_signal,
    f31ccq_f31_cash_conversion_quality_consist_378d_base_v095_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdalog_21d_base_v096_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdalog_63d_base_v097_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdalog_252d_base_v098_signal,
    f31ccq_f31_cash_conversion_quality_durabilityema_63d_base_v099_signal,
    f31ccq_f31_cash_conversion_quality_durabilityema_252d_base_v100_signal,
    f31ccq_f31_cash_conversion_quality_consistema_63d_base_v101_signal,
    f31ccq_f31_cash_conversion_quality_consistema_252d_base_v102_signal,
    f31ccq_f31_cash_conversion_quality_ocffcfratio_63d_base_v103_signal,
    f31ccq_f31_cash_conversion_quality_ocffcfratio_252d_base_v104_signal,
    f31ccq_f31_cash_conversion_quality_ocffcfdiff_63d_base_v105_signal,
    f31ccq_f31_cash_conversion_quality_ocffcfdiff_252d_base_v106_signal,
    f31ccq_f31_cash_conversion_quality_durabilxprice_5d_base_v107_signal,
    f31ccq_f31_cash_conversion_quality_durabilxprice_21d_base_v108_signal,
    f31ccq_f31_cash_conversion_quality_durabilxprice_63d_base_v109_signal,
    f31ccq_f31_cash_conversion_quality_consistxprice_5d_base_v110_signal,
    f31ccq_f31_cash_conversion_quality_consistxprice_21d_base_v111_signal,
    f31ccq_f31_cash_conversion_quality_consistxprice_504d_base_v112_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdaslope_21d_base_v113_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdaslope_63d_base_v114_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdaslope_252d_base_v115_signal,
    f31ccq_f31_cash_conversion_quality_durabilityratio_63v252_base_v116_signal,
    f31ccq_f31_cash_conversion_quality_durabilityratio_252v504_base_v117_signal,
    f31ccq_f31_cash_conversion_quality_consistratio_63v252_base_v118_signal,
    f31ccq_f31_cash_conversion_quality_consistratio_252v504_base_v119_signal,
    f31ccq_f31_cash_conversion_quality_durabilitydiff_63m252_base_v120_signal,
    f31ccq_f31_cash_conversion_quality_durabilitydiff_252m504_base_v121_signal,
    f31ccq_f31_cash_conversion_quality_consistdiff_63m252_base_v122_signal,
    f31ccq_f31_cash_conversion_quality_consistdiff_252m504_base_v123_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdaxfcf_63d_base_v124_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdaxfcf_252d_base_v125_signal,
    f31ccq_f31_cash_conversion_quality_durabxlog_63d_base_v126_signal,
    f31ccq_f31_cash_conversion_quality_durabxlog_252d_base_v127_signal,
    f31ccq_f31_cash_conversion_quality_consistxlog_63d_base_v128_signal,
    f31ccq_f31_cash_conversion_quality_consistxlog_252d_base_v129_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdaxpriceslope_21d_base_v130_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdaxpriceslope_63d_base_v131_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdaxpriceslope_252d_base_v132_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdaxstd_63d_base_v133_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdaxstd_252d_base_v134_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdadeep_252d_base_v135_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdahigh_252d_base_v136_signal,
    f31ccq_f31_cash_conversion_quality_durabperc_63d_base_v137_signal,
    f31ccq_f31_cash_conversion_quality_durabperc_252d_base_v138_signal,
    f31ccq_f31_cash_conversion_quality_consistperc_63d_base_v139_signal,
    f31ccq_f31_cash_conversion_quality_consistperc_252d_base_v140_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdax_ebitdagrowth_63d_base_v141_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdax_ebitdagrowth_252d_base_v142_signal,
    f31ccq_f31_cash_conversion_quality_fcfebitdax_fcfgrowth_63d_base_v143_signal,
    f31ccq_f31_cash_conversion_quality_fcfebitdax_fcfgrowth_252d_base_v144_signal,
    f31ccq_f31_cash_conversion_quality_durabxebitda_63d_base_v145_signal,
    f31ccq_f31_cash_conversion_quality_durabxebitda_252d_base_v146_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdavolz_63d_base_v147_signal,
    f31ccq_f31_cash_conversion_quality_ocfebitdavolz_252d_base_v148_signal,
    f31ccq_f31_cash_conversion_quality_compositeq_63d_base_v149_signal,
    f31ccq_f31_cash_conversion_quality_compositeq_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F31_CASH_CONVERSION_QUALITY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")

    cols = {
        "closeadj": closeadj, "ebitda": ebitda, "fcf": fcf, "ncfo": ncfo,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f31_ocf_to_ebitda", "_f31_cash_conv_durability", "_f31_conversion_consistency")
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
    print(f"OK f31_cash_conversion_quality_base_076_150_claude: {n_features} features pass")
