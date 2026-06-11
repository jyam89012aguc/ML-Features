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

def _f11_revenue_per_asset(revenue, assets):
    return revenue / assets.replace(0, np.nan)


def _f11_ebitda_per_asset(ebitda, assets):
    return ebitda / assets.replace(0, np.nan)


def _f11_unit_econ_score(revenue, ebitda, assets, w):
    rpa = revenue / assets.replace(0, np.nan)
    epa = ebitda / assets.replace(0, np.nan)
    rpa_m = rpa.rolling(w, min_periods=max(1, w // 2)).mean()
    epa_m = epa.rolling(w, min_periods=max(1, w // 2)).mean()
    return rpa_m * 0.5 + epa_m * 0.5


# ===== features =====

def f11rue_f11_restaurant_unit_economics_epa_sclose_378d_base_v076_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 378) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_xclose_504d_base_v077_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_zclose_504d_base_v078_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 504) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_mclose_504d_base_v079_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 504) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_sclose_504d_base_v080_signal(ebitda, assets, closeadj):
    result = _mean(_f11_ebitda_per_asset(ebitda, assets), 504) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_xclose_5d_base_v081_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_zclose_5d_base_v082_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_mclose_5d_base_v083_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_sclose_5d_base_v084_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_xclose_10d_base_v085_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_zclose_10d_base_v086_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_mclose_10d_base_v087_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_sclose_10d_base_v088_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_xclose_21d_base_v089_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_zclose_21d_base_v090_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_mclose_21d_base_v091_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_sclose_21d_base_v092_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_xclose_42d_base_v093_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_zclose_42d_base_v094_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_mclose_42d_base_v095_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_sclose_42d_base_v096_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_xclose_63d_base_v097_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_zclose_63d_base_v098_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_mclose_63d_base_v099_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_sclose_63d_base_v100_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_xclose_126d_base_v101_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_zclose_126d_base_v102_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 126) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_mclose_126d_base_v103_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 126) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_sclose_126d_base_v104_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_xclose_189d_base_v105_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_zclose_189d_base_v106_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 189) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_mclose_189d_base_v107_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 189) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_sclose_189d_base_v108_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 189) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_xclose_252d_base_v109_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_zclose_252d_base_v110_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 252) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_mclose_252d_base_v111_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 252) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_sclose_252d_base_v112_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 252) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_xclose_378d_base_v113_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_zclose_378d_base_v114_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 378) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_mclose_378d_base_v115_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 378) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_sclose_378d_base_v116_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 378) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_xclose_504d_base_v117_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_zclose_504d_base_v118_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 504) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_mclose_504d_base_v119_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 504) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_sclose_504d_base_v120_signal(revenue, ebitda, assets, closeadj):
    result = _f11_unit_econ_score(revenue, ebitda, assets, 504) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpaz0_21d_base_v121_signal(revenue, assets, closeadj):
    result = _z(_f11_revenue_per_asset(revenue, assets), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpaz1_42d_base_v122_signal(revenue, assets, closeadj):
    result = _z(_f11_revenue_per_asset(revenue, assets), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpaz2_63d_base_v123_signal(revenue, assets, closeadj):
    result = _z(_f11_revenue_per_asset(revenue, assets), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpaz3_126d_base_v124_signal(revenue, assets, closeadj):
    result = _z(_f11_revenue_per_asset(revenue, assets), 126) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpaz4_189d_base_v125_signal(revenue, assets, closeadj):
    result = _z(_f11_revenue_per_asset(revenue, assets), 189) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpaz5_252d_base_v126_signal(revenue, assets, closeadj):
    result = _z(_f11_revenue_per_asset(revenue, assets), 252) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpaz6_378d_base_v127_signal(revenue, assets, closeadj):
    result = _z(_f11_revenue_per_asset(revenue, assets), 378) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpaz7_504d_base_v128_signal(revenue, assets, closeadj):
    result = _z(_f11_revenue_per_asset(revenue, assets), 504) * (closeadj - _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpaz8_10d_base_v129_signal(revenue, assets, closeadj):
    result = _z(_f11_revenue_per_asset(revenue, assets), 10) * (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpaz9_5d_base_v130_signal(revenue, assets, closeadj):
    result = _z(_f11_revenue_per_asset(revenue, assets), 5) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpasd0_21d_base_v131_signal(revenue, assets, closeadj):
    result = _std(_f11_revenue_per_asset(revenue, assets), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpasd1_42d_base_v132_signal(revenue, assets, closeadj):
    result = _std(_f11_revenue_per_asset(revenue, assets), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpasd2_63d_base_v133_signal(revenue, assets, closeadj):
    result = _std(_f11_revenue_per_asset(revenue, assets), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpasd3_126d_base_v134_signal(revenue, assets, closeadj):
    result = _std(_f11_revenue_per_asset(revenue, assets), 126) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpasd4_189d_base_v135_signal(revenue, assets, closeadj):
    result = _std(_f11_revenue_per_asset(revenue, assets), 189) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpasd5_252d_base_v136_signal(revenue, assets, closeadj):
    result = _std(_f11_revenue_per_asset(revenue, assets), 252) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpasd6_378d_base_v137_signal(revenue, assets, closeadj):
    result = _std(_f11_revenue_per_asset(revenue, assets), 378) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpasd7_504d_base_v138_signal(revenue, assets, closeadj):
    result = _std(_f11_revenue_per_asset(revenue, assets), 504) * (closeadj - _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpasd8_10d_base_v139_signal(revenue, assets, closeadj):
    result = _std(_f11_revenue_per_asset(revenue, assets), 10) * (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpasd9_5d_base_v140_signal(revenue, assets, closeadj):
    result = _std(_f11_revenue_per_asset(revenue, assets), 5) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epaz0_21d_base_v141_signal(ebitda, assets, closeadj):
    result = _z(_f11_ebitda_per_asset(ebitda, assets), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epaz1_42d_base_v142_signal(ebitda, assets, closeadj):
    result = _z(_f11_ebitda_per_asset(ebitda, assets), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epaz2_63d_base_v143_signal(ebitda, assets, closeadj):
    result = _z(_f11_ebitda_per_asset(ebitda, assets), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epaz3_126d_base_v144_signal(ebitda, assets, closeadj):
    result = _z(_f11_ebitda_per_asset(ebitda, assets), 126) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epaz4_189d_base_v145_signal(ebitda, assets, closeadj):
    result = _z(_f11_ebitda_per_asset(ebitda, assets), 189) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epaz5_252d_base_v146_signal(ebitda, assets, closeadj):
    result = _z(_f11_ebitda_per_asset(ebitda, assets), 252) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epaz6_378d_base_v147_signal(ebitda, assets, closeadj):
    result = _z(_f11_ebitda_per_asset(ebitda, assets), 378) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epaz7_504d_base_v148_signal(ebitda, assets, closeadj):
    result = _z(_f11_ebitda_per_asset(ebitda, assets), 504) * (closeadj - _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epaz8_10d_base_v149_signal(ebitda, assets, closeadj):
    result = _z(_f11_ebitda_per_asset(ebitda, assets), 10) * (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epaz9_5d_base_v150_signal(ebitda, assets, closeadj):
    result = _z(_f11_ebitda_per_asset(ebitda, assets), 5) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f11rue_f11_restaurant_unit_economics_epa_sclose_378d_base_v076_signal,
    f11rue_f11_restaurant_unit_economics_epa_xclose_504d_base_v077_signal,
    f11rue_f11_restaurant_unit_economics_epa_zclose_504d_base_v078_signal,
    f11rue_f11_restaurant_unit_economics_epa_mclose_504d_base_v079_signal,
    f11rue_f11_restaurant_unit_economics_epa_sclose_504d_base_v080_signal,
    f11rue_f11_restaurant_unit_economics_ues_xclose_5d_base_v081_signal,
    f11rue_f11_restaurant_unit_economics_ues_zclose_5d_base_v082_signal,
    f11rue_f11_restaurant_unit_economics_ues_mclose_5d_base_v083_signal,
    f11rue_f11_restaurant_unit_economics_ues_sclose_5d_base_v084_signal,
    f11rue_f11_restaurant_unit_economics_ues_xclose_10d_base_v085_signal,
    f11rue_f11_restaurant_unit_economics_ues_zclose_10d_base_v086_signal,
    f11rue_f11_restaurant_unit_economics_ues_mclose_10d_base_v087_signal,
    f11rue_f11_restaurant_unit_economics_ues_sclose_10d_base_v088_signal,
    f11rue_f11_restaurant_unit_economics_ues_xclose_21d_base_v089_signal,
    f11rue_f11_restaurant_unit_economics_ues_zclose_21d_base_v090_signal,
    f11rue_f11_restaurant_unit_economics_ues_mclose_21d_base_v091_signal,
    f11rue_f11_restaurant_unit_economics_ues_sclose_21d_base_v092_signal,
    f11rue_f11_restaurant_unit_economics_ues_xclose_42d_base_v093_signal,
    f11rue_f11_restaurant_unit_economics_ues_zclose_42d_base_v094_signal,
    f11rue_f11_restaurant_unit_economics_ues_mclose_42d_base_v095_signal,
    f11rue_f11_restaurant_unit_economics_ues_sclose_42d_base_v096_signal,
    f11rue_f11_restaurant_unit_economics_ues_xclose_63d_base_v097_signal,
    f11rue_f11_restaurant_unit_economics_ues_zclose_63d_base_v098_signal,
    f11rue_f11_restaurant_unit_economics_ues_mclose_63d_base_v099_signal,
    f11rue_f11_restaurant_unit_economics_ues_sclose_63d_base_v100_signal,
    f11rue_f11_restaurant_unit_economics_ues_xclose_126d_base_v101_signal,
    f11rue_f11_restaurant_unit_economics_ues_zclose_126d_base_v102_signal,
    f11rue_f11_restaurant_unit_economics_ues_mclose_126d_base_v103_signal,
    f11rue_f11_restaurant_unit_economics_ues_sclose_126d_base_v104_signal,
    f11rue_f11_restaurant_unit_economics_ues_xclose_189d_base_v105_signal,
    f11rue_f11_restaurant_unit_economics_ues_zclose_189d_base_v106_signal,
    f11rue_f11_restaurant_unit_economics_ues_mclose_189d_base_v107_signal,
    f11rue_f11_restaurant_unit_economics_ues_sclose_189d_base_v108_signal,
    f11rue_f11_restaurant_unit_economics_ues_xclose_252d_base_v109_signal,
    f11rue_f11_restaurant_unit_economics_ues_zclose_252d_base_v110_signal,
    f11rue_f11_restaurant_unit_economics_ues_mclose_252d_base_v111_signal,
    f11rue_f11_restaurant_unit_economics_ues_sclose_252d_base_v112_signal,
    f11rue_f11_restaurant_unit_economics_ues_xclose_378d_base_v113_signal,
    f11rue_f11_restaurant_unit_economics_ues_zclose_378d_base_v114_signal,
    f11rue_f11_restaurant_unit_economics_ues_mclose_378d_base_v115_signal,
    f11rue_f11_restaurant_unit_economics_ues_sclose_378d_base_v116_signal,
    f11rue_f11_restaurant_unit_economics_ues_xclose_504d_base_v117_signal,
    f11rue_f11_restaurant_unit_economics_ues_zclose_504d_base_v118_signal,
    f11rue_f11_restaurant_unit_economics_ues_mclose_504d_base_v119_signal,
    f11rue_f11_restaurant_unit_economics_ues_sclose_504d_base_v120_signal,
    f11rue_f11_restaurant_unit_economics_rpaz0_21d_base_v121_signal,
    f11rue_f11_restaurant_unit_economics_rpaz1_42d_base_v122_signal,
    f11rue_f11_restaurant_unit_economics_rpaz2_63d_base_v123_signal,
    f11rue_f11_restaurant_unit_economics_rpaz3_126d_base_v124_signal,
    f11rue_f11_restaurant_unit_economics_rpaz4_189d_base_v125_signal,
    f11rue_f11_restaurant_unit_economics_rpaz5_252d_base_v126_signal,
    f11rue_f11_restaurant_unit_economics_rpaz6_378d_base_v127_signal,
    f11rue_f11_restaurant_unit_economics_rpaz7_504d_base_v128_signal,
    f11rue_f11_restaurant_unit_economics_rpaz8_10d_base_v129_signal,
    f11rue_f11_restaurant_unit_economics_rpaz9_5d_base_v130_signal,
    f11rue_f11_restaurant_unit_economics_rpasd0_21d_base_v131_signal,
    f11rue_f11_restaurant_unit_economics_rpasd1_42d_base_v132_signal,
    f11rue_f11_restaurant_unit_economics_rpasd2_63d_base_v133_signal,
    f11rue_f11_restaurant_unit_economics_rpasd3_126d_base_v134_signal,
    f11rue_f11_restaurant_unit_economics_rpasd4_189d_base_v135_signal,
    f11rue_f11_restaurant_unit_economics_rpasd5_252d_base_v136_signal,
    f11rue_f11_restaurant_unit_economics_rpasd6_378d_base_v137_signal,
    f11rue_f11_restaurant_unit_economics_rpasd7_504d_base_v138_signal,
    f11rue_f11_restaurant_unit_economics_rpasd8_10d_base_v139_signal,
    f11rue_f11_restaurant_unit_economics_rpasd9_5d_base_v140_signal,
    f11rue_f11_restaurant_unit_economics_epaz0_21d_base_v141_signal,
    f11rue_f11_restaurant_unit_economics_epaz1_42d_base_v142_signal,
    f11rue_f11_restaurant_unit_economics_epaz2_63d_base_v143_signal,
    f11rue_f11_restaurant_unit_economics_epaz3_126d_base_v144_signal,
    f11rue_f11_restaurant_unit_economics_epaz4_189d_base_v145_signal,
    f11rue_f11_restaurant_unit_economics_epaz5_252d_base_v146_signal,
    f11rue_f11_restaurant_unit_economics_epaz6_378d_base_v147_signal,
    f11rue_f11_restaurant_unit_economics_epaz7_504d_base_v148_signal,
    f11rue_f11_restaurant_unit_economics_epaz8_10d_base_v149_signal,
    f11rue_f11_restaurant_unit_economics_epaz9_5d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F11_RESTAURANT_UNIT_ECONOMICS_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f11_revenue_per_asset", "_f11_ebitda_per_asset", "_f11_unit_econ_score")
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
    print(f"OK f11_restaurant_unit_economics_base_076_150_claude: {n_features} features pass")
