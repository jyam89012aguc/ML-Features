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
def _f41_roic_stability(roic, w):
    m = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = roic.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan).abs()


def _f41_roic_compound(roic, w):
    return roic.rolling(w, min_periods=max(1, w // 2)).mean() * np.sqrt(w)


def _f41_roic_quality(roic, roa, w):
    spread = roic - roa
    return spread.rolling(w, min_periods=max(1, w // 2)).mean()

def f41urs_f41_utility_roic_stability_stabzxcm63_base_v076_signal(roic, roa, roe, closeadj):
    # rid=76
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 21)
    result = trans * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcm63_base_v077_signal(roic, roa, roe, closeadj):
    # rid=77
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 63)
    result = trans * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcm63_base_v078_signal(roic, roa, roe, closeadj):
    # rid=78
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 126)
    result = trans * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcm126_base_v079_signal(roic, roa, roe, closeadj):
    # rid=79
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 21)
    result = trans * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcm126_base_v080_signal(roic, roa, roe, closeadj):
    # rid=80
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 63)
    result = trans * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcm126_base_v081_signal(roic, roa, roe, closeadj):
    # rid=81
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 126)
    result = trans * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcz_base_v082_signal(roic, roa, roe, closeadj):
    # rid=82
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 21)
    result = trans * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcz_base_v083_signal(roic, roa, roe, closeadj):
    # rid=83
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 63)
    result = trans * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcz_base_v084_signal(roic, roa, roe, closeadj):
    # rid=84
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 126)
    result = trans * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcr_base_v085_signal(roic, roa, roe, closeadj):
    # rid=85
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 21)
    result = trans * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcr_base_v086_signal(roic, roa, roe, closeadj):
    # rid=86
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 63)
    result = trans * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcr_base_v087_signal(roic, roa, roe, closeadj):
    # rid=87
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 126)
    result = trans * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcr63_base_v088_signal(roic, roa, roe, closeadj):
    # rid=88
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 21)
    result = trans * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcr63_base_v089_signal(roic, roa, roe, closeadj):
    # rid=89
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 63)
    result = trans * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabzxcr63_base_v090_signal(roic, roa, roe, closeadj):
    # rid=90
    base = _f41_roic_stability(roic, 21)
    trans = _z(base, 126)
    result = trans * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxc_base_v091_signal(roic, roa, roe, closeadj):
    # rid=91
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 21)
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxc_base_v092_signal(roic, roa, roe, closeadj):
    # rid=92
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 63)
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxc_base_v093_signal(roic, roa, roe, closeadj):
    # rid=93
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 126)
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxlc_base_v094_signal(roic, roa, roe, closeadj):
    # rid=94
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 21)
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxlc_base_v095_signal(roic, roa, roe, closeadj):
    # rid=95
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 63)
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxlc_base_v096_signal(roic, roa, roe, closeadj):
    # rid=96
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 126)
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemadc_base_v097_signal(roic, roa, roe, closeadj):
    # rid=97
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 21)
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemadc_base_v098_signal(roic, roa, roe, closeadj):
    # rid=98
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 63)
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemadc_base_v099_signal(roic, roa, roe, closeadj):
    # rid=99
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 126)
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcm_base_v100_signal(roic, roa, roe, closeadj):
    # rid=100
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 21)
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcm_base_v101_signal(roic, roa, roe, closeadj):
    # rid=101
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 63)
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcm_base_v102_signal(roic, roa, roe, closeadj):
    # rid=102
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 126)
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcm63_base_v103_signal(roic, roa, roe, closeadj):
    # rid=103
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 21)
    result = trans * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcm63_base_v104_signal(roic, roa, roe, closeadj):
    # rid=104
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 63)
    result = trans * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcm63_base_v105_signal(roic, roa, roe, closeadj):
    # rid=105
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 126)
    result = trans * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcm126_base_v106_signal(roic, roa, roe, closeadj):
    # rid=106
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 21)
    result = trans * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcm126_base_v107_signal(roic, roa, roe, closeadj):
    # rid=107
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 63)
    result = trans * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcm126_base_v108_signal(roic, roa, roe, closeadj):
    # rid=108
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 126)
    result = trans * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcz_base_v109_signal(roic, roa, roe, closeadj):
    # rid=109
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 21)
    result = trans * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcz_base_v110_signal(roic, roa, roe, closeadj):
    # rid=110
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 63)
    result = trans * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcz_base_v111_signal(roic, roa, roe, closeadj):
    # rid=111
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 126)
    result = trans * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcr_base_v112_signal(roic, roa, roe, closeadj):
    # rid=112
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 21)
    result = trans * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcr_base_v113_signal(roic, roa, roe, closeadj):
    # rid=113
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 63)
    result = trans * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcr_base_v114_signal(roic, roa, roe, closeadj):
    # rid=114
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 126)
    result = trans * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcr63_base_v115_signal(roic, roa, roe, closeadj):
    # rid=115
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 21)
    result = trans * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcr63_base_v116_signal(roic, roa, roe, closeadj):
    # rid=116
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 63)
    result = trans * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabemaxcr63_base_v117_signal(roic, roa, roe, closeadj):
    # rid=117
    base = _f41_roic_stability(roic, 21)
    trans = _ema(base, 126)
    result = trans * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stababsxc_base_v118_signal(roic, roa, roe, closeadj):
    # rid=118
    base = _f41_roic_stability(roic, 21)
    trans = base.abs()
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stababsxlc_base_v119_signal(roic, roa, roe, closeadj):
    # rid=119
    base = _f41_roic_stability(roic, 21)
    trans = base.abs()
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stababsdc_base_v120_signal(roic, roa, roe, closeadj):
    # rid=120
    base = _f41_roic_stability(roic, 21)
    trans = base.abs()
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stababsxcm_base_v121_signal(roic, roa, roe, closeadj):
    # rid=121
    base = _f41_roic_stability(roic, 21)
    trans = base.abs()
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stababsxcm63_base_v122_signal(roic, roa, roe, closeadj):
    # rid=122
    base = _f41_roic_stability(roic, 21)
    trans = base.abs()
    result = trans * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stababsxcm126_base_v123_signal(roic, roa, roe, closeadj):
    # rid=123
    base = _f41_roic_stability(roic, 21)
    trans = base.abs()
    result = trans * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stababsxcz_base_v124_signal(roic, roa, roe, closeadj):
    # rid=124
    base = _f41_roic_stability(roic, 21)
    trans = base.abs()
    result = trans * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stababsxcr_base_v125_signal(roic, roa, roe, closeadj):
    # rid=125
    base = _f41_roic_stability(roic, 21)
    trans = base.abs()
    result = trans * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stababsxcr63_base_v126_signal(roic, roa, roe, closeadj):
    # rid=126
    base = _f41_roic_stability(roic, 21)
    trans = base.abs()
    result = trans * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stablogxc_base_v127_signal(roic, roa, roe, closeadj):
    # rid=127
    base = _f41_roic_stability(roic, 21)
    trans = np.log(base.abs() + 1e-9)
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stablogxlc_base_v128_signal(roic, roa, roe, closeadj):
    # rid=128
    base = _f41_roic_stability(roic, 21)
    trans = np.log(base.abs() + 1e-9)
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stablogdc_base_v129_signal(roic, roa, roe, closeadj):
    # rid=129
    base = _f41_roic_stability(roic, 21)
    trans = np.log(base.abs() + 1e-9)
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stablogxcm_base_v130_signal(roic, roa, roe, closeadj):
    # rid=130
    base = _f41_roic_stability(roic, 21)
    trans = np.log(base.abs() + 1e-9)
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stablogxcm63_base_v131_signal(roic, roa, roe, closeadj):
    # rid=131
    base = _f41_roic_stability(roic, 21)
    trans = np.log(base.abs() + 1e-9)
    result = trans * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stablogxcm126_base_v132_signal(roic, roa, roe, closeadj):
    # rid=132
    base = _f41_roic_stability(roic, 21)
    trans = np.log(base.abs() + 1e-9)
    result = trans * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stablogxcz_base_v133_signal(roic, roa, roe, closeadj):
    # rid=133
    base = _f41_roic_stability(roic, 21)
    trans = np.log(base.abs() + 1e-9)
    result = trans * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stablogxcr_base_v134_signal(roic, roa, roe, closeadj):
    # rid=134
    base = _f41_roic_stability(roic, 21)
    trans = np.log(base.abs() + 1e-9)
    result = trans * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stablogxcr63_base_v135_signal(roic, roa, roe, closeadj):
    # rid=135
    base = _f41_roic_stability(roic, 21)
    trans = np.log(base.abs() + 1e-9)
    result = trans * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsignxc_base_v136_signal(roic, roa, roe, closeadj):
    # rid=136
    base = _f41_roic_stability(roic, 21)
    trans = np.sign(base)
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsignxlc_base_v137_signal(roic, roa, roe, closeadj):
    # rid=137
    base = _f41_roic_stability(roic, 21)
    trans = np.sign(base)
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsigndc_base_v138_signal(roic, roa, roe, closeadj):
    # rid=138
    base = _f41_roic_stability(roic, 21)
    trans = np.sign(base)
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsignxcm_base_v139_signal(roic, roa, roe, closeadj):
    # rid=139
    base = _f41_roic_stability(roic, 21)
    trans = np.sign(base)
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsignxcm63_base_v140_signal(roic, roa, roe, closeadj):
    # rid=140
    base = _f41_roic_stability(roic, 21)
    trans = np.sign(base)
    result = trans * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsignxcm126_base_v141_signal(roic, roa, roe, closeadj):
    # rid=141
    base = _f41_roic_stability(roic, 21)
    trans = np.sign(base)
    result = trans * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsignxcz_base_v142_signal(roic, roa, roe, closeadj):
    # rid=142
    base = _f41_roic_stability(roic, 21)
    trans = np.sign(base)
    result = trans * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsignxcr_base_v143_signal(roic, roa, roe, closeadj):
    # rid=143
    base = _f41_roic_stability(roic, 21)
    trans = np.sign(base)
    result = trans * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsignxcr63_base_v144_signal(roic, roa, roe, closeadj):
    # rid=144
    base = _f41_roic_stability(roic, 21)
    trans = np.sign(base)
    result = trans * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsqxc_base_v145_signal(roic, roa, roe, closeadj):
    # rid=145
    base = _f41_roic_stability(roic, 21)
    trans = base * base.abs()
    result = trans * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsqxlc_base_v146_signal(roic, roa, roe, closeadj):
    # rid=146
    base = _f41_roic_stability(roic, 21)
    trans = base * base.abs()
    result = trans * np.log(closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsqdc_base_v147_signal(roic, roa, roe, closeadj):
    # rid=147
    base = _f41_roic_stability(roic, 21)
    trans = base * base.abs()
    result = trans / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsqxcm_base_v148_signal(roic, roa, roe, closeadj):
    # rid=148
    base = _f41_roic_stability(roic, 21)
    trans = base * base.abs()
    result = trans * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsqxcm63_base_v149_signal(roic, roa, roe, closeadj):
    # rid=149
    base = _f41_roic_stability(roic, 21)
    trans = base * base.abs()
    result = trans * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f41urs_f41_utility_roic_stability_stabsqxcm126_base_v150_signal(roic, roa, roe, closeadj):
    # rid=150
    base = _f41_roic_stability(roic, 21)
    trans = base * base.abs()
    result = trans * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f41urs_f41_utility_roic_stability_stabzxcm63_base_v076_signal,
    f41urs_f41_utility_roic_stability_stabzxcm63_base_v077_signal,
    f41urs_f41_utility_roic_stability_stabzxcm63_base_v078_signal,
    f41urs_f41_utility_roic_stability_stabzxcm126_base_v079_signal,
    f41urs_f41_utility_roic_stability_stabzxcm126_base_v080_signal,
    f41urs_f41_utility_roic_stability_stabzxcm126_base_v081_signal,
    f41urs_f41_utility_roic_stability_stabzxcz_base_v082_signal,
    f41urs_f41_utility_roic_stability_stabzxcz_base_v083_signal,
    f41urs_f41_utility_roic_stability_stabzxcz_base_v084_signal,
    f41urs_f41_utility_roic_stability_stabzxcr_base_v085_signal,
    f41urs_f41_utility_roic_stability_stabzxcr_base_v086_signal,
    f41urs_f41_utility_roic_stability_stabzxcr_base_v087_signal,
    f41urs_f41_utility_roic_stability_stabzxcr63_base_v088_signal,
    f41urs_f41_utility_roic_stability_stabzxcr63_base_v089_signal,
    f41urs_f41_utility_roic_stability_stabzxcr63_base_v090_signal,
    f41urs_f41_utility_roic_stability_stabemaxc_base_v091_signal,
    f41urs_f41_utility_roic_stability_stabemaxc_base_v092_signal,
    f41urs_f41_utility_roic_stability_stabemaxc_base_v093_signal,
    f41urs_f41_utility_roic_stability_stabemaxlc_base_v094_signal,
    f41urs_f41_utility_roic_stability_stabemaxlc_base_v095_signal,
    f41urs_f41_utility_roic_stability_stabemaxlc_base_v096_signal,
    f41urs_f41_utility_roic_stability_stabemadc_base_v097_signal,
    f41urs_f41_utility_roic_stability_stabemadc_base_v098_signal,
    f41urs_f41_utility_roic_stability_stabemadc_base_v099_signal,
    f41urs_f41_utility_roic_stability_stabemaxcm_base_v100_signal,
    f41urs_f41_utility_roic_stability_stabemaxcm_base_v101_signal,
    f41urs_f41_utility_roic_stability_stabemaxcm_base_v102_signal,
    f41urs_f41_utility_roic_stability_stabemaxcm63_base_v103_signal,
    f41urs_f41_utility_roic_stability_stabemaxcm63_base_v104_signal,
    f41urs_f41_utility_roic_stability_stabemaxcm63_base_v105_signal,
    f41urs_f41_utility_roic_stability_stabemaxcm126_base_v106_signal,
    f41urs_f41_utility_roic_stability_stabemaxcm126_base_v107_signal,
    f41urs_f41_utility_roic_stability_stabemaxcm126_base_v108_signal,
    f41urs_f41_utility_roic_stability_stabemaxcz_base_v109_signal,
    f41urs_f41_utility_roic_stability_stabemaxcz_base_v110_signal,
    f41urs_f41_utility_roic_stability_stabemaxcz_base_v111_signal,
    f41urs_f41_utility_roic_stability_stabemaxcr_base_v112_signal,
    f41urs_f41_utility_roic_stability_stabemaxcr_base_v113_signal,
    f41urs_f41_utility_roic_stability_stabemaxcr_base_v114_signal,
    f41urs_f41_utility_roic_stability_stabemaxcr63_base_v115_signal,
    f41urs_f41_utility_roic_stability_stabemaxcr63_base_v116_signal,
    f41urs_f41_utility_roic_stability_stabemaxcr63_base_v117_signal,
    f41urs_f41_utility_roic_stability_stababsxc_base_v118_signal,
    f41urs_f41_utility_roic_stability_stababsxlc_base_v119_signal,
    f41urs_f41_utility_roic_stability_stababsdc_base_v120_signal,
    f41urs_f41_utility_roic_stability_stababsxcm_base_v121_signal,
    f41urs_f41_utility_roic_stability_stababsxcm63_base_v122_signal,
    f41urs_f41_utility_roic_stability_stababsxcm126_base_v123_signal,
    f41urs_f41_utility_roic_stability_stababsxcz_base_v124_signal,
    f41urs_f41_utility_roic_stability_stababsxcr_base_v125_signal,
    f41urs_f41_utility_roic_stability_stababsxcr63_base_v126_signal,
    f41urs_f41_utility_roic_stability_stablogxc_base_v127_signal,
    f41urs_f41_utility_roic_stability_stablogxlc_base_v128_signal,
    f41urs_f41_utility_roic_stability_stablogdc_base_v129_signal,
    f41urs_f41_utility_roic_stability_stablogxcm_base_v130_signal,
    f41urs_f41_utility_roic_stability_stablogxcm63_base_v131_signal,
    f41urs_f41_utility_roic_stability_stablogxcm126_base_v132_signal,
    f41urs_f41_utility_roic_stability_stablogxcz_base_v133_signal,
    f41urs_f41_utility_roic_stability_stablogxcr_base_v134_signal,
    f41urs_f41_utility_roic_stability_stablogxcr63_base_v135_signal,
    f41urs_f41_utility_roic_stability_stabsignxc_base_v136_signal,
    f41urs_f41_utility_roic_stability_stabsignxlc_base_v137_signal,
    f41urs_f41_utility_roic_stability_stabsigndc_base_v138_signal,
    f41urs_f41_utility_roic_stability_stabsignxcm_base_v139_signal,
    f41urs_f41_utility_roic_stability_stabsignxcm63_base_v140_signal,
    f41urs_f41_utility_roic_stability_stabsignxcm126_base_v141_signal,
    f41urs_f41_utility_roic_stability_stabsignxcz_base_v142_signal,
    f41urs_f41_utility_roic_stability_stabsignxcr_base_v143_signal,
    f41urs_f41_utility_roic_stability_stabsignxcr63_base_v144_signal,
    f41urs_f41_utility_roic_stability_stabsqxc_base_v145_signal,
    f41urs_f41_utility_roic_stability_stabsqxlc_base_v146_signal,
    f41urs_f41_utility_roic_stability_stabsqdc_base_v147_signal,
    f41urs_f41_utility_roic_stability_stabsqxcm_base_v148_signal,
    f41urs_f41_utility_roic_stability_stabsqxcm63_base_v149_signal,
    f41urs_f41_utility_roic_stability_stabsqxcm126_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F41_UTILITY_ROIC_STABILITY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f41_roic_stability", "_f41_roic_compound", "_f41_roic_quality")
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
    print(f"OK f41_utility_roic_stability_base_076_150_claude: {n_features} features pass")
