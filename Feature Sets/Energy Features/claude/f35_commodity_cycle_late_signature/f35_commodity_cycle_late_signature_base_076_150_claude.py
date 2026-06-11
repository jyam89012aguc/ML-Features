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
    return s.ewm(span=max(2, w), adjust=False, min_periods=max(1, w // 2)).mean()

# ===== folder domain primitives =====
def _f35_capex_pulse(capex, w):
    m = capex.rolling(w, min_periods=max(1, w // 2)).mean()
    return (capex - m) / m.replace(0, np.nan).abs()

def _f35_margin_extreme(ebitdamargin, w):
    mx = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).max()
    m = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return (mx - m)

def _f35_cycle_late_score(capex, ebitdamargin, w):
    cp = capex.rolling(w, min_periods=max(1, w // 2)).mean()
    cz = (capex - cp) / capex.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    mz = (ebitdamargin - ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()) / ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    return cz + mz


def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc252_42d_base_v076_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 42)
    result = base.abs() * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xema21c_42d_base_v077_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 42)
    result = base.abs() * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xema63c_42d_base_v078_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 42)
    result = base.abs() * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xc_63d_base_v079_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc21_63d_base_v080_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 63)
    result = base.abs() * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc63_63d_base_v081_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 63)
    result = base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc252_63d_base_v082_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 63)
    result = base.abs() * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xema21c_63d_base_v083_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 63)
    result = base.abs() * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xema63c_63d_base_v084_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 63)
    result = base.abs() * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xc_126d_base_v085_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc21_126d_base_v086_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 126)
    result = base.abs() * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc63_126d_base_v087_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 126)
    result = base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc252_126d_base_v088_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 126)
    result = base.abs() * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xema21c_126d_base_v089_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 126)
    result = base.abs() * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xema63c_126d_base_v090_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 126)
    result = base.abs() * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xc_189d_base_v091_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc21_189d_base_v092_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 189)
    result = base.abs() * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc63_189d_base_v093_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 189)
    result = base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc252_189d_base_v094_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 189)
    result = base.abs() * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xema21c_189d_base_v095_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 189)
    result = base.abs() * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xema63c_189d_base_v096_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 189)
    result = base.abs() * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xc_252d_base_v097_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc21_252d_base_v098_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 252)
    result = base.abs() * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc63_252d_base_v099_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 252)
    result = base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc252_252d_base_v100_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 252)
    result = base.abs() * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xema21c_252d_base_v101_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 252)
    result = base.abs() * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xema63c_252d_base_v102_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 252)
    result = base.abs() * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xc_378d_base_v103_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc21_378d_base_v104_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 378)
    result = base.abs() * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc63_378d_base_v105_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 378)
    result = base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc252_378d_base_v106_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 378)
    result = base.abs() * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xema21c_378d_base_v107_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 378)
    result = base.abs() * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xema63c_378d_base_v108_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 378)
    result = base.abs() * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xc_5d_base_v109_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 5)
    result = (base * base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc21_5d_base_v110_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 5)
    result = (base * base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc63_5d_base_v111_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 5)
    result = (base * base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc252_5d_base_v112_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 5)
    result = (base * base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema21c_5d_base_v113_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 5)
    result = (base * base) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema63c_5d_base_v114_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 5)
    result = (base * base) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xc_10d_base_v115_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 10)
    result = (base * base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc21_10d_base_v116_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 10)
    result = (base * base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc63_10d_base_v117_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 10)
    result = (base * base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc252_10d_base_v118_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 10)
    result = (base * base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema21c_10d_base_v119_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 10)
    result = (base * base) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema63c_10d_base_v120_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 10)
    result = (base * base) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xc_21d_base_v121_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 21)
    result = (base * base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc21_21d_base_v122_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 21)
    result = (base * base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc63_21d_base_v123_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 21)
    result = (base * base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc252_21d_base_v124_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 21)
    result = (base * base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema21c_21d_base_v125_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 21)
    result = (base * base) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema63c_21d_base_v126_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 21)
    result = (base * base) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xc_42d_base_v127_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 42)
    result = (base * base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc21_42d_base_v128_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 42)
    result = (base * base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc63_42d_base_v129_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 42)
    result = (base * base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc252_42d_base_v130_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 42)
    result = (base * base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema21c_42d_base_v131_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 42)
    result = (base * base) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema63c_42d_base_v132_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 42)
    result = (base * base) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xc_63d_base_v133_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 63)
    result = (base * base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc21_63d_base_v134_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 63)
    result = (base * base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc63_63d_base_v135_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 63)
    result = (base * base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc252_63d_base_v136_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 63)
    result = (base * base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema21c_63d_base_v137_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 63)
    result = (base * base) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema63c_63d_base_v138_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 63)
    result = (base * base) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xc_126d_base_v139_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 126)
    result = (base * base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc21_126d_base_v140_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 126)
    result = (base * base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc63_126d_base_v141_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 126)
    result = (base * base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc252_126d_base_v142_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 126)
    result = (base * base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema21c_126d_base_v143_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 126)
    result = (base * base) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema63c_126d_base_v144_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 126)
    result = (base * base) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xc_189d_base_v145_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 189)
    result = (base * base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc21_189d_base_v146_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 189)
    result = (base * base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc63_189d_base_v147_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 189)
    result = (base * base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc252_189d_base_v148_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 189)
    result = (base * base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema21c_189d_base_v149_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 189)
    result = (base * base) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema63c_189d_base_v150_signal(capex, closeadj):
    base = _f35_capex_pulse(capex, 189)
    result = (base * base) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc252_42d_base_v076_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xema21c_42d_base_v077_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xema63c_42d_base_v078_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xc_63d_base_v079_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc21_63d_base_v080_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc63_63d_base_v081_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc252_63d_base_v082_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xema21c_63d_base_v083_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xema63c_63d_base_v084_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xc_126d_base_v085_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc21_126d_base_v086_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc63_126d_base_v087_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc252_126d_base_v088_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xema21c_126d_base_v089_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xema63c_126d_base_v090_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xc_189d_base_v091_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc21_189d_base_v092_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc63_189d_base_v093_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc252_189d_base_v094_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xema21c_189d_base_v095_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xema63c_189d_base_v096_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xc_252d_base_v097_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc21_252d_base_v098_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc63_252d_base_v099_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc252_252d_base_v100_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xema21c_252d_base_v101_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xema63c_252d_base_v102_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xc_378d_base_v103_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc21_378d_base_v104_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc63_378d_base_v105_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xmc252_378d_base_v106_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xema21c_378d_base_v107_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_absv_xema63c_378d_base_v108_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xc_5d_base_v109_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc21_5d_base_v110_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc63_5d_base_v111_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc252_5d_base_v112_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema21c_5d_base_v113_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema63c_5d_base_v114_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xc_10d_base_v115_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc21_10d_base_v116_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc63_10d_base_v117_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc252_10d_base_v118_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema21c_10d_base_v119_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema63c_10d_base_v120_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xc_21d_base_v121_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc21_21d_base_v122_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc63_21d_base_v123_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc252_21d_base_v124_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema21c_21d_base_v125_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema63c_21d_base_v126_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xc_42d_base_v127_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc21_42d_base_v128_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc63_42d_base_v129_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc252_42d_base_v130_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema21c_42d_base_v131_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema63c_42d_base_v132_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xc_63d_base_v133_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc21_63d_base_v134_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc63_63d_base_v135_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc252_63d_base_v136_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema21c_63d_base_v137_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema63c_63d_base_v138_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xc_126d_base_v139_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc21_126d_base_v140_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc63_126d_base_v141_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc252_126d_base_v142_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema21c_126d_base_v143_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema63c_126d_base_v144_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xc_189d_base_v145_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc21_189d_base_v146_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc63_189d_base_v147_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xmc252_189d_base_v148_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema21c_189d_base_v149_signal,
    f35ccl_f35_commodity_cycle_late_signature_cxpuls_sq_xema63c_189d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F35_COMMODITY_CYCLE_LATE_SIGNATURE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    debt    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    de = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue,
        "ebitda": ebitda,
        "netinc": netinc,
        "fcf": fcf,
        "capex": capex,
        "debt": debt,
        "ebitdamargin": ebitdamargin,
        "de": de,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f35_capex_pulse", "_f35_margin_extreme", "_f35_cycle_late_score",)
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
    print(f"OK f35_commodity_cycle_late_signature_076_150_claude: {n_features} features pass")
