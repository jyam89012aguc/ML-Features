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
def _f47_quiet_fcf_growth(fcf, w):
    m = fcf.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = fcf.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    return m / sd


def _f47_low_attention_growth(closeadj, volume, fcf, w):
    dv = (closeadj * volume).rolling(w, min_periods=max(1, w // 2)).mean()
    g = fcf.rolling(w, min_periods=max(1, w // 2)).mean()
    return g * closeadj / dv.replace(0, np.nan)


def _f47_hidden_quality_score(fcf, roic, w):
    fg = fcf.rolling(w, min_periods=max(1, w // 2)).mean()
    rq = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    return fg * rq


# ===== features =====
def f47hrc_f47_hidden_renewable_compounder_hq_fr_84d_s01_base_v076_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 84)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_84d_s01_base_v077_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 84)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_84d_s01_base_v078_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 84)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_84d_s01_base_v079_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 84)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_105d_s01_base_v080_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 105)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_105d_s01_base_v081_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 105)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_105d_s01_base_v082_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 105)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_105d_s01_base_v083_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 105)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_105d_s01_base_v084_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 105)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_105d_s01_base_v085_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 105)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_105d_s01_base_v086_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 105)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_105d_s01_base_v087_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 105)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_105d_s01_base_v088_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 105)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_105d_s01_base_v089_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 105)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_105d_s01_base_v090_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 105)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_105d_s01_base_v091_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 105)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_105d_s01_base_v092_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 105)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_105d_s01_base_v093_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 105)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_105d_s01_base_v094_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 105)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_105d_s01_base_v095_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 105)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_105d_s01_base_v096_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 105)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_105d_s01_base_v097_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 105)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_105d_s01_base_v098_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 105)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_105d_s01_base_v099_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 105)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_105d_s01_base_v100_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 105)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_105d_s01_base_v101_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 105)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_105d_s01_base_v102_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 105)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_105d_s01_base_v103_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 105)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_126d_s01_base_v104_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 126)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_126d_s01_base_v105_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 126)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_126d_s01_base_v106_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_126d_s01_base_v107_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 126)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_126d_s01_base_v108_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 126)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_126d_s01_base_v109_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 126)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_126d_s01_base_v110_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 126)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_126d_s01_base_v111_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 126)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_126d_s01_base_v112_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 126)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_126d_s01_base_v113_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 126)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_126d_s01_base_v114_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_126d_s01_base_v115_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 126)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_126d_s01_base_v116_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 126)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_126d_s01_base_v117_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 126)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_126d_s01_base_v118_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 126)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_126d_s01_base_v119_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 126)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_126d_s01_base_v120_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 126)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_126d_s01_base_v121_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 126)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_126d_s01_base_v122_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_126d_s01_base_v123_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 126)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_126d_s01_base_v124_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 126)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_126d_s01_base_v125_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 126)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_126d_s01_base_v126_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 126)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_126d_s01_base_v127_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 126)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_147d_s01_base_v128_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 147)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_147d_s01_base_v129_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 147)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_147d_s01_base_v130_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 147)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_147d_s01_base_v131_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 147)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_147d_s01_base_v132_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 147)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_147d_s01_base_v133_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 147)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_147d_s01_base_v134_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 147)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_147d_s01_base_v135_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 147)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_147d_s01_base_v136_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 147)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_147d_s01_base_v137_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 147)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_147d_s01_base_v138_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 147)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_147d_s01_base_v139_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 147)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_147d_s01_base_v140_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 147)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_147d_s01_base_v141_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 147)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_147d_s01_base_v142_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 147)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_147d_s01_base_v143_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 147)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_147d_s01_base_v144_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 147)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_147d_s01_base_v145_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 147)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_147d_s01_base_v146_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 147)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_147d_s01_base_v147_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 147)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_147d_s01_base_v148_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 147)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_147d_s01_base_v149_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 147)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_147d_s01_base_v150_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 147)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f47hrc_f47_hidden_renewable_compounder_hq_fr_84d_s01_base_v076_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_84d_s01_base_v077_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_84d_s01_base_v078_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_84d_s01_base_v079_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_105d_s01_base_v080_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_105d_s01_base_v081_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_105d_s01_base_v082_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_105d_s01_base_v083_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_105d_s01_base_v084_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_105d_s01_base_v085_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_105d_s01_base_v086_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_105d_s01_base_v087_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_105d_s01_base_v088_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_105d_s01_base_v089_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_105d_s01_base_v090_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_105d_s01_base_v091_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_105d_s01_base_v092_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_105d_s01_base_v093_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_105d_s01_base_v094_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_105d_s01_base_v095_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_105d_s01_base_v096_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_105d_s01_base_v097_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_105d_s01_base_v098_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_105d_s01_base_v099_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_105d_s01_base_v100_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_105d_s01_base_v101_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_105d_s01_base_v102_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_105d_s01_base_v103_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_126d_s01_base_v104_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_126d_s01_base_v105_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_126d_s01_base_v106_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_126d_s01_base_v107_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_126d_s01_base_v108_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_126d_s01_base_v109_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_126d_s01_base_v110_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_126d_s01_base_v111_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_126d_s01_base_v112_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_126d_s01_base_v113_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_126d_s01_base_v114_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_126d_s01_base_v115_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_126d_s01_base_v116_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_126d_s01_base_v117_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_126d_s01_base_v118_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_126d_s01_base_v119_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_126d_s01_base_v120_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_126d_s01_base_v121_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_126d_s01_base_v122_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_126d_s01_base_v123_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_126d_s01_base_v124_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_126d_s01_base_v125_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_126d_s01_base_v126_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_126d_s01_base_v127_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_147d_s01_base_v128_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_147d_s01_base_v129_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_147d_s01_base_v130_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_147d_s01_base_v131_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_147d_s01_base_v132_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_147d_s01_base_v133_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_147d_s01_base_v134_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_147d_s01_base_v135_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_147d_s01_base_v136_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_147d_s01_base_v137_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_147d_s01_base_v138_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_147d_s01_base_v139_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_147d_s01_base_v140_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_147d_s01_base_v141_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_147d_s01_base_v142_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_147d_s01_base_v143_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_147d_s01_base_v144_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_147d_s01_base_v145_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_147d_s01_base_v146_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_147d_s01_base_v147_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_147d_s01_base_v148_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_147d_s01_base_v149_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_147d_s01_base_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F47_HIDDEN_RENEWABLE_COMPOUNDER_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    roic    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    cols = {"closeadj": closeadj, "fcf": fcf, "roic": roic, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f47_quiet_fcf_growth", "_f47_low_attention_growth", "_f47_hidden_quality_score",)
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
    print(f"OK f47_hidden_renewable_compounder_base_076_150_claude: {n_features} features pass")
