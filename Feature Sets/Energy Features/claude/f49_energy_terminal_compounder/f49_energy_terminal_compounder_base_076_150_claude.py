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
def _f49_quality_composite(roic, fcf, revenue, w):
    rq = roic.rolling(w, min_periods=max(2, w // 2)).mean()
    fy = fcf / revenue.replace(0, np.nan).abs()
    fq = fy.rolling(w, min_periods=max(2, w // 2)).mean()
    return rq + fq


def _f49_compounder_score(roic, ebitdamargin, w):
    rq = roic.rolling(w, min_periods=max(2, w // 2)).mean()
    mq = ebitdamargin.rolling(w, min_periods=max(2, w // 2)).mean()
    return rq * mq


def _f49_terminal_quality(fcf, revenue, roic, w):
    fy = fcf / revenue.replace(0, np.nan).abs()
    fq = fy.rolling(w, min_periods=max(2, w // 2)).mean()
    rq = roic.rolling(w, min_periods=max(2, w // 2)).mean()
    return fq * rq



def etc_f49_energy_terminal_compounder_quality_composite_10d_zN_126_base_v076_signal(roic, fcf, revenue, closeadj):
    result = _z(_f49_quality_composite(roic, fcf, revenue, 10), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_meanN_21_base_v077_signal(roic, fcf, revenue, closeadj):
    result = _mean(_f49_quality_composite(roic, fcf, revenue, 10), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_meanN_42_base_v078_signal(roic, fcf, revenue, closeadj):
    result = _mean(_f49_quality_composite(roic, fcf, revenue, 10), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_meanN_63_base_v079_signal(roic, fcf, revenue, closeadj):
    result = _mean(_f49_quality_composite(roic, fcf, revenue, 10), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_meanN_126_base_v080_signal(roic, fcf, revenue, closeadj):
    result = _mean(_f49_quality_composite(roic, fcf, revenue, 10), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_stdN_21_base_v081_signal(roic, fcf, revenue, closeadj):
    result = _std(_f49_quality_composite(roic, fcf, revenue, 10), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_stdN_42_base_v082_signal(roic, fcf, revenue, closeadj):
    result = _std(_f49_quality_composite(roic, fcf, revenue, 10), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_stdN_63_base_v083_signal(roic, fcf, revenue, closeadj):
    result = _std(_f49_quality_composite(roic, fcf, revenue, 10), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_stdN_126_base_v084_signal(roic, fcf, revenue, closeadj):
    result = _std(_f49_quality_composite(roic, fcf, revenue, 10), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_emaN_21_base_v085_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_emaN_42_base_v086_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).ewm(span=42, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_emaN_63_base_v087_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_emaN_126_base_v088_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_qrank_21_base_v089_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(21, min_periods=max(2, 21 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_qrank_42_base_v090_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(42, min_periods=max(2, 42 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_qrank_63_base_v091_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(63, min_periods=max(2, 63 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_qrank_126_base_v092_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(126, min_periods=max(2, 126 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_diffN_21_base_v093_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_diffN_42_base_v094_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).diff(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_diffN_63_base_v095_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_diffN_126_base_v096_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_absexp_21_base_v097_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_negexp_21_base_v098_signal(roic, fcf, revenue, closeadj):
    result = -(_f49_quality_composite(roic, fcf, revenue, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_tanh_21_base_v099_signal(roic, fcf, revenue, closeadj):
    result = np.tanh(_f49_quality_composite(roic, fcf, revenue, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_invexp_21_base_v100_signal(roic, fcf, revenue, closeadj):
    result = 1.0 / (1.0 + (_f49_quality_composite(roic, fcf, revenue, 10)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_clipz_21_base_v101_signal(roic, fcf, revenue, closeadj):
    result = _z(_f49_quality_composite(roic, fcf, revenue, 10), 21).clip(-5,5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_clipz_42_base_v102_signal(roic, fcf, revenue, closeadj):
    result = _z(_f49_quality_composite(roic, fcf, revenue, 10), 42).clip(-5,5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_clipz_63_base_v103_signal(roic, fcf, revenue, closeadj):
    result = _z(_f49_quality_composite(roic, fcf, revenue, 10), 63).clip(-5,5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_clipz_126_base_v104_signal(roic, fcf, revenue, closeadj):
    result = _z(_f49_quality_composite(roic, fcf, revenue, 10), 126).clip(-5,5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_cubed_21_base_v105_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).pow(3) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_sqrtabs_21_base_v106_signal(roic, fcf, revenue, closeadj):
    result = np.sqrt((_f49_quality_composite(roic, fcf, revenue, 10)).abs() + 1e-9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_logmean_21_base_v107_signal(roic, fcf, revenue, closeadj):
    result = np.log(_mean((_f49_quality_composite(roic, fcf, revenue, 10)).abs() + 1.0, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_logmean_42_base_v108_signal(roic, fcf, revenue, closeadj):
    result = np.log(_mean((_f49_quality_composite(roic, fcf, revenue, 10)).abs() + 1.0, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_logmean_63_base_v109_signal(roic, fcf, revenue, closeadj):
    result = np.log(_mean((_f49_quality_composite(roic, fcf, revenue, 10)).abs() + 1.0, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_logmean_126_base_v110_signal(roic, fcf, revenue, closeadj):
    result = np.log(_mean((_f49_quality_composite(roic, fcf, revenue, 10)).abs() + 1.0, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_medN_21_base_v111_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(21, min_periods=max(2, 21 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_medN_42_base_v112_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(42, min_periods=max(2, 42 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_medN_63_base_v113_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(63, min_periods=max(2, 63 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_medN_126_base_v114_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(126, min_periods=max(2, 126 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_minN_21_base_v115_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(21, min_periods=max(2, 21 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_minN_42_base_v116_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(42, min_periods=max(2, 42 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_minN_63_base_v117_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(63, min_periods=max(2, 63 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_minN_126_base_v118_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(126, min_periods=max(2, 126 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_maxN_21_base_v119_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(21, min_periods=max(2, 21 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_maxN_42_base_v120_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(42, min_periods=max(2, 42 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_maxN_63_base_v121_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(63, min_periods=max(2, 63 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_maxN_126_base_v122_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(126, min_periods=max(2, 126 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_skewN_21_base_v123_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(21, min_periods=max(2, 21 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_skewN_42_base_v124_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(42, min_periods=max(2, 42 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_skewN_63_base_v125_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(63, min_periods=max(2, 63 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_skewN_126_base_v126_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(126, min_periods=max(2, 126 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_kurtN_21_base_v127_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(21, min_periods=max(2, 21 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_kurtN_42_base_v128_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(42, min_periods=max(2, 42 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_kurtN_63_base_v129_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(63, min_periods=max(2, 63 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_kurtN_126_base_v130_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(126, min_periods=max(2, 126 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_sumN_21_base_v131_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(21, min_periods=max(2, 21 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_sumN_42_base_v132_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(42, min_periods=max(2, 42 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_sumN_63_base_v133_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(63, min_periods=max(2, 63 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_10d_sumN_126_base_v134_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)).rolling(126, min_periods=max(2, 126 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_21d_raw_21_base_v135_signal(roic, fcf, revenue):
    result = _f49_quality_composite(roic, fcf, revenue, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_21d_scXclose_21_base_v136_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_21d_logabs_21_base_v137_signal(roic, fcf, revenue, closeadj):
    result = np.log((_f49_quality_composite(roic, fcf, revenue, 21)).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_21d_sign_21_base_v138_signal(roic, fcf, revenue, closeadj):
    result = np.sign(_f49_quality_composite(roic, fcf, revenue, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_21d_signsq_21_base_v139_signal(roic, fcf, revenue, closeadj):
    result = np.sign(_f49_quality_composite(roic, fcf, revenue, 21)) * (_f49_quality_composite(roic, fcf, revenue, 21)).pow(2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_21d_zN_21_base_v140_signal(roic, fcf, revenue, closeadj):
    result = _z(_f49_quality_composite(roic, fcf, revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_21d_zN_42_base_v141_signal(roic, fcf, revenue, closeadj):
    result = _z(_f49_quality_composite(roic, fcf, revenue, 21), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_21d_zN_63_base_v142_signal(roic, fcf, revenue, closeadj):
    result = _z(_f49_quality_composite(roic, fcf, revenue, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_21d_zN_126_base_v143_signal(roic, fcf, revenue, closeadj):
    result = _z(_f49_quality_composite(roic, fcf, revenue, 21), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_21d_meanN_21_base_v144_signal(roic, fcf, revenue, closeadj):
    result = _mean(_f49_quality_composite(roic, fcf, revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_21d_meanN_42_base_v145_signal(roic, fcf, revenue, closeadj):
    result = _mean(_f49_quality_composite(roic, fcf, revenue, 21), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_21d_meanN_63_base_v146_signal(roic, fcf, revenue, closeadj):
    result = _mean(_f49_quality_composite(roic, fcf, revenue, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_21d_meanN_126_base_v147_signal(roic, fcf, revenue, closeadj):
    result = _mean(_f49_quality_composite(roic, fcf, revenue, 21), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_21d_stdN_21_base_v148_signal(roic, fcf, revenue, closeadj):
    result = _std(_f49_quality_composite(roic, fcf, revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_21d_stdN_42_base_v149_signal(roic, fcf, revenue, closeadj):
    result = _std(_f49_quality_composite(roic, fcf, revenue, 21), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_21d_stdN_63_base_v150_signal(roic, fcf, revenue, closeadj):
    result = _std(_f49_quality_composite(roic, fcf, revenue, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    etc_f49_energy_terminal_compounder_quality_composite_10d_zN_126_base_v076_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_meanN_21_base_v077_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_meanN_42_base_v078_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_meanN_63_base_v079_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_meanN_126_base_v080_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_stdN_21_base_v081_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_stdN_42_base_v082_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_stdN_63_base_v083_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_stdN_126_base_v084_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_emaN_21_base_v085_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_emaN_42_base_v086_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_emaN_63_base_v087_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_emaN_126_base_v088_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_qrank_21_base_v089_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_qrank_42_base_v090_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_qrank_63_base_v091_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_qrank_126_base_v092_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_diffN_21_base_v093_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_diffN_42_base_v094_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_diffN_63_base_v095_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_diffN_126_base_v096_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_absexp_21_base_v097_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_negexp_21_base_v098_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_tanh_21_base_v099_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_invexp_21_base_v100_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_clipz_21_base_v101_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_clipz_42_base_v102_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_clipz_63_base_v103_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_clipz_126_base_v104_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_cubed_21_base_v105_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_sqrtabs_21_base_v106_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_logmean_21_base_v107_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_logmean_42_base_v108_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_logmean_63_base_v109_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_logmean_126_base_v110_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_medN_21_base_v111_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_medN_42_base_v112_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_medN_63_base_v113_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_medN_126_base_v114_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_minN_21_base_v115_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_minN_42_base_v116_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_minN_63_base_v117_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_minN_126_base_v118_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_maxN_21_base_v119_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_maxN_42_base_v120_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_maxN_63_base_v121_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_maxN_126_base_v122_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_skewN_21_base_v123_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_skewN_42_base_v124_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_skewN_63_base_v125_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_skewN_126_base_v126_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_kurtN_21_base_v127_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_kurtN_42_base_v128_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_kurtN_63_base_v129_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_kurtN_126_base_v130_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_sumN_21_base_v131_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_sumN_42_base_v132_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_sumN_63_base_v133_signal,
    etc_f49_energy_terminal_compounder_quality_composite_10d_sumN_126_base_v134_signal,
    etc_f49_energy_terminal_compounder_quality_composite_21d_raw_21_base_v135_signal,
    etc_f49_energy_terminal_compounder_quality_composite_21d_scXclose_21_base_v136_signal,
    etc_f49_energy_terminal_compounder_quality_composite_21d_logabs_21_base_v137_signal,
    etc_f49_energy_terminal_compounder_quality_composite_21d_sign_21_base_v138_signal,
    etc_f49_energy_terminal_compounder_quality_composite_21d_signsq_21_base_v139_signal,
    etc_f49_energy_terminal_compounder_quality_composite_21d_zN_21_base_v140_signal,
    etc_f49_energy_terminal_compounder_quality_composite_21d_zN_42_base_v141_signal,
    etc_f49_energy_terminal_compounder_quality_composite_21d_zN_63_base_v142_signal,
    etc_f49_energy_terminal_compounder_quality_composite_21d_zN_126_base_v143_signal,
    etc_f49_energy_terminal_compounder_quality_composite_21d_meanN_21_base_v144_signal,
    etc_f49_energy_terminal_compounder_quality_composite_21d_meanN_42_base_v145_signal,
    etc_f49_energy_terminal_compounder_quality_composite_21d_meanN_63_base_v146_signal,
    etc_f49_energy_terminal_compounder_quality_composite_21d_meanN_126_base_v147_signal,
    etc_f49_energy_terminal_compounder_quality_composite_21d_stdN_21_base_v148_signal,
    etc_f49_energy_terminal_compounder_quality_composite_21d_stdN_42_base_v149_signal,
    etc_f49_energy_terminal_compounder_quality_composite_21d_stdN_63_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F49_ENERGY_TERMINAL_COMPOUNDER_REGISTRY_076_150 = REGISTRY


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
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    eps     = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "netinc": netinc, "fcf": fcf,
        "eps": eps, "ebitdamargin": ebitdamargin, "roic": roic,
    }

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
    print(f"OK {__file__}: {n_features} features pass")
