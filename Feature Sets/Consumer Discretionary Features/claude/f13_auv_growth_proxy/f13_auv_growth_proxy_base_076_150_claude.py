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

def _f13_revenue_per_ppe(revenue, ppnenet):
    return revenue / ppnenet.replace(0, np.nan)


def _f13_auv_growth(revenue, ppnenet, w):
    rpp = revenue / ppnenet.replace(0, np.nan)
    return rpp.pct_change(periods=w)


def _f13_unit_volume_trajectory(revenue, ppnenet, w):
    rpp = revenue / ppnenet.replace(0, np.nan)
    g1 = rpp.pct_change(periods=w)
    g2 = rpp.pct_change(periods=2 * w)
    return g1 + 0.5 * g2


# ===== features =====

def f13auv_f13_auv_growth_proxy_auvg_sclose_378d_base_v076_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 378) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_xclose_504d_base_v077_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_zclose_504d_base_v078_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 504) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_mclose_504d_base_v079_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 504) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvg_sclose_504d_base_v080_signal(revenue, ppnenet, closeadj):
    result = _f13_auv_growth(revenue, ppnenet, 504) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_xclose_5d_base_v081_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_zclose_5d_base_v082_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_mclose_5d_base_v083_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_sclose_5d_base_v084_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_xclose_10d_base_v085_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_zclose_10d_base_v086_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_mclose_10d_base_v087_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_sclose_10d_base_v088_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_xclose_21d_base_v089_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_zclose_21d_base_v090_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_mclose_21d_base_v091_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_sclose_21d_base_v092_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_xclose_42d_base_v093_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_zclose_42d_base_v094_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_mclose_42d_base_v095_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_sclose_42d_base_v096_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_xclose_63d_base_v097_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_zclose_63d_base_v098_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_mclose_63d_base_v099_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_sclose_63d_base_v100_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_xclose_126d_base_v101_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_zclose_126d_base_v102_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 126) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_mclose_126d_base_v103_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 126) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_sclose_126d_base_v104_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_xclose_189d_base_v105_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_zclose_189d_base_v106_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 189) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_mclose_189d_base_v107_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 189) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_sclose_189d_base_v108_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 189) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_xclose_252d_base_v109_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_zclose_252d_base_v110_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 252) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_mclose_252d_base_v111_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 252) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_sclose_252d_base_v112_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 252) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_xclose_378d_base_v113_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_zclose_378d_base_v114_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 378) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_mclose_378d_base_v115_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 378) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_sclose_378d_base_v116_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 378) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_xclose_504d_base_v117_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_zclose_504d_base_v118_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 504) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_mclose_504d_base_v119_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 504) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_uvt_sclose_504d_base_v120_signal(revenue, ppnenet, closeadj):
    result = _f13_unit_volume_trajectory(revenue, ppnenet, 504) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rppz0_21d_base_v121_signal(revenue, ppnenet, closeadj):
    result = _z(_f13_revenue_per_ppe(revenue, ppnenet), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rppz1_42d_base_v122_signal(revenue, ppnenet, closeadj):
    result = _z(_f13_revenue_per_ppe(revenue, ppnenet), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rppz2_63d_base_v123_signal(revenue, ppnenet, closeadj):
    result = _z(_f13_revenue_per_ppe(revenue, ppnenet), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rppz3_126d_base_v124_signal(revenue, ppnenet, closeadj):
    result = _z(_f13_revenue_per_ppe(revenue, ppnenet), 126) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rppz4_189d_base_v125_signal(revenue, ppnenet, closeadj):
    result = _z(_f13_revenue_per_ppe(revenue, ppnenet), 189) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rppz5_252d_base_v126_signal(revenue, ppnenet, closeadj):
    result = _z(_f13_revenue_per_ppe(revenue, ppnenet), 252) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rppz6_378d_base_v127_signal(revenue, ppnenet, closeadj):
    result = _z(_f13_revenue_per_ppe(revenue, ppnenet), 378) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rppz7_504d_base_v128_signal(revenue, ppnenet, closeadj):
    result = _z(_f13_revenue_per_ppe(revenue, ppnenet), 504) * (closeadj - _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rppz8_10d_base_v129_signal(revenue, ppnenet, closeadj):
    result = _z(_f13_revenue_per_ppe(revenue, ppnenet), 10) * (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rppz9_5d_base_v130_signal(revenue, ppnenet, closeadj):
    result = _z(_f13_revenue_per_ppe(revenue, ppnenet), 5) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rppsd0_21d_base_v131_signal(revenue, ppnenet, closeadj):
    result = _std(_f13_revenue_per_ppe(revenue, ppnenet), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rppsd1_42d_base_v132_signal(revenue, ppnenet, closeadj):
    result = _std(_f13_revenue_per_ppe(revenue, ppnenet), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rppsd2_63d_base_v133_signal(revenue, ppnenet, closeadj):
    result = _std(_f13_revenue_per_ppe(revenue, ppnenet), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rppsd3_126d_base_v134_signal(revenue, ppnenet, closeadj):
    result = _std(_f13_revenue_per_ppe(revenue, ppnenet), 126) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rppsd4_189d_base_v135_signal(revenue, ppnenet, closeadj):
    result = _std(_f13_revenue_per_ppe(revenue, ppnenet), 189) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rppsd5_252d_base_v136_signal(revenue, ppnenet, closeadj):
    result = _std(_f13_revenue_per_ppe(revenue, ppnenet), 252) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rppsd6_378d_base_v137_signal(revenue, ppnenet, closeadj):
    result = _std(_f13_revenue_per_ppe(revenue, ppnenet), 378) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rppsd7_504d_base_v138_signal(revenue, ppnenet, closeadj):
    result = _std(_f13_revenue_per_ppe(revenue, ppnenet), 504) * (closeadj - _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rppsd8_10d_base_v139_signal(revenue, ppnenet, closeadj):
    result = _std(_f13_revenue_per_ppe(revenue, ppnenet), 10) * (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_rppsd9_5d_base_v140_signal(revenue, ppnenet, closeadj):
    result = _std(_f13_revenue_per_ppe(revenue, ppnenet), 5) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvgm0_21d_base_v141_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_auv_growth(revenue, ppnenet, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvgm1_42d_base_v142_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_auv_growth(revenue, ppnenet, 42), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvgm2_63d_base_v143_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_auv_growth(revenue, ppnenet, 63), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvgm3_126d_base_v144_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_auv_growth(revenue, ppnenet, 126), 21) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvgm4_189d_base_v145_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_auv_growth(revenue, ppnenet, 189), 21) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvgm5_252d_base_v146_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_auv_growth(revenue, ppnenet, 252), 21) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvgm6_378d_base_v147_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_auv_growth(revenue, ppnenet, 378), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvgm7_504d_base_v148_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_auv_growth(revenue, ppnenet, 504), 21) * (closeadj - _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvgm8_10d_base_v149_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_auv_growth(revenue, ppnenet, 10), 21) * (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


def f13auv_f13_auv_growth_proxy_auvgm9_5d_base_v150_signal(revenue, ppnenet, closeadj):
    result = _mean(_f13_auv_growth(revenue, ppnenet, 5), 21) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f13auv_f13_auv_growth_proxy_auvg_sclose_378d_base_v076_signal,
    f13auv_f13_auv_growth_proxy_auvg_xclose_504d_base_v077_signal,
    f13auv_f13_auv_growth_proxy_auvg_zclose_504d_base_v078_signal,
    f13auv_f13_auv_growth_proxy_auvg_mclose_504d_base_v079_signal,
    f13auv_f13_auv_growth_proxy_auvg_sclose_504d_base_v080_signal,
    f13auv_f13_auv_growth_proxy_uvt_xclose_5d_base_v081_signal,
    f13auv_f13_auv_growth_proxy_uvt_zclose_5d_base_v082_signal,
    f13auv_f13_auv_growth_proxy_uvt_mclose_5d_base_v083_signal,
    f13auv_f13_auv_growth_proxy_uvt_sclose_5d_base_v084_signal,
    f13auv_f13_auv_growth_proxy_uvt_xclose_10d_base_v085_signal,
    f13auv_f13_auv_growth_proxy_uvt_zclose_10d_base_v086_signal,
    f13auv_f13_auv_growth_proxy_uvt_mclose_10d_base_v087_signal,
    f13auv_f13_auv_growth_proxy_uvt_sclose_10d_base_v088_signal,
    f13auv_f13_auv_growth_proxy_uvt_xclose_21d_base_v089_signal,
    f13auv_f13_auv_growth_proxy_uvt_zclose_21d_base_v090_signal,
    f13auv_f13_auv_growth_proxy_uvt_mclose_21d_base_v091_signal,
    f13auv_f13_auv_growth_proxy_uvt_sclose_21d_base_v092_signal,
    f13auv_f13_auv_growth_proxy_uvt_xclose_42d_base_v093_signal,
    f13auv_f13_auv_growth_proxy_uvt_zclose_42d_base_v094_signal,
    f13auv_f13_auv_growth_proxy_uvt_mclose_42d_base_v095_signal,
    f13auv_f13_auv_growth_proxy_uvt_sclose_42d_base_v096_signal,
    f13auv_f13_auv_growth_proxy_uvt_xclose_63d_base_v097_signal,
    f13auv_f13_auv_growth_proxy_uvt_zclose_63d_base_v098_signal,
    f13auv_f13_auv_growth_proxy_uvt_mclose_63d_base_v099_signal,
    f13auv_f13_auv_growth_proxy_uvt_sclose_63d_base_v100_signal,
    f13auv_f13_auv_growth_proxy_uvt_xclose_126d_base_v101_signal,
    f13auv_f13_auv_growth_proxy_uvt_zclose_126d_base_v102_signal,
    f13auv_f13_auv_growth_proxy_uvt_mclose_126d_base_v103_signal,
    f13auv_f13_auv_growth_proxy_uvt_sclose_126d_base_v104_signal,
    f13auv_f13_auv_growth_proxy_uvt_xclose_189d_base_v105_signal,
    f13auv_f13_auv_growth_proxy_uvt_zclose_189d_base_v106_signal,
    f13auv_f13_auv_growth_proxy_uvt_mclose_189d_base_v107_signal,
    f13auv_f13_auv_growth_proxy_uvt_sclose_189d_base_v108_signal,
    f13auv_f13_auv_growth_proxy_uvt_xclose_252d_base_v109_signal,
    f13auv_f13_auv_growth_proxy_uvt_zclose_252d_base_v110_signal,
    f13auv_f13_auv_growth_proxy_uvt_mclose_252d_base_v111_signal,
    f13auv_f13_auv_growth_proxy_uvt_sclose_252d_base_v112_signal,
    f13auv_f13_auv_growth_proxy_uvt_xclose_378d_base_v113_signal,
    f13auv_f13_auv_growth_proxy_uvt_zclose_378d_base_v114_signal,
    f13auv_f13_auv_growth_proxy_uvt_mclose_378d_base_v115_signal,
    f13auv_f13_auv_growth_proxy_uvt_sclose_378d_base_v116_signal,
    f13auv_f13_auv_growth_proxy_uvt_xclose_504d_base_v117_signal,
    f13auv_f13_auv_growth_proxy_uvt_zclose_504d_base_v118_signal,
    f13auv_f13_auv_growth_proxy_uvt_mclose_504d_base_v119_signal,
    f13auv_f13_auv_growth_proxy_uvt_sclose_504d_base_v120_signal,
    f13auv_f13_auv_growth_proxy_rppz0_21d_base_v121_signal,
    f13auv_f13_auv_growth_proxy_rppz1_42d_base_v122_signal,
    f13auv_f13_auv_growth_proxy_rppz2_63d_base_v123_signal,
    f13auv_f13_auv_growth_proxy_rppz3_126d_base_v124_signal,
    f13auv_f13_auv_growth_proxy_rppz4_189d_base_v125_signal,
    f13auv_f13_auv_growth_proxy_rppz5_252d_base_v126_signal,
    f13auv_f13_auv_growth_proxy_rppz6_378d_base_v127_signal,
    f13auv_f13_auv_growth_proxy_rppz7_504d_base_v128_signal,
    f13auv_f13_auv_growth_proxy_rppz8_10d_base_v129_signal,
    f13auv_f13_auv_growth_proxy_rppz9_5d_base_v130_signal,
    f13auv_f13_auv_growth_proxy_rppsd0_21d_base_v131_signal,
    f13auv_f13_auv_growth_proxy_rppsd1_42d_base_v132_signal,
    f13auv_f13_auv_growth_proxy_rppsd2_63d_base_v133_signal,
    f13auv_f13_auv_growth_proxy_rppsd3_126d_base_v134_signal,
    f13auv_f13_auv_growth_proxy_rppsd4_189d_base_v135_signal,
    f13auv_f13_auv_growth_proxy_rppsd5_252d_base_v136_signal,
    f13auv_f13_auv_growth_proxy_rppsd6_378d_base_v137_signal,
    f13auv_f13_auv_growth_proxy_rppsd7_504d_base_v138_signal,
    f13auv_f13_auv_growth_proxy_rppsd8_10d_base_v139_signal,
    f13auv_f13_auv_growth_proxy_rppsd9_5d_base_v140_signal,
    f13auv_f13_auv_growth_proxy_auvgm0_21d_base_v141_signal,
    f13auv_f13_auv_growth_proxy_auvgm1_42d_base_v142_signal,
    f13auv_f13_auv_growth_proxy_auvgm2_63d_base_v143_signal,
    f13auv_f13_auv_growth_proxy_auvgm3_126d_base_v144_signal,
    f13auv_f13_auv_growth_proxy_auvgm4_189d_base_v145_signal,
    f13auv_f13_auv_growth_proxy_auvgm5_252d_base_v146_signal,
    f13auv_f13_auv_growth_proxy_auvgm6_378d_base_v147_signal,
    f13auv_f13_auv_growth_proxy_auvgm7_504d_base_v148_signal,
    f13auv_f13_auv_growth_proxy_auvgm8_10d_base_v149_signal,
    f13auv_f13_auv_growth_proxy_auvgm9_5d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F13_AUV_GROWTH_PROXY_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f13_revenue_per_ppe", "_f13_auv_growth", "_f13_unit_volume_trajectory")
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
    print(f"OK f13_auv_growth_proxy_base_076_150_claude: {n_features} features pass")
