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
def _f13_margin_floor(grossmargin, w):
    return grossmargin.rolling(w, min_periods=max(1, w // 2)).min()


def _f13_margin_quality(ebitdamargin, w):
    m = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f13_margin_consistency(grossmargin, ebitdamargin, w):
    gs = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    es = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return 1.0 / (1.0 + gs + es)

def f13dmq_f13_diagnostics_margin_quality_qualmean_126d_base_v076_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 126)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualmean_189d_base_v077_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 189)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualmean_252d_base_v078_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualmean_378d_base_v079_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 378)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualmean_504d_base_v080_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 504)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorema_5d_base_v081_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 5)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorema_10d_base_v082_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 10)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorema_21d_base_v083_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 21)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorema_42d_base_v084_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 42)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorema_63d_base_v085_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 63)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorema_126d_base_v086_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 126)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorema_189d_base_v087_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 189)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorema_252d_base_v088_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 252)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorema_378d_base_v089_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 378)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorema_504d_base_v090_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 504)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_conslog_5d_base_v091_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 5)
    result = np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_conslog_10d_base_v092_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 10)
    result = np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_conslog_21d_base_v093_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 21)
    result = np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_conslog_42d_base_v094_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 42)
    result = np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_conslog_63d_base_v095_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 63)
    result = np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_conslog_126d_base_v096_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 126)
    result = np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_conslog_189d_base_v097_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 189)
    result = np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_conslog_252d_base_v098_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 252)
    result = np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_conslog_378d_base_v099_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 378)
    result = np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_conslog_504d_base_v100_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 504)
    result = np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualz_5d_base_v101_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 5)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualz_10d_base_v102_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 10)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualz_21d_base_v103_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualz_42d_base_v104_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 42)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualz_63d_base_v105_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualz_126d_base_v106_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 126)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualz_189d_base_v107_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 189)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualz_252d_base_v108_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualz_378d_base_v109_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 378)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualz_504d_base_v110_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 504)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorxnm_5d_base_v111_signal(grossmargin, netmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 5)
    result = base * netmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorxnm_10d_base_v112_signal(grossmargin, netmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 10)
    result = base * netmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorxnm_21d_base_v113_signal(grossmargin, netmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 21)
    result = base * netmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorxnm_42d_base_v114_signal(grossmargin, netmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 42)
    result = base * netmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorxnm_63d_base_v115_signal(grossmargin, netmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 63)
    result = base * netmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorxnm_126d_base_v116_signal(grossmargin, netmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 126)
    result = base * netmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorxnm_189d_base_v117_signal(grossmargin, netmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 189)
    result = base * netmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorxnm_252d_base_v118_signal(grossmargin, netmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 252)
    result = base * netmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorxnm_378d_base_v119_signal(grossmargin, netmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 378)
    result = base * netmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorxnm_504d_base_v120_signal(grossmargin, netmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 504)
    result = base * netmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_consmean_5d_base_v121_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_consmean_10d_base_v122_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 10)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_consmean_21d_base_v123_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_consmean_42d_base_v124_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 42)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_consmean_63d_base_v125_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_consmean_126d_base_v126_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 126)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_consmean_189d_base_v127_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 189)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_consmean_252d_base_v128_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_consmean_378d_base_v129_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 378)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_consmean_504d_base_v130_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 504)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_5d_base_v131_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 5)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 5)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_10d_base_v132_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 10)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 10)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_21d_base_v133_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 21)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 21)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_42d_base_v134_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 42)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 42)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_63d_base_v135_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 63)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 63)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_126d_base_v136_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 126)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 126)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_189d_base_v137_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 189)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 189)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_252d_base_v138_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 252)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 252)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_378d_base_v139_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 378)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 378)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_504d_base_v140_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 504)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 504)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorstd_5d_base_v141_signal(grossmargin, closeadj):
    f = _f13_margin_floor(grossmargin, 5)
    base = _std(f, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorstd_10d_base_v142_signal(grossmargin, closeadj):
    f = _f13_margin_floor(grossmargin, 10)
    base = _std(f, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorstd_21d_base_v143_signal(grossmargin, closeadj):
    f = _f13_margin_floor(grossmargin, 21)
    base = _std(f, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorstd_42d_base_v144_signal(grossmargin, closeadj):
    f = _f13_margin_floor(grossmargin, 42)
    base = _std(f, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorstd_63d_base_v145_signal(grossmargin, closeadj):
    f = _f13_margin_floor(grossmargin, 63)
    base = _std(f, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorstd_126d_base_v146_signal(grossmargin, closeadj):
    f = _f13_margin_floor(grossmargin, 126)
    base = _std(f, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorstd_189d_base_v147_signal(grossmargin, closeadj):
    f = _f13_margin_floor(grossmargin, 189)
    base = _std(f, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorstd_252d_base_v148_signal(grossmargin, closeadj):
    f = _f13_margin_floor(grossmargin, 252)
    base = _std(f, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorstd_378d_base_v149_signal(grossmargin, closeadj):
    f = _f13_margin_floor(grossmargin, 378)
    base = _std(f, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorstd_504d_base_v150_signal(grossmargin, closeadj):
    f = _f13_margin_floor(grossmargin, 504)
    base = _std(f, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f13dmq_f13_diagnostics_margin_quality_qualmean_126d_base_v076_signal,
    f13dmq_f13_diagnostics_margin_quality_qualmean_189d_base_v077_signal,
    f13dmq_f13_diagnostics_margin_quality_qualmean_252d_base_v078_signal,
    f13dmq_f13_diagnostics_margin_quality_qualmean_378d_base_v079_signal,
    f13dmq_f13_diagnostics_margin_quality_qualmean_504d_base_v080_signal,
    f13dmq_f13_diagnostics_margin_quality_floorema_5d_base_v081_signal,
    f13dmq_f13_diagnostics_margin_quality_floorema_10d_base_v082_signal,
    f13dmq_f13_diagnostics_margin_quality_floorema_21d_base_v083_signal,
    f13dmq_f13_diagnostics_margin_quality_floorema_42d_base_v084_signal,
    f13dmq_f13_diagnostics_margin_quality_floorema_63d_base_v085_signal,
    f13dmq_f13_diagnostics_margin_quality_floorema_126d_base_v086_signal,
    f13dmq_f13_diagnostics_margin_quality_floorema_189d_base_v087_signal,
    f13dmq_f13_diagnostics_margin_quality_floorema_252d_base_v088_signal,
    f13dmq_f13_diagnostics_margin_quality_floorema_378d_base_v089_signal,
    f13dmq_f13_diagnostics_margin_quality_floorema_504d_base_v090_signal,
    f13dmq_f13_diagnostics_margin_quality_conslog_5d_base_v091_signal,
    f13dmq_f13_diagnostics_margin_quality_conslog_10d_base_v092_signal,
    f13dmq_f13_diagnostics_margin_quality_conslog_21d_base_v093_signal,
    f13dmq_f13_diagnostics_margin_quality_conslog_42d_base_v094_signal,
    f13dmq_f13_diagnostics_margin_quality_conslog_63d_base_v095_signal,
    f13dmq_f13_diagnostics_margin_quality_conslog_126d_base_v096_signal,
    f13dmq_f13_diagnostics_margin_quality_conslog_189d_base_v097_signal,
    f13dmq_f13_diagnostics_margin_quality_conslog_252d_base_v098_signal,
    f13dmq_f13_diagnostics_margin_quality_conslog_378d_base_v099_signal,
    f13dmq_f13_diagnostics_margin_quality_conslog_504d_base_v100_signal,
    f13dmq_f13_diagnostics_margin_quality_qualz_5d_base_v101_signal,
    f13dmq_f13_diagnostics_margin_quality_qualz_10d_base_v102_signal,
    f13dmq_f13_diagnostics_margin_quality_qualz_21d_base_v103_signal,
    f13dmq_f13_diagnostics_margin_quality_qualz_42d_base_v104_signal,
    f13dmq_f13_diagnostics_margin_quality_qualz_63d_base_v105_signal,
    f13dmq_f13_diagnostics_margin_quality_qualz_126d_base_v106_signal,
    f13dmq_f13_diagnostics_margin_quality_qualz_189d_base_v107_signal,
    f13dmq_f13_diagnostics_margin_quality_qualz_252d_base_v108_signal,
    f13dmq_f13_diagnostics_margin_quality_qualz_378d_base_v109_signal,
    f13dmq_f13_diagnostics_margin_quality_qualz_504d_base_v110_signal,
    f13dmq_f13_diagnostics_margin_quality_floorxnm_5d_base_v111_signal,
    f13dmq_f13_diagnostics_margin_quality_floorxnm_10d_base_v112_signal,
    f13dmq_f13_diagnostics_margin_quality_floorxnm_21d_base_v113_signal,
    f13dmq_f13_diagnostics_margin_quality_floorxnm_42d_base_v114_signal,
    f13dmq_f13_diagnostics_margin_quality_floorxnm_63d_base_v115_signal,
    f13dmq_f13_diagnostics_margin_quality_floorxnm_126d_base_v116_signal,
    f13dmq_f13_diagnostics_margin_quality_floorxnm_189d_base_v117_signal,
    f13dmq_f13_diagnostics_margin_quality_floorxnm_252d_base_v118_signal,
    f13dmq_f13_diagnostics_margin_quality_floorxnm_378d_base_v119_signal,
    f13dmq_f13_diagnostics_margin_quality_floorxnm_504d_base_v120_signal,
    f13dmq_f13_diagnostics_margin_quality_consmean_5d_base_v121_signal,
    f13dmq_f13_diagnostics_margin_quality_consmean_10d_base_v122_signal,
    f13dmq_f13_diagnostics_margin_quality_consmean_21d_base_v123_signal,
    f13dmq_f13_diagnostics_margin_quality_consmean_42d_base_v124_signal,
    f13dmq_f13_diagnostics_margin_quality_consmean_63d_base_v125_signal,
    f13dmq_f13_diagnostics_margin_quality_consmean_126d_base_v126_signal,
    f13dmq_f13_diagnostics_margin_quality_consmean_189d_base_v127_signal,
    f13dmq_f13_diagnostics_margin_quality_consmean_252d_base_v128_signal,
    f13dmq_f13_diagnostics_margin_quality_consmean_378d_base_v129_signal,
    f13dmq_f13_diagnostics_margin_quality_consmean_504d_base_v130_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_5d_base_v131_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_10d_base_v132_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_21d_base_v133_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_42d_base_v134_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_63d_base_v135_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_126d_base_v136_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_189d_base_v137_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_252d_base_v138_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_378d_base_v139_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_504d_base_v140_signal,
    f13dmq_f13_diagnostics_margin_quality_floorstd_5d_base_v141_signal,
    f13dmq_f13_diagnostics_margin_quality_floorstd_10d_base_v142_signal,
    f13dmq_f13_diagnostics_margin_quality_floorstd_21d_base_v143_signal,
    f13dmq_f13_diagnostics_margin_quality_floorstd_42d_base_v144_signal,
    f13dmq_f13_diagnostics_margin_quality_floorstd_63d_base_v145_signal,
    f13dmq_f13_diagnostics_margin_quality_floorstd_126d_base_v146_signal,
    f13dmq_f13_diagnostics_margin_quality_floorstd_189d_base_v147_signal,
    f13dmq_f13_diagnostics_margin_quality_floorstd_252d_base_v148_signal,
    f13dmq_f13_diagnostics_margin_quality_floorstd_378d_base_v149_signal,
    f13dmq_f13_diagnostics_margin_quality_floorstd_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F13_DIAGNOSTICS_MARGIN_QUALITY_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f13_margin_floor", "_f13_margin_quality", "_f13_margin_consistency",)
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
    print(f"OK f13_diagnostics_margin_quality_base_076_150_claude: {n_features} features pass")
