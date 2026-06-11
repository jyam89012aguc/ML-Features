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
    return s.ewm(span=w, adjust=False, min_periods=max(1, w // 2)).mean()


# ===== folder domain primitives =====
def _f38_margin_floor(grossmargin, w):
    # Rolling minimum of grossmargin -- the "floor"
    return grossmargin.rolling(w, min_periods=max(1, w // 2)).min()


def _f38_premium_persistence(ebitdamargin, w):
    # Mean margin / std margin (signal-to-noise of margin)
    m = _mean(ebitdamargin, w)
    s = _std(ebitdamargin, w)
    return m / s.replace(0, np.nan)


def _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, w):
    # Margin level x (1 / revenue volatility)
    mean_gm = _mean(grossmargin, w)
    mean_em = _mean(ebitdamargin, w)
    rev_vol = _std(revenue.pct_change(), w)
    return (mean_gm + mean_em) / rev_vol.replace(0, np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxem_5d_base_v076_signal(grossmargin, ebitdamargin, closeadj):
    d = _f38_margin_floor(grossmargin, 5)
    result = d * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxem_10d_base_v077_signal(grossmargin, ebitdamargin, closeadj):
    d = _f38_margin_floor(grossmargin, 10)
    result = d * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxem_21d_base_v078_signal(grossmargin, ebitdamargin, closeadj):
    d = _f38_margin_floor(grossmargin, 21)
    result = d * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxem_42d_base_v079_signal(grossmargin, ebitdamargin, closeadj):
    d = _f38_margin_floor(grossmargin, 42)
    result = d * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxem_63d_base_v080_signal(grossmargin, ebitdamargin, closeadj):
    d = _f38_margin_floor(grossmargin, 63)
    result = d * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxem_126d_base_v081_signal(grossmargin, ebitdamargin, closeadj):
    d = _f38_margin_floor(grossmargin, 126)
    result = d * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxem_189d_base_v082_signal(grossmargin, ebitdamargin, closeadj):
    d = _f38_margin_floor(grossmargin, 189)
    result = d * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxem_252d_base_v083_signal(grossmargin, ebitdamargin, closeadj):
    d = _f38_margin_floor(grossmargin, 252)
    result = d * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxem_378d_base_v084_signal(grossmargin, ebitdamargin, closeadj):
    d = _f38_margin_floor(grossmargin, 378)
    result = d * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxem_504d_base_v085_signal(grossmargin, ebitdamargin, closeadj):
    d = _f38_margin_floor(grossmargin, 504)
    result = d * ebitdamargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperema_5d_base_v086_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 63)
    result = _ema(d, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperema_10d_base_v087_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 63)
    result = _ema(d, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperema_21d_base_v088_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 63)
    result = _ema(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperema_42d_base_v089_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 63)
    result = _ema(d, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperema_63d_base_v090_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 63)
    result = _ema(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperema_126d_base_v091_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 63)
    result = _ema(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperema_189d_base_v092_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 63)
    result = _ema(d, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperema_252d_base_v093_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 63)
    result = _ema(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperema_378d_base_v094_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 63)
    result = _ema(d, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperema_504d_base_v095_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 63)
    result = _ema(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurxgm_5d_base_v096_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 5)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurxgm_10d_base_v097_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 10)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurxgm_21d_base_v098_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 21)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurxgm_42d_base_v099_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 42)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurxgm_63d_base_v100_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurxgm_126d_base_v101_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 126)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurxgm_189d_base_v102_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 189)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurxgm_252d_base_v103_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 252)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurxgm_378d_base_v104_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 378)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurxgm_504d_base_v105_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 504)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxrevg_21d_base_v106_signal(grossmargin, revenue, closeadj):
    d = _f38_margin_floor(grossmargin, 21)
    result = d * revenue.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxrevg_63d_base_v107_signal(grossmargin, revenue, closeadj):
    d = _f38_margin_floor(grossmargin, 63)
    result = d * revenue.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxrevg_126d_base_v108_signal(grossmargin, revenue, closeadj):
    d = _f38_margin_floor(grossmargin, 126)
    result = d * revenue.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxrevg_189d_base_v109_signal(grossmargin, revenue, closeadj):
    d = _f38_margin_floor(grossmargin, 189)
    result = d * revenue.pct_change(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxrevg_252d_base_v110_signal(grossmargin, revenue, closeadj):
    d = _f38_margin_floor(grossmargin, 252)
    result = d * revenue.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxrevg_378d_base_v111_signal(grossmargin, revenue, closeadj):
    d = _f38_margin_floor(grossmargin, 378)
    result = d * revenue.pct_change(378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxrevg_504d_base_v112_signal(grossmargin, revenue, closeadj):
    d = _f38_margin_floor(grossmargin, 504)
    result = d * revenue.pct_change(504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperxgm_21d_base_v113_signal(ebitdamargin, grossmargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 21)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperxgm_63d_base_v114_signal(ebitdamargin, grossmargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 63)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperxgm_126d_base_v115_signal(ebitdamargin, grossmargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 126)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperxgm_189d_base_v116_signal(ebitdamargin, grossmargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 189)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperxgm_252d_base_v117_signal(ebitdamargin, grossmargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 252)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperxgm_378d_base_v118_signal(ebitdamargin, grossmargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 378)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperxgm_504d_base_v119_signal(ebitdamargin, grossmargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 504)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurchg_21d_base_v120_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = d.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurchg_63d_base_v121_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = d.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurchg_126d_base_v122_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = d.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurchg_189d_base_v123_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = d.diff(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurchg_252d_base_v124_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = d.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurchg_378d_base_v125_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = d.diff(378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurchg_504d_base_v126_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = d.diff(504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnmd_21d_base_v127_signal(grossmargin, netmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 21)
    result = d * netmargin.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnmd_63d_base_v128_signal(grossmargin, netmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 63)
    result = d * netmargin.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnmd_126d_base_v129_signal(grossmargin, netmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 126)
    result = d * netmargin.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnmd_189d_base_v130_signal(grossmargin, netmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 189)
    result = d * netmargin.diff(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnmd_252d_base_v131_signal(grossmargin, netmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 252)
    result = d * netmargin.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnmd_378d_base_v132_signal(grossmargin, netmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 378)
    result = d * netmargin.diff(378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnmd_504d_base_v133_signal(grossmargin, netmargin, closeadj):
    d = _f38_margin_floor(grossmargin, 504)
    result = d * netmargin.diff(504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperstd_42d_base_v134_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 63)
    result = _std(d, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperstd_63d_base_v135_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 63)
    result = _std(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperstd_126d_base_v136_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 63)
    result = _std(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperstd_189d_base_v137_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 63)
    result = _std(d, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperstd_252d_base_v138_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 63)
    result = _std(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperstd_378d_base_v139_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 63)
    result = _std(d, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperstd_504d_base_v140_signal(ebitdamargin, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 63)
    result = _std(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurxemd_21d_base_v141_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = d * ebitdamargin.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurxemd_63d_base_v142_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = d * ebitdamargin.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurxemd_126d_base_v143_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = d * ebitdamargin.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurxemd_189d_base_v144_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = d * ebitdamargin.diff(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurxemd_252d_base_v145_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = d * ebitdamargin.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurxemd_378d_base_v146_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = d * ebitdamargin.diff(378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurxemd_504d_base_v147_signal(grossmargin, ebitdamargin, revenue, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = d * ebitdamargin.diff(504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_mgnfloorxrev_252d_base_v148_signal(grossmargin, revenue, closeadj):
    d = _f38_margin_floor(grossmargin, 252)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_preperxrevg_252d_base_v149_signal(ebitdamargin, revenue, closeadj):
    d = _f38_premium_persistence(ebitdamargin, 252)
    result = d * revenue.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38lbp_f38_luxury_brand_premium_durability_luxdurxnmd_252d_base_v150_signal(grossmargin, ebitdamargin, revenue, netmargin, closeadj):
    d = _f38_luxury_durability_score(grossmargin, ebitdamargin, revenue, 63)
    result = d * netmargin.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxem_5d_base_v076_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxem_10d_base_v077_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxem_21d_base_v078_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxem_42d_base_v079_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxem_63d_base_v080_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxem_126d_base_v081_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxem_189d_base_v082_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxem_252d_base_v083_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxem_378d_base_v084_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxem_504d_base_v085_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperema_5d_base_v086_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperema_10d_base_v087_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperema_21d_base_v088_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperema_42d_base_v089_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperema_63d_base_v090_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperema_126d_base_v091_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperema_189d_base_v092_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperema_252d_base_v093_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperema_378d_base_v094_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperema_504d_base_v095_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurxgm_5d_base_v096_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurxgm_10d_base_v097_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurxgm_21d_base_v098_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurxgm_42d_base_v099_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurxgm_63d_base_v100_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurxgm_126d_base_v101_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurxgm_189d_base_v102_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurxgm_252d_base_v103_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurxgm_378d_base_v104_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurxgm_504d_base_v105_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxrevg_21d_base_v106_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxrevg_63d_base_v107_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxrevg_126d_base_v108_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxrevg_189d_base_v109_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxrevg_252d_base_v110_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxrevg_378d_base_v111_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxrevg_504d_base_v112_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperxgm_21d_base_v113_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperxgm_63d_base_v114_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperxgm_126d_base_v115_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperxgm_189d_base_v116_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperxgm_252d_base_v117_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperxgm_378d_base_v118_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperxgm_504d_base_v119_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurchg_21d_base_v120_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurchg_63d_base_v121_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurchg_126d_base_v122_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurchg_189d_base_v123_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurchg_252d_base_v124_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurchg_378d_base_v125_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurchg_504d_base_v126_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnmd_21d_base_v127_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnmd_63d_base_v128_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnmd_126d_base_v129_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnmd_189d_base_v130_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnmd_252d_base_v131_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnmd_378d_base_v132_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxnmd_504d_base_v133_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperstd_42d_base_v134_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperstd_63d_base_v135_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperstd_126d_base_v136_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperstd_189d_base_v137_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperstd_252d_base_v138_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperstd_378d_base_v139_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperstd_504d_base_v140_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurxemd_21d_base_v141_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurxemd_63d_base_v142_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurxemd_126d_base_v143_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurxemd_189d_base_v144_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurxemd_252d_base_v145_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurxemd_378d_base_v146_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurxemd_504d_base_v147_signal,
    f38lbp_f38_luxury_brand_premium_durability_mgnfloorxrev_252d_base_v148_signal,
    f38lbp_f38_luxury_brand_premium_durability_preperxrevg_252d_base_v149_signal,
    f38lbp_f38_luxury_brand_premium_durability_luxdurxnmd_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F38_LUXURY_BRAND_PREMIUM_DURABILITY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {
        "closeadj": closeadj, "volume": volume,
        "revenue": revenue, "cor": cor, "inventory": inventory,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
    }


    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f38_margin_floor", "_f38_premium_persistence", "_f38_luxury_durability_score",)
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
    print(f"OK f38_luxury_brand_premium_durability_076_150_claude: {n_features} features pass")
