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
def _f43_capex_intensity(capex, revenue):
    return capex / revenue.replace(0, np.nan)


def _f43_capex_efficiency(capex, revenue, w):
    rev_chg = revenue.diff(periods=w)
    cap_avg = _mean(capex, w)
    return rev_chg / cap_avg.replace(0, np.nan)


def _f43_capex_quality(capex, depamor, w):
    cap_avg = _mean(capex, w)
    dep_avg = _mean(depamor, w)
    return (cap_avg - dep_avg) / dep_avg.replace(0, np.nan)

# v076: capeff_10d_alt
def f43hce_f43_healthcare_capex_efficiency_capeff_10d_alt_base_v076_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 10) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v077: capeff_42d_alt
def f43hce_f43_healthcare_capex_efficiency_capeff_42d_alt_base_v077_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 42) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v078: capeff_189d_alt
def f43hce_f43_healthcare_capex_efficiency_capeff_189d_alt_base_v078_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 189) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v079: composite_63d
def f43hce_f43_healthcare_capex_efficiency_composite_63d_base_v079_signal(capex, revenue, depamor, closeadj):
    result = (_z(_mean(_f43_capex_intensity(capex, revenue), 63), 252) + _z(_f43_capex_efficiency(capex, revenue, 63), 252) + _z(_f43_capex_quality(capex, depamor, 63), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v080: composite_252d
def f43hce_f43_healthcare_capex_efficiency_composite_252d_base_v080_signal(capex, revenue, depamor, closeadj):
    result = (_z(_mean(_f43_capex_intensity(capex, revenue), 252), 504) + _z(_f43_capex_efficiency(capex, revenue, 252), 504) + _z(_f43_capex_quality(capex, depamor, 252), 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v081: composite_126d
def f43hce_f43_healthcare_capex_efficiency_composite_126d_base_v081_signal(capex, revenue, depamor, closeadj):
    result = (_z(_mean(_f43_capex_intensity(capex, revenue), 126), 252) + _z(_f43_capex_efficiency(capex, revenue, 126), 252) + _z(_f43_capex_quality(capex, depamor, 126), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v082: capintxprice2_21d
def f43hce_f43_healthcare_capex_efficiency_capintxprice2_21d_base_v082_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v083: capintxprice2_63d
def f43hce_f43_healthcare_capex_efficiency_capintxprice2_63d_base_v083_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v084: capintxprice2_252d
def f43hce_f43_healthcare_capex_efficiency_capintxprice2_252d_base_v084_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v085: capeffxprice2_21d
def f43hce_f43_healthcare_capex_efficiency_capeffxprice2_21d_base_v085_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v086: capeffxprice2_63d
def f43hce_f43_healthcare_capex_efficiency_capeffxprice2_63d_base_v086_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v087: capeffxprice2_252d
def f43hce_f43_healthcare_capex_efficiency_capeffxprice2_252d_base_v087_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v088: capqualxprice2_21d
def f43hce_f43_healthcare_capex_efficiency_capqualxprice2_21d_base_v088_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v089: capqualxprice2_63d
def f43hce_f43_healthcare_capex_efficiency_capqualxprice2_63d_base_v089_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v090: capqualxprice2_252d
def f43hce_f43_healthcare_capex_efficiency_capqualxprice2_252d_base_v090_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v091: capintqr_21d
def f43hce_f43_healthcare_capex_efficiency_capintqr_21d_base_v091_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 21).rolling(252, min_periods=84).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v092: capintqr_63d
def f43hce_f43_healthcare_capex_efficiency_capintqr_63d_base_v092_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 63).rolling(252, min_periods=84).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v093: capintqr_252d
def f43hce_f43_healthcare_capex_efficiency_capintqr_252d_base_v093_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 252).rolling(504, min_periods=168).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v094: capeffqr_21d
def f43hce_f43_healthcare_capex_efficiency_capeffqr_21d_base_v094_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 21).rolling(252, min_periods=84).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v095: capeffqr_63d
def f43hce_f43_healthcare_capex_efficiency_capeffqr_63d_base_v095_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 63).rolling(252, min_periods=84).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v096: capeffqr_252d
def f43hce_f43_healthcare_capex_efficiency_capeffqr_252d_base_v096_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 252).rolling(504, min_periods=168).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v097: capqualqr_21d
def f43hce_f43_healthcare_capex_efficiency_capqualqr_21d_base_v097_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 21).rolling(252, min_periods=84).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v098: capqualqr_63d
def f43hce_f43_healthcare_capex_efficiency_capqualqr_63d_base_v098_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 63).rolling(252, min_periods=84).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v099: capqualqr_252d
def f43hce_f43_healthcare_capex_efficiency_capqualqr_252d_base_v099_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 252).rolling(504, min_periods=168).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v100: capintdiff_21_21
def f43hce_f43_healthcare_capex_efficiency_capintdiff_21_21_base_v100_signal(capex, revenue, closeadj):
    result = (_mean(_f43_capex_intensity(capex, revenue), 21) - _mean(_f43_capex_intensity(capex, revenue), 21).shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v101: capintdiff_63_63
def f43hce_f43_healthcare_capex_efficiency_capintdiff_63_63_base_v101_signal(capex, revenue, closeadj):
    result = (_mean(_f43_capex_intensity(capex, revenue), 63) - _mean(_f43_capex_intensity(capex, revenue), 63).shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v102: capintdiff_252_63
def f43hce_f43_healthcare_capex_efficiency_capintdiff_252_63_base_v102_signal(capex, revenue, closeadj):
    result = (_mean(_f43_capex_intensity(capex, revenue), 252) - _mean(_f43_capex_intensity(capex, revenue), 252).shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v103: capeffdiff_21_21
def f43hce_f43_healthcare_capex_efficiency_capeffdiff_21_21_base_v103_signal(capex, revenue, closeadj):
    result = (_f43_capex_efficiency(capex, revenue, 21) - _f43_capex_efficiency(capex, revenue, 21).shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v104: capeffdiff_63_63
def f43hce_f43_healthcare_capex_efficiency_capeffdiff_63_63_base_v104_signal(capex, revenue, closeadj):
    result = (_f43_capex_efficiency(capex, revenue, 63) - _f43_capex_efficiency(capex, revenue, 63).shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v105: capeffdiff_252_63
def f43hce_f43_healthcare_capex_efficiency_capeffdiff_252_63_base_v105_signal(capex, revenue, closeadj):
    result = (_f43_capex_efficiency(capex, revenue, 252) - _f43_capex_efficiency(capex, revenue, 252).shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v106: capqualdiff_21_21
def f43hce_f43_healthcare_capex_efficiency_capqualdiff_21_21_base_v106_signal(capex, depamor, closeadj):
    result = (_f43_capex_quality(capex, depamor, 21) - _f43_capex_quality(capex, depamor, 21).shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v107: capqualdiff_63_63
def f43hce_f43_healthcare_capex_efficiency_capqualdiff_63_63_base_v107_signal(capex, depamor, closeadj):
    result = (_f43_capex_quality(capex, depamor, 63) - _f43_capex_quality(capex, depamor, 63).shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v108: capqualdiff_252_63
def f43hce_f43_healthcare_capex_efficiency_capqualdiff_252_63_base_v108_signal(capex, depamor, closeadj):
    result = (_f43_capex_quality(capex, depamor, 252) - _f43_capex_quality(capex, depamor, 252).shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v109: capintlog_21d
def f43hce_f43_healthcare_capex_efficiency_capintlog_21d_base_v109_signal(capex, revenue, closeadj):
    result = np.log1p(_mean(_f43_capex_intensity(capex, revenue), 21).abs()) * np.sign(_mean(_f43_capex_intensity(capex, revenue), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v110: capintlog_63d
def f43hce_f43_healthcare_capex_efficiency_capintlog_63d_base_v110_signal(capex, revenue, closeadj):
    result = np.log1p(_mean(_f43_capex_intensity(capex, revenue), 63).abs()) * np.sign(_mean(_f43_capex_intensity(capex, revenue), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v111: capintlog_252d
def f43hce_f43_healthcare_capex_efficiency_capintlog_252d_base_v111_signal(capex, revenue, closeadj):
    result = np.log1p(_mean(_f43_capex_intensity(capex, revenue), 252).abs()) * np.sign(_mean(_f43_capex_intensity(capex, revenue), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v112: capefflog_21d
def f43hce_f43_healthcare_capex_efficiency_capefflog_21d_base_v112_signal(capex, revenue, closeadj):
    result = np.sign(_f43_capex_efficiency(capex, revenue, 21)) * np.log1p(_f43_capex_efficiency(capex, revenue, 21).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v113: capefflog_63d
def f43hce_f43_healthcare_capex_efficiency_capefflog_63d_base_v113_signal(capex, revenue, closeadj):
    result = np.sign(_f43_capex_efficiency(capex, revenue, 63)) * np.log1p(_f43_capex_efficiency(capex, revenue, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v114: capefflog_252d
def f43hce_f43_healthcare_capex_efficiency_capefflog_252d_base_v114_signal(capex, revenue, closeadj):
    result = np.sign(_f43_capex_efficiency(capex, revenue, 252)) * np.log1p(_f43_capex_efficiency(capex, revenue, 252).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v115: capquallog_21d
def f43hce_f43_healthcare_capex_efficiency_capquallog_21d_base_v115_signal(capex, depamor, closeadj):
    result = np.sign(_f43_capex_quality(capex, depamor, 21)) * np.log1p(_f43_capex_quality(capex, depamor, 21).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v116: capquallog_63d
def f43hce_f43_healthcare_capex_efficiency_capquallog_63d_base_v116_signal(capex, depamor, closeadj):
    result = np.sign(_f43_capex_quality(capex, depamor, 63)) * np.log1p(_f43_capex_quality(capex, depamor, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v117: capquallog_252d
def f43hce_f43_healthcare_capex_efficiency_capquallog_252d_base_v117_signal(capex, depamor, closeadj):
    result = np.sign(_f43_capex_quality(capex, depamor, 252)) * np.log1p(_f43_capex_quality(capex, depamor, 252).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v118: capeffx_21x63
def f43hce_f43_healthcare_capex_efficiency_capeffx_21x63_base_v118_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 21) * _f43_capex_efficiency(capex, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v119: capeffx_21x252
def f43hce_f43_healthcare_capex_efficiency_capeffx_21x252_base_v119_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 21) * _f43_capex_efficiency(capex, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v120: capeffx_63x252
def f43hce_f43_healthcare_capex_efficiency_capeffx_63x252_base_v120_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 63) * _f43_capex_efficiency(capex, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v121: capeffx_63x504
def f43hce_f43_healthcare_capex_efficiency_capeffx_63x504_base_v121_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 63) * _f43_capex_efficiency(capex, revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v122: capeffx_126x504
def f43hce_f43_healthcare_capex_efficiency_capeffx_126x504_base_v122_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 126) * _f43_capex_efficiency(capex, revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v123: capqualx_21x63
def f43hce_f43_healthcare_capex_efficiency_capqualx_21x63_base_v123_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 21) * _f43_capex_quality(capex, depamor, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v124: capqualx_21x252
def f43hce_f43_healthcare_capex_efficiency_capqualx_21x252_base_v124_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 21) * _f43_capex_quality(capex, depamor, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v125: capqualx_63x252
def f43hce_f43_healthcare_capex_efficiency_capqualx_63x252_base_v125_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 63) * _f43_capex_quality(capex, depamor, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v126: capqualx_63x504
def f43hce_f43_healthcare_capex_efficiency_capqualx_63x504_base_v126_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 63) * _f43_capex_quality(capex, depamor, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v127: capqualx_126x504
def f43hce_f43_healthcare_capex_efficiency_capqualx_126x504_base_v127_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 126) * _f43_capex_quality(capex, depamor, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v128: capintx_21x63
def f43hce_f43_healthcare_capex_efficiency_capintx_21x63_base_v128_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 21) * _mean(_f43_capex_intensity(capex, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v129: capintx_21x252
def f43hce_f43_healthcare_capex_efficiency_capintx_21x252_base_v129_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 21) * _mean(_f43_capex_intensity(capex, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v130: capintx_63x252
def f43hce_f43_healthcare_capex_efficiency_capintx_63x252_base_v130_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 63) * _mean(_f43_capex_intensity(capex, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v131: capintx_63x504
def f43hce_f43_healthcare_capex_efficiency_capintx_63x504_base_v131_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 63) * _mean(_f43_capex_intensity(capex, revenue), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v132: capintx_126x504
def f43hce_f43_healthcare_capex_efficiency_capintx_126x504_base_v132_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 126) * _mean(_f43_capex_intensity(capex, revenue), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v133: capefftri_2163252
def f43hce_f43_healthcare_capex_efficiency_capefftri_2163252_base_v133_signal(capex, revenue, closeadj):
    result = (_f43_capex_efficiency(capex, revenue, 21) + _f43_capex_efficiency(capex, revenue, 63) + _f43_capex_efficiency(capex, revenue, 252)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v134: capefftri_63126252
def f43hce_f43_healthcare_capex_efficiency_capefftri_63126252_base_v134_signal(capex, revenue, closeadj):
    result = (_f43_capex_efficiency(capex, revenue, 63) + _f43_capex_efficiency(capex, revenue, 126) + _f43_capex_efficiency(capex, revenue, 252)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v135: capefftri_126252504
def f43hce_f43_healthcare_capex_efficiency_capefftri_126252504_base_v135_signal(capex, revenue, closeadj):
    result = (_f43_capex_efficiency(capex, revenue, 126) + _f43_capex_efficiency(capex, revenue, 252) + _f43_capex_efficiency(capex, revenue, 504)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v136: capqualtri_2163252
def f43hce_f43_healthcare_capex_efficiency_capqualtri_2163252_base_v136_signal(capex, depamor, closeadj):
    result = (_f43_capex_quality(capex, depamor, 21) + _f43_capex_quality(capex, depamor, 63) + _f43_capex_quality(capex, depamor, 252)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v137: capqualtri_63126252
def f43hce_f43_healthcare_capex_efficiency_capqualtri_63126252_base_v137_signal(capex, depamor, closeadj):
    result = (_f43_capex_quality(capex, depamor, 63) + _f43_capex_quality(capex, depamor, 126) + _f43_capex_quality(capex, depamor, 252)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v138: capqualtri_126252504
def f43hce_f43_healthcare_capex_efficiency_capqualtri_126252504_base_v138_signal(capex, depamor, closeadj):
    result = (_f43_capex_quality(capex, depamor, 126) + _f43_capex_quality(capex, depamor, 252) + _f43_capex_quality(capex, depamor, 504)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v139: capinttri_2163252
def f43hce_f43_healthcare_capex_efficiency_capinttri_2163252_base_v139_signal(capex, revenue, closeadj):
    result = (_mean(_f43_capex_intensity(capex, revenue), 21) + _mean(_f43_capex_intensity(capex, revenue), 63) + _mean(_f43_capex_intensity(capex, revenue), 252)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v140: capinttri_63126252
def f43hce_f43_healthcare_capex_efficiency_capinttri_63126252_base_v140_signal(capex, revenue, closeadj):
    result = (_mean(_f43_capex_intensity(capex, revenue), 63) + _mean(_f43_capex_intensity(capex, revenue), 126) + _mean(_f43_capex_intensity(capex, revenue), 252)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v141: capinttri_126252504
def f43hce_f43_healthcare_capex_efficiency_capinttri_126252504_base_v141_signal(capex, revenue, closeadj):
    result = (_mean(_f43_capex_intensity(capex, revenue), 126) + _mean(_f43_capex_intensity(capex, revenue), 252) + _mean(_f43_capex_intensity(capex, revenue), 504)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v142: capeffxrev_21d
def f43hce_f43_healthcare_capex_efficiency_capeffxrev_21d_base_v142_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 21) * revenue.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v143: capeffxrev_63d
def f43hce_f43_healthcare_capex_efficiency_capeffxrev_63d_base_v143_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 63) * revenue.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v144: capeffxrev_252d
def f43hce_f43_healthcare_capex_efficiency_capeffxrev_252d_base_v144_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 252) * revenue.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v145: capqual_5d_alt
def f43hce_f43_healthcare_capex_efficiency_capqual_5d_alt_base_v145_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 5) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v146: capqual_10d_alt
def f43hce_f43_healthcare_capex_efficiency_capqual_10d_alt_base_v146_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 10) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v147: capqual_42d_alt
def f43hce_f43_healthcare_capex_efficiency_capqual_42d_alt_base_v147_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 42) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v148: capqual_189d_alt
def f43hce_f43_healthcare_capex_efficiency_capqual_189d_alt_base_v148_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 189) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v149: capqual_378d_alt
def f43hce_f43_healthcare_capex_efficiency_capqual_378d_alt_base_v149_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 378) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v150: capeffpos_21d
def f43hce_f43_healthcare_capex_efficiency_capeffpos_21d_base_v150_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 21).clip(lower=0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f43hce_f43_healthcare_capex_efficiency_capeff_10d_alt_base_v076_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_42d_alt_base_v077_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_189d_alt_base_v078_signal,
    f43hce_f43_healthcare_capex_efficiency_composite_63d_base_v079_signal,
    f43hce_f43_healthcare_capex_efficiency_composite_252d_base_v080_signal,
    f43hce_f43_healthcare_capex_efficiency_composite_126d_base_v081_signal,
    f43hce_f43_healthcare_capex_efficiency_capintxprice2_21d_base_v082_signal,
    f43hce_f43_healthcare_capex_efficiency_capintxprice2_63d_base_v083_signal,
    f43hce_f43_healthcare_capex_efficiency_capintxprice2_252d_base_v084_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffxprice2_21d_base_v085_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffxprice2_63d_base_v086_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffxprice2_252d_base_v087_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualxprice2_21d_base_v088_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualxprice2_63d_base_v089_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualxprice2_252d_base_v090_signal,
    f43hce_f43_healthcare_capex_efficiency_capintqr_21d_base_v091_signal,
    f43hce_f43_healthcare_capex_efficiency_capintqr_63d_base_v092_signal,
    f43hce_f43_healthcare_capex_efficiency_capintqr_252d_base_v093_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffqr_21d_base_v094_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffqr_63d_base_v095_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffqr_252d_base_v096_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualqr_21d_base_v097_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualqr_63d_base_v098_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualqr_252d_base_v099_signal,
    f43hce_f43_healthcare_capex_efficiency_capintdiff_21_21_base_v100_signal,
    f43hce_f43_healthcare_capex_efficiency_capintdiff_63_63_base_v101_signal,
    f43hce_f43_healthcare_capex_efficiency_capintdiff_252_63_base_v102_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffdiff_21_21_base_v103_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffdiff_63_63_base_v104_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffdiff_252_63_base_v105_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualdiff_21_21_base_v106_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualdiff_63_63_base_v107_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualdiff_252_63_base_v108_signal,
    f43hce_f43_healthcare_capex_efficiency_capintlog_21d_base_v109_signal,
    f43hce_f43_healthcare_capex_efficiency_capintlog_63d_base_v110_signal,
    f43hce_f43_healthcare_capex_efficiency_capintlog_252d_base_v111_signal,
    f43hce_f43_healthcare_capex_efficiency_capefflog_21d_base_v112_signal,
    f43hce_f43_healthcare_capex_efficiency_capefflog_63d_base_v113_signal,
    f43hce_f43_healthcare_capex_efficiency_capefflog_252d_base_v114_signal,
    f43hce_f43_healthcare_capex_efficiency_capquallog_21d_base_v115_signal,
    f43hce_f43_healthcare_capex_efficiency_capquallog_63d_base_v116_signal,
    f43hce_f43_healthcare_capex_efficiency_capquallog_252d_base_v117_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffx_21x63_base_v118_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffx_21x252_base_v119_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffx_63x252_base_v120_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffx_63x504_base_v121_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffx_126x504_base_v122_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualx_21x63_base_v123_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualx_21x252_base_v124_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualx_63x252_base_v125_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualx_63x504_base_v126_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualx_126x504_base_v127_signal,
    f43hce_f43_healthcare_capex_efficiency_capintx_21x63_base_v128_signal,
    f43hce_f43_healthcare_capex_efficiency_capintx_21x252_base_v129_signal,
    f43hce_f43_healthcare_capex_efficiency_capintx_63x252_base_v130_signal,
    f43hce_f43_healthcare_capex_efficiency_capintx_63x504_base_v131_signal,
    f43hce_f43_healthcare_capex_efficiency_capintx_126x504_base_v132_signal,
    f43hce_f43_healthcare_capex_efficiency_capefftri_2163252_base_v133_signal,
    f43hce_f43_healthcare_capex_efficiency_capefftri_63126252_base_v134_signal,
    f43hce_f43_healthcare_capex_efficiency_capefftri_126252504_base_v135_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualtri_2163252_base_v136_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualtri_63126252_base_v137_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualtri_126252504_base_v138_signal,
    f43hce_f43_healthcare_capex_efficiency_capinttri_2163252_base_v139_signal,
    f43hce_f43_healthcare_capex_efficiency_capinttri_63126252_base_v140_signal,
    f43hce_f43_healthcare_capex_efficiency_capinttri_126252504_base_v141_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffxrev_21d_base_v142_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffxrev_63d_base_v143_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffxrev_252d_base_v144_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_5d_alt_base_v145_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_10d_alt_base_v146_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_42d_alt_base_v147_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_189d_alt_base_v148_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_378d_alt_base_v149_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffpos_21d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F43_HEALTHCARE_CAPEX_EFFICIENCY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    capex = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")

    cols = {
        "capex": capex,
        "closeadj": closeadj,
        "depamor": depamor,
        "revenue": revenue,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f43_capex_intensity', '_f43_capex_efficiency', '_f43_capex_quality',)
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
    print(f"OK f43_healthcare_capex_efficiency_base_076_150_claude: {n_features} features pass")
