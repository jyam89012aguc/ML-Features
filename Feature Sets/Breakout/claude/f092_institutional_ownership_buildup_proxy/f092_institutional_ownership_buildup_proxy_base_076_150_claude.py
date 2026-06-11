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
def _f092_marketcap_trend(marketcap, w):
    return _mean(marketcap, w) / _mean(marketcap, w * 2).replace(0, np.nan) - 1.0


def _f092_mc_per_share(marketcap, sharesbas):
    return marketcap / sharesbas.replace(0, np.nan)


def _f092_inst_buildup_proxy(marketcap, sharesbas, w):
    mps = marketcap / sharesbas.replace(0, np.nan)
    return mps.pct_change(w)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_tanhw_5d_base_v076_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 5)
    result = np.tanh(_z(base, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_tanhw_5d_base_v077_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 5)
    result = np.tanh(_z(base, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_tanhw_5d_base_v078_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = np.tanh(_z(base, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_tanhw_10d_base_v079_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 10)
    result = np.tanh(_z(base, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_tanhw_10d_base_v080_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 10)
    result = np.tanh(_z(base, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_tanhw_10d_base_v081_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = np.tanh(_z(base, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_tanhw_21d_base_v082_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 21)
    result = np.tanh(_z(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_tanhw_21d_base_v083_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 21)
    result = np.tanh(_z(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_tanhw_21d_base_v084_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = np.tanh(_z(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_tanhw_42d_base_v085_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 42)
    result = np.tanh(_z(base, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_tanhw_42d_base_v086_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 42)
    result = np.tanh(_z(base, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_tanhw_42d_base_v087_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = np.tanh(_z(base, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_tanhw_63d_base_v088_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 63)
    result = np.tanh(_z(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_tanhw_63d_base_v089_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 63)
    result = np.tanh(_z(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_tanhw_63d_base_v090_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = np.tanh(_z(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_tanhw_126d_base_v091_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 126)
    result = np.tanh(_z(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_tanhw_126d_base_v092_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 126)
    result = np.tanh(_z(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_tanhw_126d_base_v093_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = np.tanh(_z(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_tanhw_189d_base_v094_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 189)
    result = np.tanh(_z(base, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_tanhw_189d_base_v095_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 189)
    result = np.tanh(_z(base, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_tanhw_189d_base_v096_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = np.tanh(_z(base, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_tanhw_252d_base_v097_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_tanhw_252d_base_v098_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_tanhw_252d_base_v099_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_tanhw_378d_base_v100_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 378)
    result = np.tanh(_z(base, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_tanhw_378d_base_v101_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 378)
    result = np.tanh(_z(base, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_tanhw_378d_base_v102_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = np.tanh(_z(base, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_tanhw_504d_base_v103_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 504)
    result = np.tanh(_z(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_tanhw_504d_base_v104_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 504)
    result = np.tanh(_z(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_tanhw_504d_base_v105_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = np.tanh(_z(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_zclipw_5d_base_v106_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 5)
    result = _z(base, 5).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_zclipw_5d_base_v107_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 5)
    result = _z(base, 5).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_zclipw_5d_base_v108_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 5).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_zclipw_10d_base_v109_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 10)
    result = _z(base, 10).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_zclipw_10d_base_v110_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 10)
    result = _z(base, 10).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_zclipw_10d_base_v111_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 10).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_zclipw_21d_base_v112_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 21)
    result = _z(base, 21).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_zclipw_21d_base_v113_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 21)
    result = _z(base, 21).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_zclipw_21d_base_v114_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 21).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_zclipw_42d_base_v115_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 42)
    result = _z(base, 42).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_zclipw_42d_base_v116_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 42)
    result = _z(base, 42).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_zclipw_42d_base_v117_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 42).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_zclipw_63d_base_v118_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 63)
    result = _z(base, 63).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_zclipw_63d_base_v119_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 63)
    result = _z(base, 63).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_zclipw_63d_base_v120_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 63).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_zclipw_126d_base_v121_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 126)
    result = _z(base, 126).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_zclipw_126d_base_v122_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 126)
    result = _z(base, 126).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_zclipw_126d_base_v123_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 126).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_zclipw_189d_base_v124_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 189)
    result = _z(base, 189).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_zclipw_189d_base_v125_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 189)
    result = _z(base, 189).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_zclipw_189d_base_v126_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 189).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_zclipw_252d_base_v127_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_zclipw_252d_base_v128_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_zclipw_252d_base_v129_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_zclipw_378d_base_v130_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 378)
    result = _z(base, 378).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_zclipw_378d_base_v131_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 378)
    result = _z(base, 378).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_zclipw_378d_base_v132_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 378).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_zclipw_504d_base_v133_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 504)
    result = _z(base, 504).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_zclipw_504d_base_v134_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 504)
    result = _z(base, 504).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_zclipw_504d_base_v135_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 504).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_varw_5d_base_v136_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 5)
    result = base.rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_varw_5d_base_v137_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 5)
    result = base.rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_varw_5d_base_v138_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 5).rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_varw_10d_base_v139_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 10)
    result = base.rolling(10, min_periods=max(2, 10 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_varw_10d_base_v140_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 10)
    result = base.rolling(10, min_periods=max(2, 10 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_varw_10d_base_v141_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 10).rolling(10, min_periods=max(2, 10 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_varw_21d_base_v142_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 21)
    result = base.rolling(21, min_periods=max(2, 21 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_varw_21d_base_v143_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 21)
    result = base.rolling(21, min_periods=max(2, 21 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_varw_21d_base_v144_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 21).rolling(21, min_periods=max(2, 21 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_varw_42d_base_v145_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 42)
    result = base.rolling(42, min_periods=max(2, 42 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_varw_42d_base_v146_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 42)
    result = base.rolling(42, min_periods=max(2, 42 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_varw_42d_base_v147_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 42).rolling(42, min_periods=max(2, 42 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_varw_63d_base_v148_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_varw_63d_base_v149_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_varw_63d_base_v150_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 63).rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_tanhw_5d_base_v076_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_tanhw_5d_base_v077_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_tanhw_5d_base_v078_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_tanhw_10d_base_v079_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_tanhw_10d_base_v080_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_tanhw_10d_base_v081_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_tanhw_21d_base_v082_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_tanhw_21d_base_v083_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_tanhw_21d_base_v084_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_tanhw_42d_base_v085_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_tanhw_42d_base_v086_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_tanhw_42d_base_v087_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_tanhw_63d_base_v088_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_tanhw_63d_base_v089_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_tanhw_63d_base_v090_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_tanhw_126d_base_v091_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_tanhw_126d_base_v092_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_tanhw_126d_base_v093_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_tanhw_189d_base_v094_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_tanhw_189d_base_v095_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_tanhw_189d_base_v096_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_tanhw_252d_base_v097_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_tanhw_252d_base_v098_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_tanhw_252d_base_v099_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_tanhw_378d_base_v100_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_tanhw_378d_base_v101_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_tanhw_378d_base_v102_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_tanhw_504d_base_v103_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_tanhw_504d_base_v104_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_tanhw_504d_base_v105_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_zclipw_5d_base_v106_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_zclipw_5d_base_v107_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_zclipw_5d_base_v108_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_zclipw_10d_base_v109_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_zclipw_10d_base_v110_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_zclipw_10d_base_v111_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_zclipw_21d_base_v112_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_zclipw_21d_base_v113_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_zclipw_21d_base_v114_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_zclipw_42d_base_v115_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_zclipw_42d_base_v116_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_zclipw_42d_base_v117_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_zclipw_63d_base_v118_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_zclipw_63d_base_v119_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_zclipw_63d_base_v120_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_zclipw_126d_base_v121_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_zclipw_126d_base_v122_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_zclipw_126d_base_v123_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_zclipw_189d_base_v124_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_zclipw_189d_base_v125_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_zclipw_189d_base_v126_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_zclipw_252d_base_v127_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_zclipw_252d_base_v128_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_zclipw_252d_base_v129_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_zclipw_378d_base_v130_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_zclipw_378d_base_v131_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_zclipw_378d_base_v132_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_zclipw_504d_base_v133_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_zclipw_504d_base_v134_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_zclipw_504d_base_v135_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_varw_5d_base_v136_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_varw_5d_base_v137_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_varw_5d_base_v138_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_varw_10d_base_v139_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_varw_10d_base_v140_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_varw_10d_base_v141_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_varw_21d_base_v142_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_varw_21d_base_v143_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_varw_21d_base_v144_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_varw_42d_base_v145_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_varw_42d_base_v146_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_varw_42d_base_v147_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_varw_63d_base_v148_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_varw_63d_base_v149_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_varw_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F092_INSTITUTIONAL_OWNERSHIP_BUILDUP_PROXY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    marketcap = pd.Series(closeadj * 1e8, name="marketcap")
    dps = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    payoutratio = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    roic = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    cols = {
        "closeadj": closeadj, "volume": volume, "sharesbas": sharesbas,
        "marketcap": marketcap, "dps": dps, "payoutratio": payoutratio,
        "roic": roic,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f092_marketcap_trend", "_f092_mc_per_share", "_f092_inst_buildup_proxy")
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
    print(f"OK f092_institutional_ownership_buildup_proxy_base_076_150_claude: {n_features} features pass")
