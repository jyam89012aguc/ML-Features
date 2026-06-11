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
def _f47_quiet_growth(fcf, w):
    g = fcf.pct_change(periods=w)
    smooth = g.rolling(w, min_periods=max(1, w // 2)).mean()
    stab = g.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    return smooth / stab


def _f47_low_attention_growth(close, volume, fcf, w):
    dv = (close * volume).rolling(w, min_periods=max(1, w // 2)).mean()
    g = fcf.pct_change(periods=w)
    return g / dv.replace(0, np.nan) * close


def _f47_hidden_quality_score(fcf, roic, w):
    g = fcf.pct_change(periods=w).rolling(w, min_periods=max(1, w // 2)).mean()
    q = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    return g * q



# ===== features =====

def f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose63_126d_base_v076_signal(fcf, closeadj):
    result = (_f47_quiet_growth(fcf, 126)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose63_126d_base_v077_signal(closeadj, volume, fcf):
    result = (_f47_low_attention_growth(closeadj, volume, fcf, 126)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose63_126d_base_v078_signal(fcf, roic, closeadj):
    result = (_f47_hidden_quality_score(fcf, roic, 126)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose63_189d_base_v079_signal(fcf, closeadj):
    result = (_f47_quiet_growth(fcf, 189)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose63_189d_base_v080_signal(closeadj, volume, fcf):
    result = (_f47_low_attention_growth(closeadj, volume, fcf, 189)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose63_189d_base_v081_signal(fcf, roic, closeadj):
    result = (_f47_hidden_quality_score(fcf, roic, 189)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose63_252d_base_v082_signal(fcf, closeadj):
    result = (_f47_quiet_growth(fcf, 252)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose63_252d_base_v083_signal(closeadj, volume, fcf):
    result = (_f47_low_attention_growth(closeadj, volume, fcf, 252)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose63_252d_base_v084_signal(fcf, roic, closeadj):
    result = (_f47_hidden_quality_score(fcf, roic, 252)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose63_378d_base_v085_signal(fcf, closeadj):
    result = (_f47_quiet_growth(fcf, 378)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose63_378d_base_v086_signal(closeadj, volume, fcf):
    result = (_f47_low_attention_growth(closeadj, volume, fcf, 378)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose63_378d_base_v087_signal(fcf, roic, closeadj):
    result = (_f47_hidden_quality_score(fcf, roic, 378)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose63_504d_base_v088_signal(fcf, closeadj):
    result = (_f47_quiet_growth(fcf, 504)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose63_504d_base_v089_signal(closeadj, volume, fcf):
    result = (_f47_low_attention_growth(closeadj, volume, fcf, 504)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose63_504d_base_v090_signal(fcf, roic, closeadj):
    result = (_f47_hidden_quality_score(fcf, roic, 504)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose5_5d_base_v091_signal(fcf, closeadj):
    result = (_f47_quiet_growth(fcf, 5)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose5_5d_base_v092_signal(closeadj, volume, fcf):
    result = (_f47_low_attention_growth(closeadj, volume, fcf, 5)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose5_5d_base_v093_signal(fcf, roic, closeadj):
    result = (_f47_hidden_quality_score(fcf, roic, 5)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose5_10d_base_v094_signal(fcf, closeadj):
    result = (_f47_quiet_growth(fcf, 10)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose5_10d_base_v095_signal(closeadj, volume, fcf):
    result = (_f47_low_attention_growth(closeadj, volume, fcf, 10)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose5_10d_base_v096_signal(fcf, roic, closeadj):
    result = (_f47_hidden_quality_score(fcf, roic, 10)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose5_21d_base_v097_signal(fcf, closeadj):
    result = (_f47_quiet_growth(fcf, 21)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose5_21d_base_v098_signal(closeadj, volume, fcf):
    result = (_f47_low_attention_growth(closeadj, volume, fcf, 21)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose5_21d_base_v099_signal(fcf, roic, closeadj):
    result = (_f47_hidden_quality_score(fcf, roic, 21)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose5_42d_base_v100_signal(fcf, closeadj):
    result = (_f47_quiet_growth(fcf, 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose5_42d_base_v101_signal(closeadj, volume, fcf):
    result = (_f47_low_attention_growth(closeadj, volume, fcf, 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose5_42d_base_v102_signal(fcf, roic, closeadj):
    result = (_f47_hidden_quality_score(fcf, roic, 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose5_63d_base_v103_signal(fcf, closeadj):
    result = (_f47_quiet_growth(fcf, 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose5_63d_base_v104_signal(closeadj, volume, fcf):
    result = (_f47_low_attention_growth(closeadj, volume, fcf, 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose5_63d_base_v105_signal(fcf, roic, closeadj):
    result = (_f47_hidden_quality_score(fcf, roic, 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose5_126d_base_v106_signal(fcf, closeadj):
    result = (_f47_quiet_growth(fcf, 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose5_126d_base_v107_signal(closeadj, volume, fcf):
    result = (_f47_low_attention_growth(closeadj, volume, fcf, 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose5_126d_base_v108_signal(fcf, roic, closeadj):
    result = (_f47_hidden_quality_score(fcf, roic, 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose5_189d_base_v109_signal(fcf, closeadj):
    result = (_f47_quiet_growth(fcf, 189)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose5_189d_base_v110_signal(closeadj, volume, fcf):
    result = (_f47_low_attention_growth(closeadj, volume, fcf, 189)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose5_189d_base_v111_signal(fcf, roic, closeadj):
    result = (_f47_hidden_quality_score(fcf, roic, 189)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose5_252d_base_v112_signal(fcf, closeadj):
    result = (_f47_quiet_growth(fcf, 252)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose5_252d_base_v113_signal(closeadj, volume, fcf):
    result = (_f47_low_attention_growth(closeadj, volume, fcf, 252)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose5_252d_base_v114_signal(fcf, roic, closeadj):
    result = (_f47_hidden_quality_score(fcf, roic, 252)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose5_378d_base_v115_signal(fcf, closeadj):
    result = (_f47_quiet_growth(fcf, 378)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose5_378d_base_v116_signal(closeadj, volume, fcf):
    result = (_f47_low_attention_growth(closeadj, volume, fcf, 378)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose5_378d_base_v117_signal(fcf, roic, closeadj):
    result = (_f47_hidden_quality_score(fcf, roic, 378)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose5_504d_base_v118_signal(fcf, closeadj):
    result = (_f47_quiet_growth(fcf, 504)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose5_504d_base_v119_signal(closeadj, volume, fcf):
    result = (_f47_low_attention_growth(closeadj, volume, fcf, 504)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose5_504d_base_v120_signal(fcf, roic, closeadj):
    result = (_f47_hidden_quality_score(fcf, roic, 504)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose126_5d_base_v121_signal(fcf, closeadj):
    result = (_f47_quiet_growth(fcf, 5)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose126_5d_base_v122_signal(closeadj, volume, fcf):
    result = (_f47_low_attention_growth(closeadj, volume, fcf, 5)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose126_5d_base_v123_signal(fcf, roic, closeadj):
    result = (_f47_hidden_quality_score(fcf, roic, 5)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose126_10d_base_v124_signal(fcf, closeadj):
    result = (_f47_quiet_growth(fcf, 10)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose126_10d_base_v125_signal(closeadj, volume, fcf):
    result = (_f47_low_attention_growth(closeadj, volume, fcf, 10)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose126_10d_base_v126_signal(fcf, roic, closeadj):
    result = (_f47_hidden_quality_score(fcf, roic, 10)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose126_21d_base_v127_signal(fcf, closeadj):
    result = (_f47_quiet_growth(fcf, 21)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose126_21d_base_v128_signal(closeadj, volume, fcf):
    result = (_f47_low_attention_growth(closeadj, volume, fcf, 21)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose126_21d_base_v129_signal(fcf, roic, closeadj):
    result = (_f47_hidden_quality_score(fcf, roic, 21)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose126_42d_base_v130_signal(fcf, closeadj):
    result = (_f47_quiet_growth(fcf, 42)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose126_42d_base_v131_signal(closeadj, volume, fcf):
    result = (_f47_low_attention_growth(closeadj, volume, fcf, 42)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose126_42d_base_v132_signal(fcf, roic, closeadj):
    result = (_f47_hidden_quality_score(fcf, roic, 42)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose126_63d_base_v133_signal(fcf, closeadj):
    result = (_f47_quiet_growth(fcf, 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose126_63d_base_v134_signal(closeadj, volume, fcf):
    result = (_f47_low_attention_growth(closeadj, volume, fcf, 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose126_63d_base_v135_signal(fcf, roic, closeadj):
    result = (_f47_hidden_quality_score(fcf, roic, 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose126_126d_base_v136_signal(fcf, closeadj):
    result = (_f47_quiet_growth(fcf, 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose126_126d_base_v137_signal(closeadj, volume, fcf):
    result = (_f47_low_attention_growth(closeadj, volume, fcf, 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose126_126d_base_v138_signal(fcf, roic, closeadj):
    result = (_f47_hidden_quality_score(fcf, roic, 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose126_189d_base_v139_signal(fcf, closeadj):
    result = (_f47_quiet_growth(fcf, 189)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose126_189d_base_v140_signal(closeadj, volume, fcf):
    result = (_f47_low_attention_growth(closeadj, volume, fcf, 189)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose126_189d_base_v141_signal(fcf, roic, closeadj):
    result = (_f47_hidden_quality_score(fcf, roic, 189)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose126_252d_base_v142_signal(fcf, closeadj):
    result = (_f47_quiet_growth(fcf, 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose126_252d_base_v143_signal(closeadj, volume, fcf):
    result = (_f47_low_attention_growth(closeadj, volume, fcf, 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose126_252d_base_v144_signal(fcf, roic, closeadj):
    result = (_f47_hidden_quality_score(fcf, roic, 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose126_378d_base_v145_signal(fcf, closeadj):
    result = (_f47_quiet_growth(fcf, 378)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose126_378d_base_v146_signal(closeadj, volume, fcf):
    result = (_f47_low_attention_growth(closeadj, volume, fcf, 378)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose126_378d_base_v147_signal(fcf, roic, closeadj):
    result = (_f47_hidden_quality_score(fcf, roic, 378)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose126_504d_base_v148_signal(fcf, closeadj):
    result = (_f47_quiet_growth(fcf, 504)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose126_504d_base_v149_signal(closeadj, volume, fcf):
    result = (_f47_low_attention_growth(closeadj, volume, fcf, 504)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose126_504d_base_v150_signal(fcf, roic, closeadj):
    result = (_f47_hidden_quality_score(fcf, roic, 504)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose63_126d_base_v076_signal,
    f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose63_126d_base_v077_signal,
    f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose63_126d_base_v078_signal,
    f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose63_189d_base_v079_signal,
    f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose63_189d_base_v080_signal,
    f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose63_189d_base_v081_signal,
    f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose63_252d_base_v082_signal,
    f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose63_252d_base_v083_signal,
    f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose63_252d_base_v084_signal,
    f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose63_378d_base_v085_signal,
    f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose63_378d_base_v086_signal,
    f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose63_378d_base_v087_signal,
    f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose63_504d_base_v088_signal,
    f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose63_504d_base_v089_signal,
    f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose63_504d_base_v090_signal,
    f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose5_5d_base_v091_signal,
    f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose5_5d_base_v092_signal,
    f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose5_5d_base_v093_signal,
    f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose5_10d_base_v094_signal,
    f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose5_10d_base_v095_signal,
    f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose5_10d_base_v096_signal,
    f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose5_21d_base_v097_signal,
    f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose5_21d_base_v098_signal,
    f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose5_21d_base_v099_signal,
    f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose5_42d_base_v100_signal,
    f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose5_42d_base_v101_signal,
    f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose5_42d_base_v102_signal,
    f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose5_63d_base_v103_signal,
    f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose5_63d_base_v104_signal,
    f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose5_63d_base_v105_signal,
    f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose5_126d_base_v106_signal,
    f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose5_126d_base_v107_signal,
    f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose5_126d_base_v108_signal,
    f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose5_189d_base_v109_signal,
    f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose5_189d_base_v110_signal,
    f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose5_189d_base_v111_signal,
    f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose5_252d_base_v112_signal,
    f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose5_252d_base_v113_signal,
    f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose5_252d_base_v114_signal,
    f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose5_378d_base_v115_signal,
    f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose5_378d_base_v116_signal,
    f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose5_378d_base_v117_signal,
    f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose5_504d_base_v118_signal,
    f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose5_504d_base_v119_signal,
    f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose5_504d_base_v120_signal,
    f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose126_5d_base_v121_signal,
    f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose126_5d_base_v122_signal,
    f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose126_5d_base_v123_signal,
    f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose126_10d_base_v124_signal,
    f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose126_10d_base_v125_signal,
    f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose126_10d_base_v126_signal,
    f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose126_21d_base_v127_signal,
    f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose126_21d_base_v128_signal,
    f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose126_21d_base_v129_signal,
    f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose126_42d_base_v130_signal,
    f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose126_42d_base_v131_signal,
    f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose126_42d_base_v132_signal,
    f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose126_63d_base_v133_signal,
    f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose126_63d_base_v134_signal,
    f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose126_63d_base_v135_signal,
    f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose126_126d_base_v136_signal,
    f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose126_126d_base_v137_signal,
    f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose126_126d_base_v138_signal,
    f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose126_189d_base_v139_signal,
    f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose126_189d_base_v140_signal,
    f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose126_189d_base_v141_signal,
    f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose126_252d_base_v142_signal,
    f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose126_252d_base_v143_signal,
    f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose126_252d_base_v144_signal,
    f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose126_378d_base_v145_signal,
    f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose126_378d_base_v146_signal,
    f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose126_378d_base_v147_signal,
    f47hmc_f47_hidden_medtech_compounder_p1_raw_xclose126_504d_base_v148_signal,
    f47hmc_f47_hidden_medtech_compounder_p2_raw_xclose126_504d_base_v149_signal,
    f47hmc_f47_hidden_medtech_compounder_p3_raw_xclose126_504d_base_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F47_HIDDEN_MEDTECH_COMPOUNDER_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high.values, name="high")
    low = pd.Series(low.values, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    eps     = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "netinc": netinc, "fcf": fcf,
        "eps": eps, "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "roic": roic,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f47_quiet_growth", "_f47_low_attention_growth", "_f47_hidden_quality_score")
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
    print(f"OK f47_hidden_medtech_compounder_base_076_150_claude: {n_features} features pass")
