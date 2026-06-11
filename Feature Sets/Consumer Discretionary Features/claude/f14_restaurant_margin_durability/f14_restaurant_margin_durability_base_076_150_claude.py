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

def _f14_margin_durability(ebitdamargin, w):
    m = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f14_margin_growth_stability(ebitdamargin, revenue, w):
    rg = revenue.pct_change(periods=w)
    msd = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return rg / msd.replace(0, np.nan)


def _f14_durability_score(ebitdamargin, grossmargin, w):
    em = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    gm = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    esd = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    gsd = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    return (em + gm) / (esd + gsd).replace(0, np.nan)


# ===== features =====

def f14rmd_f14_restaurant_margin_durability_mgs_sclose_378d_base_v076_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 378) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_xclose_504d_base_v077_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_zclose_504d_base_v078_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 504) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_mclose_504d_base_v079_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 504) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mgs_sclose_504d_base_v080_signal(ebitdamargin, revenue, closeadj):
    result = _f14_margin_growth_stability(ebitdamargin, revenue, 504) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_xclose_5d_base_v081_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_zclose_5d_base_v082_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_mclose_5d_base_v083_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_sclose_5d_base_v084_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_xclose_10d_base_v085_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_zclose_10d_base_v086_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_mclose_10d_base_v087_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_sclose_10d_base_v088_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_xclose_21d_base_v089_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_zclose_21d_base_v090_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_mclose_21d_base_v091_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_sclose_21d_base_v092_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_xclose_42d_base_v093_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_zclose_42d_base_v094_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_mclose_42d_base_v095_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_sclose_42d_base_v096_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_xclose_63d_base_v097_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_zclose_63d_base_v098_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_mclose_63d_base_v099_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_sclose_63d_base_v100_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_xclose_126d_base_v101_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_zclose_126d_base_v102_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 126) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_mclose_126d_base_v103_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 126) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_sclose_126d_base_v104_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_xclose_189d_base_v105_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_zclose_189d_base_v106_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 189) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_mclose_189d_base_v107_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 189) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_sclose_189d_base_v108_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 189) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_xclose_252d_base_v109_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_zclose_252d_base_v110_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 252) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_mclose_252d_base_v111_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 252) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_sclose_252d_base_v112_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 252) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_xclose_378d_base_v113_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_zclose_378d_base_v114_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 378) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_mclose_378d_base_v115_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 378) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_sclose_378d_base_v116_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 378) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_xclose_504d_base_v117_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_zclose_504d_base_v118_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 504) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_mclose_504d_base_v119_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 504) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_ds_sclose_504d_base_v120_signal(ebitdamargin, grossmargin, closeadj):
    result = _f14_durability_score(ebitdamargin, grossmargin, 504) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mdm0_21d_base_v121_signal(ebitdamargin, closeadj):
    result = _mean(_f14_margin_durability(ebitdamargin, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mdm1_42d_base_v122_signal(ebitdamargin, closeadj):
    result = _mean(_f14_margin_durability(ebitdamargin, 42), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mdm2_63d_base_v123_signal(ebitdamargin, closeadj):
    result = _mean(_f14_margin_durability(ebitdamargin, 63), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mdm3_126d_base_v124_signal(ebitdamargin, closeadj):
    result = _mean(_f14_margin_durability(ebitdamargin, 126), 21) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mdm4_189d_base_v125_signal(ebitdamargin, closeadj):
    result = _mean(_f14_margin_durability(ebitdamargin, 189), 21) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mdm5_252d_base_v126_signal(ebitdamargin, closeadj):
    result = _mean(_f14_margin_durability(ebitdamargin, 252), 21) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mdm6_378d_base_v127_signal(ebitdamargin, closeadj):
    result = _mean(_f14_margin_durability(ebitdamargin, 378), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mdm7_504d_base_v128_signal(ebitdamargin, closeadj):
    result = _mean(_f14_margin_durability(ebitdamargin, 504), 21) * (closeadj - _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mdm8_10d_base_v129_signal(ebitdamargin, closeadj):
    result = _mean(_f14_margin_durability(ebitdamargin, 10), 21) * (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mdm9_5d_base_v130_signal(ebitdamargin, closeadj):
    result = _mean(_f14_margin_durability(ebitdamargin, 5), 21) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mdz0_21d_base_v131_signal(ebitdamargin, closeadj):
    result = _z(_f14_margin_durability(ebitdamargin, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mdz1_42d_base_v132_signal(ebitdamargin, closeadj):
    result = _z(_f14_margin_durability(ebitdamargin, 42), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mdz2_63d_base_v133_signal(ebitdamargin, closeadj):
    result = _z(_f14_margin_durability(ebitdamargin, 63), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mdz3_126d_base_v134_signal(ebitdamargin, closeadj):
    result = _z(_f14_margin_durability(ebitdamargin, 126), 63) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mdz4_189d_base_v135_signal(ebitdamargin, closeadj):
    result = _z(_f14_margin_durability(ebitdamargin, 189), 63) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mdz5_252d_base_v136_signal(ebitdamargin, closeadj):
    result = _z(_f14_margin_durability(ebitdamargin, 252), 63) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mdz6_378d_base_v137_signal(ebitdamargin, closeadj):
    result = _z(_f14_margin_durability(ebitdamargin, 378), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mdz7_504d_base_v138_signal(ebitdamargin, closeadj):
    result = _z(_f14_margin_durability(ebitdamargin, 504), 63) * (closeadj - _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mdz8_10d_base_v139_signal(ebitdamargin, closeadj):
    result = _z(_f14_margin_durability(ebitdamargin, 10), 63) * (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_mdz9_5d_base_v140_signal(ebitdamargin, closeadj):
    result = _z(_f14_margin_durability(ebitdamargin, 5), 63) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_dsm0_21d_base_v141_signal(ebitdamargin, grossmargin, closeadj):
    result = _mean(_f14_durability_score(ebitdamargin, grossmargin, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_dsm1_42d_base_v142_signal(ebitdamargin, grossmargin, closeadj):
    result = _mean(_f14_durability_score(ebitdamargin, grossmargin, 42), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_dsm2_63d_base_v143_signal(ebitdamargin, grossmargin, closeadj):
    result = _mean(_f14_durability_score(ebitdamargin, grossmargin, 63), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_dsm3_126d_base_v144_signal(ebitdamargin, grossmargin, closeadj):
    result = _mean(_f14_durability_score(ebitdamargin, grossmargin, 126), 21) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_dsm4_189d_base_v145_signal(ebitdamargin, grossmargin, closeadj):
    result = _mean(_f14_durability_score(ebitdamargin, grossmargin, 189), 21) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_dsm5_252d_base_v146_signal(ebitdamargin, grossmargin, closeadj):
    result = _mean(_f14_durability_score(ebitdamargin, grossmargin, 252), 21) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_dsm6_378d_base_v147_signal(ebitdamargin, grossmargin, closeadj):
    result = _mean(_f14_durability_score(ebitdamargin, grossmargin, 378), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_dsm7_504d_base_v148_signal(ebitdamargin, grossmargin, closeadj):
    result = _mean(_f14_durability_score(ebitdamargin, grossmargin, 504), 21) * (closeadj - _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_dsm8_10d_base_v149_signal(ebitdamargin, grossmargin, closeadj):
    result = _mean(_f14_durability_score(ebitdamargin, grossmargin, 10), 21) * (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


def f14rmd_f14_restaurant_margin_durability_dsm9_5d_base_v150_signal(ebitdamargin, grossmargin, closeadj):
    result = _mean(_f14_durability_score(ebitdamargin, grossmargin, 5), 21) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f14rmd_f14_restaurant_margin_durability_mgs_sclose_378d_base_v076_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_xclose_504d_base_v077_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_zclose_504d_base_v078_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_mclose_504d_base_v079_signal,
    f14rmd_f14_restaurant_margin_durability_mgs_sclose_504d_base_v080_signal,
    f14rmd_f14_restaurant_margin_durability_ds_xclose_5d_base_v081_signal,
    f14rmd_f14_restaurant_margin_durability_ds_zclose_5d_base_v082_signal,
    f14rmd_f14_restaurant_margin_durability_ds_mclose_5d_base_v083_signal,
    f14rmd_f14_restaurant_margin_durability_ds_sclose_5d_base_v084_signal,
    f14rmd_f14_restaurant_margin_durability_ds_xclose_10d_base_v085_signal,
    f14rmd_f14_restaurant_margin_durability_ds_zclose_10d_base_v086_signal,
    f14rmd_f14_restaurant_margin_durability_ds_mclose_10d_base_v087_signal,
    f14rmd_f14_restaurant_margin_durability_ds_sclose_10d_base_v088_signal,
    f14rmd_f14_restaurant_margin_durability_ds_xclose_21d_base_v089_signal,
    f14rmd_f14_restaurant_margin_durability_ds_zclose_21d_base_v090_signal,
    f14rmd_f14_restaurant_margin_durability_ds_mclose_21d_base_v091_signal,
    f14rmd_f14_restaurant_margin_durability_ds_sclose_21d_base_v092_signal,
    f14rmd_f14_restaurant_margin_durability_ds_xclose_42d_base_v093_signal,
    f14rmd_f14_restaurant_margin_durability_ds_zclose_42d_base_v094_signal,
    f14rmd_f14_restaurant_margin_durability_ds_mclose_42d_base_v095_signal,
    f14rmd_f14_restaurant_margin_durability_ds_sclose_42d_base_v096_signal,
    f14rmd_f14_restaurant_margin_durability_ds_xclose_63d_base_v097_signal,
    f14rmd_f14_restaurant_margin_durability_ds_zclose_63d_base_v098_signal,
    f14rmd_f14_restaurant_margin_durability_ds_mclose_63d_base_v099_signal,
    f14rmd_f14_restaurant_margin_durability_ds_sclose_63d_base_v100_signal,
    f14rmd_f14_restaurant_margin_durability_ds_xclose_126d_base_v101_signal,
    f14rmd_f14_restaurant_margin_durability_ds_zclose_126d_base_v102_signal,
    f14rmd_f14_restaurant_margin_durability_ds_mclose_126d_base_v103_signal,
    f14rmd_f14_restaurant_margin_durability_ds_sclose_126d_base_v104_signal,
    f14rmd_f14_restaurant_margin_durability_ds_xclose_189d_base_v105_signal,
    f14rmd_f14_restaurant_margin_durability_ds_zclose_189d_base_v106_signal,
    f14rmd_f14_restaurant_margin_durability_ds_mclose_189d_base_v107_signal,
    f14rmd_f14_restaurant_margin_durability_ds_sclose_189d_base_v108_signal,
    f14rmd_f14_restaurant_margin_durability_ds_xclose_252d_base_v109_signal,
    f14rmd_f14_restaurant_margin_durability_ds_zclose_252d_base_v110_signal,
    f14rmd_f14_restaurant_margin_durability_ds_mclose_252d_base_v111_signal,
    f14rmd_f14_restaurant_margin_durability_ds_sclose_252d_base_v112_signal,
    f14rmd_f14_restaurant_margin_durability_ds_xclose_378d_base_v113_signal,
    f14rmd_f14_restaurant_margin_durability_ds_zclose_378d_base_v114_signal,
    f14rmd_f14_restaurant_margin_durability_ds_mclose_378d_base_v115_signal,
    f14rmd_f14_restaurant_margin_durability_ds_sclose_378d_base_v116_signal,
    f14rmd_f14_restaurant_margin_durability_ds_xclose_504d_base_v117_signal,
    f14rmd_f14_restaurant_margin_durability_ds_zclose_504d_base_v118_signal,
    f14rmd_f14_restaurant_margin_durability_ds_mclose_504d_base_v119_signal,
    f14rmd_f14_restaurant_margin_durability_ds_sclose_504d_base_v120_signal,
    f14rmd_f14_restaurant_margin_durability_mdm0_21d_base_v121_signal,
    f14rmd_f14_restaurant_margin_durability_mdm1_42d_base_v122_signal,
    f14rmd_f14_restaurant_margin_durability_mdm2_63d_base_v123_signal,
    f14rmd_f14_restaurant_margin_durability_mdm3_126d_base_v124_signal,
    f14rmd_f14_restaurant_margin_durability_mdm4_189d_base_v125_signal,
    f14rmd_f14_restaurant_margin_durability_mdm5_252d_base_v126_signal,
    f14rmd_f14_restaurant_margin_durability_mdm6_378d_base_v127_signal,
    f14rmd_f14_restaurant_margin_durability_mdm7_504d_base_v128_signal,
    f14rmd_f14_restaurant_margin_durability_mdm8_10d_base_v129_signal,
    f14rmd_f14_restaurant_margin_durability_mdm9_5d_base_v130_signal,
    f14rmd_f14_restaurant_margin_durability_mdz0_21d_base_v131_signal,
    f14rmd_f14_restaurant_margin_durability_mdz1_42d_base_v132_signal,
    f14rmd_f14_restaurant_margin_durability_mdz2_63d_base_v133_signal,
    f14rmd_f14_restaurant_margin_durability_mdz3_126d_base_v134_signal,
    f14rmd_f14_restaurant_margin_durability_mdz4_189d_base_v135_signal,
    f14rmd_f14_restaurant_margin_durability_mdz5_252d_base_v136_signal,
    f14rmd_f14_restaurant_margin_durability_mdz6_378d_base_v137_signal,
    f14rmd_f14_restaurant_margin_durability_mdz7_504d_base_v138_signal,
    f14rmd_f14_restaurant_margin_durability_mdz8_10d_base_v139_signal,
    f14rmd_f14_restaurant_margin_durability_mdz9_5d_base_v140_signal,
    f14rmd_f14_restaurant_margin_durability_dsm0_21d_base_v141_signal,
    f14rmd_f14_restaurant_margin_durability_dsm1_42d_base_v142_signal,
    f14rmd_f14_restaurant_margin_durability_dsm2_63d_base_v143_signal,
    f14rmd_f14_restaurant_margin_durability_dsm3_126d_base_v144_signal,
    f14rmd_f14_restaurant_margin_durability_dsm4_189d_base_v145_signal,
    f14rmd_f14_restaurant_margin_durability_dsm5_252d_base_v146_signal,
    f14rmd_f14_restaurant_margin_durability_dsm6_378d_base_v147_signal,
    f14rmd_f14_restaurant_margin_durability_dsm7_504d_base_v148_signal,
    f14rmd_f14_restaurant_margin_durability_dsm8_10d_base_v149_signal,
    f14rmd_f14_restaurant_margin_durability_dsm9_5d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F14_RESTAURANT_MARGIN_DURABILITY_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f14_margin_durability", "_f14_margin_growth_stability", "_f14_durability_score")
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
    print(f"OK f14_restaurant_margin_durability_base_076_150_claude: {n_features} features pass")
