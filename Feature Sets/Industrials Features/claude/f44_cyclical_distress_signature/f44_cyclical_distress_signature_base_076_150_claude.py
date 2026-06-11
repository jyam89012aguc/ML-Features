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
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


# ===== folder domain primitives =====
def _f44_distress_proxy(debt, ebitda, w):
    ratio = debt / ebitda.replace(0, np.nan).abs()
    return ratio.rolling(w, min_periods=max(1, w // 2)).mean()


def _f44_collapse_risk(de, ebitdamargin, w):
    risk = de / ebitdamargin.replace(0, np.nan).abs()
    return risk.rolling(w, min_periods=max(1, w // 2)).mean()


def _f44_cyclical_stress(debt, fcf, ebitda, w):
    cov = fcf.rolling(w, min_periods=max(1, w // 2)).sum() / debt.replace(0, np.nan).abs()
    eb_var = ebitda.rolling(w, min_periods=max(1, w // 2)).std() / ebitda.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan).abs()
    return eb_var / cov.replace(0, np.nan).abs()

# feature 76: stress_126d_xc
def f44cds_f44_cyclical_distress_signature_stress_126d_xc_base_v076_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 126)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 77: stress_126d_xclog
def f44cds_f44_cyclical_distress_signature_stress_126d_xclog_base_v077_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 126)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 78: stress_126d_xcm21
def f44cds_f44_cyclical_distress_signature_stress_126d_xcm21_base_v078_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 126)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 79: stress_189d_xc
def f44cds_f44_cyclical_distress_signature_stress_189d_xc_base_v079_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 189)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 80: stress_189d_xclog
def f44cds_f44_cyclical_distress_signature_stress_189d_xclog_base_v080_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 189)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 81: stress_189d_xcm21
def f44cds_f44_cyclical_distress_signature_stress_189d_xcm21_base_v081_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 189)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 82: stress_252d_xc
def f44cds_f44_cyclical_distress_signature_stress_252d_xc_base_v082_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 252)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 83: stress_252d_xclog
def f44cds_f44_cyclical_distress_signature_stress_252d_xclog_base_v083_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 252)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 84: stress_252d_xcm21
def f44cds_f44_cyclical_distress_signature_stress_252d_xcm21_base_v084_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 252)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 85: stress_378d_xc
def f44cds_f44_cyclical_distress_signature_stress_378d_xc_base_v085_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 378)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 86: stress_378d_xclog
def f44cds_f44_cyclical_distress_signature_stress_378d_xclog_base_v086_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 378)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 87: stress_378d_xcm21
def f44cds_f44_cyclical_distress_signature_stress_378d_xcm21_base_v087_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 378)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 88: stress_504d_xc
def f44cds_f44_cyclical_distress_signature_stress_504d_xc_base_v088_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 504)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 89: stress_504d_xclog
def f44cds_f44_cyclical_distress_signature_stress_504d_xclog_base_v089_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 504)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 90: stress_504d_xcm21
def f44cds_f44_cyclical_distress_signature_stress_504d_xcm21_base_v090_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 504)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 91: distressxcollapse_21d
def f44cds_f44_cyclical_distress_signature_distressxcollapse_21d_base_v091_signal(debt, ebitda, de, ebitdamargin, closeadj):
    a = _f44_distress_proxy(debt, ebitda, 21)
    b = _f44_collapse_risk(de, ebitdamargin, 21)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 92: distressxstress_21d
def f44cds_f44_cyclical_distress_signature_distressxstress_21d_base_v092_signal(debt, ebitda, fcf, closeadj):
    a = _f44_distress_proxy(debt, ebitda, 21)
    b = _f44_cyclical_stress(debt, fcf, ebitda, 21)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 93: distress_z_21d
def f44cds_f44_cyclical_distress_signature_distress_z_21d_base_v093_signal(debt, ebitda, closeadj):
    base = _f44_distress_proxy(debt, ebitda, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 94: collapse_z_21d
def f44cds_f44_cyclical_distress_signature_collapse_z_21d_base_v094_signal(de, ebitdamargin, closeadj):
    base = _f44_collapse_risk(de, ebitdamargin, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 95: stress_z_21d
def f44cds_f44_cyclical_distress_signature_stress_z_21d_base_v095_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 96: distress_ema_21d
def f44cds_f44_cyclical_distress_signature_distress_ema_21d_base_v096_signal(debt, ebitda, closeadj):
    base = _f44_distress_proxy(debt, ebitda, 21)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 97: collapse_ema_21d
def f44cds_f44_cyclical_distress_signature_collapse_ema_21d_base_v097_signal(de, ebitdamargin, closeadj):
    base = _f44_collapse_risk(de, ebitdamargin, 21)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 98: stress_ema_21d
def f44cds_f44_cyclical_distress_signature_stress_ema_21d_base_v098_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 21)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 99: distress_sq_21d
def f44cds_f44_cyclical_distress_signature_distress_sq_21d_base_v099_signal(debt, ebitda, closeadj):
    base = _f44_distress_proxy(debt, ebitda, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 100: collapsexstress_21d
def f44cds_f44_cyclical_distress_signature_collapsexstress_21d_base_v100_signal(de, ebitdamargin, debt, fcf, ebitda, closeadj):
    a = _f44_collapse_risk(de, ebitdamargin, 21)
    b = _f44_cyclical_stress(debt, fcf, ebitda, 21)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 101: distressxcollapse_42d
def f44cds_f44_cyclical_distress_signature_distressxcollapse_42d_base_v101_signal(debt, ebitda, de, ebitdamargin, closeadj):
    a = _f44_distress_proxy(debt, ebitda, 42)
    b = _f44_collapse_risk(de, ebitdamargin, 42)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 102: distressxstress_42d
def f44cds_f44_cyclical_distress_signature_distressxstress_42d_base_v102_signal(debt, ebitda, fcf, closeadj):
    a = _f44_distress_proxy(debt, ebitda, 42)
    b = _f44_cyclical_stress(debt, fcf, ebitda, 42)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 103: distress_z_42d
def f44cds_f44_cyclical_distress_signature_distress_z_42d_base_v103_signal(debt, ebitda, closeadj):
    base = _f44_distress_proxy(debt, ebitda, 42)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 104: collapse_z_42d
def f44cds_f44_cyclical_distress_signature_collapse_z_42d_base_v104_signal(de, ebitdamargin, closeadj):
    base = _f44_collapse_risk(de, ebitdamargin, 42)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 105: stress_z_42d
def f44cds_f44_cyclical_distress_signature_stress_z_42d_base_v105_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 42)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 106: distress_ema_42d
def f44cds_f44_cyclical_distress_signature_distress_ema_42d_base_v106_signal(debt, ebitda, closeadj):
    base = _f44_distress_proxy(debt, ebitda, 42)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 107: collapse_ema_42d
def f44cds_f44_cyclical_distress_signature_collapse_ema_42d_base_v107_signal(de, ebitdamargin, closeadj):
    base = _f44_collapse_risk(de, ebitdamargin, 42)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 108: stress_ema_42d
def f44cds_f44_cyclical_distress_signature_stress_ema_42d_base_v108_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 42)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 109: distress_sq_42d
def f44cds_f44_cyclical_distress_signature_distress_sq_42d_base_v109_signal(debt, ebitda, closeadj):
    base = _f44_distress_proxy(debt, ebitda, 42)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 110: collapsexstress_42d
def f44cds_f44_cyclical_distress_signature_collapsexstress_42d_base_v110_signal(de, ebitdamargin, debt, fcf, ebitda, closeadj):
    a = _f44_collapse_risk(de, ebitdamargin, 42)
    b = _f44_cyclical_stress(debt, fcf, ebitda, 42)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 111: distressxcollapse_63d
def f44cds_f44_cyclical_distress_signature_distressxcollapse_63d_base_v111_signal(debt, ebitda, de, ebitdamargin, closeadj):
    a = _f44_distress_proxy(debt, ebitda, 63)
    b = _f44_collapse_risk(de, ebitdamargin, 63)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 112: distressxstress_63d
def f44cds_f44_cyclical_distress_signature_distressxstress_63d_base_v112_signal(debt, ebitda, fcf, closeadj):
    a = _f44_distress_proxy(debt, ebitda, 63)
    b = _f44_cyclical_stress(debt, fcf, ebitda, 63)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 113: distress_z_63d
def f44cds_f44_cyclical_distress_signature_distress_z_63d_base_v113_signal(debt, ebitda, closeadj):
    base = _f44_distress_proxy(debt, ebitda, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 114: collapse_z_63d
def f44cds_f44_cyclical_distress_signature_collapse_z_63d_base_v114_signal(de, ebitdamargin, closeadj):
    base = _f44_collapse_risk(de, ebitdamargin, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 115: stress_z_63d
def f44cds_f44_cyclical_distress_signature_stress_z_63d_base_v115_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 116: distress_ema_63d
def f44cds_f44_cyclical_distress_signature_distress_ema_63d_base_v116_signal(debt, ebitda, closeadj):
    base = _f44_distress_proxy(debt, ebitda, 63)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 117: collapse_ema_63d
def f44cds_f44_cyclical_distress_signature_collapse_ema_63d_base_v117_signal(de, ebitdamargin, closeadj):
    base = _f44_collapse_risk(de, ebitdamargin, 63)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 118: stress_ema_63d
def f44cds_f44_cyclical_distress_signature_stress_ema_63d_base_v118_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 63)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 119: distress_sq_63d
def f44cds_f44_cyclical_distress_signature_distress_sq_63d_base_v119_signal(debt, ebitda, closeadj):
    base = _f44_distress_proxy(debt, ebitda, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 120: collapsexstress_63d
def f44cds_f44_cyclical_distress_signature_collapsexstress_63d_base_v120_signal(de, ebitdamargin, debt, fcf, ebitda, closeadj):
    a = _f44_collapse_risk(de, ebitdamargin, 63)
    b = _f44_cyclical_stress(debt, fcf, ebitda, 63)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 121: distressxcollapse_126d
def f44cds_f44_cyclical_distress_signature_distressxcollapse_126d_base_v121_signal(debt, ebitda, de, ebitdamargin, closeadj):
    a = _f44_distress_proxy(debt, ebitda, 126)
    b = _f44_collapse_risk(de, ebitdamargin, 126)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 122: distressxstress_126d
def f44cds_f44_cyclical_distress_signature_distressxstress_126d_base_v122_signal(debt, ebitda, fcf, closeadj):
    a = _f44_distress_proxy(debt, ebitda, 126)
    b = _f44_cyclical_stress(debt, fcf, ebitda, 126)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 123: distress_z_126d
def f44cds_f44_cyclical_distress_signature_distress_z_126d_base_v123_signal(debt, ebitda, closeadj):
    base = _f44_distress_proxy(debt, ebitda, 126)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 124: collapse_z_126d
def f44cds_f44_cyclical_distress_signature_collapse_z_126d_base_v124_signal(de, ebitdamargin, closeadj):
    base = _f44_collapse_risk(de, ebitdamargin, 126)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 125: stress_z_126d
def f44cds_f44_cyclical_distress_signature_stress_z_126d_base_v125_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 126)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 126: distress_ema_126d
def f44cds_f44_cyclical_distress_signature_distress_ema_126d_base_v126_signal(debt, ebitda, closeadj):
    base = _f44_distress_proxy(debt, ebitda, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 127: collapse_ema_126d
def f44cds_f44_cyclical_distress_signature_collapse_ema_126d_base_v127_signal(de, ebitdamargin, closeadj):
    base = _f44_collapse_risk(de, ebitdamargin, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 128: stress_ema_126d
def f44cds_f44_cyclical_distress_signature_stress_ema_126d_base_v128_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 129: distress_sq_126d
def f44cds_f44_cyclical_distress_signature_distress_sq_126d_base_v129_signal(debt, ebitda, closeadj):
    base = _f44_distress_proxy(debt, ebitda, 126)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 130: collapsexstress_126d
def f44cds_f44_cyclical_distress_signature_collapsexstress_126d_base_v130_signal(de, ebitdamargin, debt, fcf, ebitda, closeadj):
    a = _f44_collapse_risk(de, ebitdamargin, 126)
    b = _f44_cyclical_stress(debt, fcf, ebitda, 126)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 131: distressxcollapse_252d
def f44cds_f44_cyclical_distress_signature_distressxcollapse_252d_base_v131_signal(debt, ebitda, de, ebitdamargin, closeadj):
    a = _f44_distress_proxy(debt, ebitda, 252)
    b = _f44_collapse_risk(de, ebitdamargin, 252)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 132: distressxstress_252d
def f44cds_f44_cyclical_distress_signature_distressxstress_252d_base_v132_signal(debt, ebitda, fcf, closeadj):
    a = _f44_distress_proxy(debt, ebitda, 252)
    b = _f44_cyclical_stress(debt, fcf, ebitda, 252)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 133: distress_z_252d
def f44cds_f44_cyclical_distress_signature_distress_z_252d_base_v133_signal(debt, ebitda, closeadj):
    base = _f44_distress_proxy(debt, ebitda, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 134: collapse_z_252d
def f44cds_f44_cyclical_distress_signature_collapse_z_252d_base_v134_signal(de, ebitdamargin, closeadj):
    base = _f44_collapse_risk(de, ebitdamargin, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 135: stress_z_252d
def f44cds_f44_cyclical_distress_signature_stress_z_252d_base_v135_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 136: distress_ema_252d
def f44cds_f44_cyclical_distress_signature_distress_ema_252d_base_v136_signal(debt, ebitda, closeadj):
    base = _f44_distress_proxy(debt, ebitda, 252)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 137: collapse_ema_252d
def f44cds_f44_cyclical_distress_signature_collapse_ema_252d_base_v137_signal(de, ebitdamargin, closeadj):
    base = _f44_collapse_risk(de, ebitdamargin, 252)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 138: stress_ema_252d
def f44cds_f44_cyclical_distress_signature_stress_ema_252d_base_v138_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 252)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 139: distress_sq_252d
def f44cds_f44_cyclical_distress_signature_distress_sq_252d_base_v139_signal(debt, ebitda, closeadj):
    base = _f44_distress_proxy(debt, ebitda, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 140: collapsexstress_252d
def f44cds_f44_cyclical_distress_signature_collapsexstress_252d_base_v140_signal(de, ebitdamargin, debt, fcf, ebitda, closeadj):
    a = _f44_collapse_risk(de, ebitdamargin, 252)
    b = _f44_cyclical_stress(debt, fcf, ebitda, 252)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 141: distress_long_10d
def f44cds_f44_cyclical_distress_signature_distress_long_10d_base_v141_signal(debt, ebitda, closeadj):
    base = _f44_distress_proxy(debt, ebitda, 10)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 142: collapse_long_10d
def f44cds_f44_cyclical_distress_signature_collapse_long_10d_base_v142_signal(de, ebitdamargin, closeadj):
    base = _f44_collapse_risk(de, ebitdamargin, 10)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 143: stress_long_10d
def f44cds_f44_cyclical_distress_signature_stress_long_10d_base_v143_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 10)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 144: distress_long_42d
def f44cds_f44_cyclical_distress_signature_distress_long_42d_base_v144_signal(debt, ebitda, closeadj):
    base = _f44_distress_proxy(debt, ebitda, 42)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 145: collapse_long_42d
def f44cds_f44_cyclical_distress_signature_collapse_long_42d_base_v145_signal(de, ebitdamargin, closeadj):
    base = _f44_collapse_risk(de, ebitdamargin, 42)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 146: stress_long_42d
def f44cds_f44_cyclical_distress_signature_stress_long_42d_base_v146_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 42)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 147: distress_long_189d
def f44cds_f44_cyclical_distress_signature_distress_long_189d_base_v147_signal(debt, ebitda, closeadj):
    base = _f44_distress_proxy(debt, ebitda, 189)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 148: collapse_long_189d
def f44cds_f44_cyclical_distress_signature_collapse_long_189d_base_v148_signal(de, ebitdamargin, closeadj):
    base = _f44_collapse_risk(de, ebitdamargin, 189)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 149: stress_long_189d
def f44cds_f44_cyclical_distress_signature_stress_long_189d_base_v149_signal(debt, fcf, ebitda, closeadj):
    base = _f44_cyclical_stress(debt, fcf, ebitda, 189)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 150: distress_long_378d
def f44cds_f44_cyclical_distress_signature_distress_long_378d_base_v150_signal(debt, ebitda, closeadj):
    base = _f44_distress_proxy(debt, ebitda, 378)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f44cds_f44_cyclical_distress_signature_stress_126d_xc_base_v076_signal,
    f44cds_f44_cyclical_distress_signature_stress_126d_xclog_base_v077_signal,
    f44cds_f44_cyclical_distress_signature_stress_126d_xcm21_base_v078_signal,
    f44cds_f44_cyclical_distress_signature_stress_189d_xc_base_v079_signal,
    f44cds_f44_cyclical_distress_signature_stress_189d_xclog_base_v080_signal,
    f44cds_f44_cyclical_distress_signature_stress_189d_xcm21_base_v081_signal,
    f44cds_f44_cyclical_distress_signature_stress_252d_xc_base_v082_signal,
    f44cds_f44_cyclical_distress_signature_stress_252d_xclog_base_v083_signal,
    f44cds_f44_cyclical_distress_signature_stress_252d_xcm21_base_v084_signal,
    f44cds_f44_cyclical_distress_signature_stress_378d_xc_base_v085_signal,
    f44cds_f44_cyclical_distress_signature_stress_378d_xclog_base_v086_signal,
    f44cds_f44_cyclical_distress_signature_stress_378d_xcm21_base_v087_signal,
    f44cds_f44_cyclical_distress_signature_stress_504d_xc_base_v088_signal,
    f44cds_f44_cyclical_distress_signature_stress_504d_xclog_base_v089_signal,
    f44cds_f44_cyclical_distress_signature_stress_504d_xcm21_base_v090_signal,
    f44cds_f44_cyclical_distress_signature_distressxcollapse_21d_base_v091_signal,
    f44cds_f44_cyclical_distress_signature_distressxstress_21d_base_v092_signal,
    f44cds_f44_cyclical_distress_signature_distress_z_21d_base_v093_signal,
    f44cds_f44_cyclical_distress_signature_collapse_z_21d_base_v094_signal,
    f44cds_f44_cyclical_distress_signature_stress_z_21d_base_v095_signal,
    f44cds_f44_cyclical_distress_signature_distress_ema_21d_base_v096_signal,
    f44cds_f44_cyclical_distress_signature_collapse_ema_21d_base_v097_signal,
    f44cds_f44_cyclical_distress_signature_stress_ema_21d_base_v098_signal,
    f44cds_f44_cyclical_distress_signature_distress_sq_21d_base_v099_signal,
    f44cds_f44_cyclical_distress_signature_collapsexstress_21d_base_v100_signal,
    f44cds_f44_cyclical_distress_signature_distressxcollapse_42d_base_v101_signal,
    f44cds_f44_cyclical_distress_signature_distressxstress_42d_base_v102_signal,
    f44cds_f44_cyclical_distress_signature_distress_z_42d_base_v103_signal,
    f44cds_f44_cyclical_distress_signature_collapse_z_42d_base_v104_signal,
    f44cds_f44_cyclical_distress_signature_stress_z_42d_base_v105_signal,
    f44cds_f44_cyclical_distress_signature_distress_ema_42d_base_v106_signal,
    f44cds_f44_cyclical_distress_signature_collapse_ema_42d_base_v107_signal,
    f44cds_f44_cyclical_distress_signature_stress_ema_42d_base_v108_signal,
    f44cds_f44_cyclical_distress_signature_distress_sq_42d_base_v109_signal,
    f44cds_f44_cyclical_distress_signature_collapsexstress_42d_base_v110_signal,
    f44cds_f44_cyclical_distress_signature_distressxcollapse_63d_base_v111_signal,
    f44cds_f44_cyclical_distress_signature_distressxstress_63d_base_v112_signal,
    f44cds_f44_cyclical_distress_signature_distress_z_63d_base_v113_signal,
    f44cds_f44_cyclical_distress_signature_collapse_z_63d_base_v114_signal,
    f44cds_f44_cyclical_distress_signature_stress_z_63d_base_v115_signal,
    f44cds_f44_cyclical_distress_signature_distress_ema_63d_base_v116_signal,
    f44cds_f44_cyclical_distress_signature_collapse_ema_63d_base_v117_signal,
    f44cds_f44_cyclical_distress_signature_stress_ema_63d_base_v118_signal,
    f44cds_f44_cyclical_distress_signature_distress_sq_63d_base_v119_signal,
    f44cds_f44_cyclical_distress_signature_collapsexstress_63d_base_v120_signal,
    f44cds_f44_cyclical_distress_signature_distressxcollapse_126d_base_v121_signal,
    f44cds_f44_cyclical_distress_signature_distressxstress_126d_base_v122_signal,
    f44cds_f44_cyclical_distress_signature_distress_z_126d_base_v123_signal,
    f44cds_f44_cyclical_distress_signature_collapse_z_126d_base_v124_signal,
    f44cds_f44_cyclical_distress_signature_stress_z_126d_base_v125_signal,
    f44cds_f44_cyclical_distress_signature_distress_ema_126d_base_v126_signal,
    f44cds_f44_cyclical_distress_signature_collapse_ema_126d_base_v127_signal,
    f44cds_f44_cyclical_distress_signature_stress_ema_126d_base_v128_signal,
    f44cds_f44_cyclical_distress_signature_distress_sq_126d_base_v129_signal,
    f44cds_f44_cyclical_distress_signature_collapsexstress_126d_base_v130_signal,
    f44cds_f44_cyclical_distress_signature_distressxcollapse_252d_base_v131_signal,
    f44cds_f44_cyclical_distress_signature_distressxstress_252d_base_v132_signal,
    f44cds_f44_cyclical_distress_signature_distress_z_252d_base_v133_signal,
    f44cds_f44_cyclical_distress_signature_collapse_z_252d_base_v134_signal,
    f44cds_f44_cyclical_distress_signature_stress_z_252d_base_v135_signal,
    f44cds_f44_cyclical_distress_signature_distress_ema_252d_base_v136_signal,
    f44cds_f44_cyclical_distress_signature_collapse_ema_252d_base_v137_signal,
    f44cds_f44_cyclical_distress_signature_stress_ema_252d_base_v138_signal,
    f44cds_f44_cyclical_distress_signature_distress_sq_252d_base_v139_signal,
    f44cds_f44_cyclical_distress_signature_collapsexstress_252d_base_v140_signal,
    f44cds_f44_cyclical_distress_signature_distress_long_10d_base_v141_signal,
    f44cds_f44_cyclical_distress_signature_collapse_long_10d_base_v142_signal,
    f44cds_f44_cyclical_distress_signature_stress_long_10d_base_v143_signal,
    f44cds_f44_cyclical_distress_signature_distress_long_42d_base_v144_signal,
    f44cds_f44_cyclical_distress_signature_collapse_long_42d_base_v145_signal,
    f44cds_f44_cyclical_distress_signature_stress_long_42d_base_v146_signal,
    f44cds_f44_cyclical_distress_signature_distress_long_189d_base_v147_signal,
    f44cds_f44_cyclical_distress_signature_collapse_long_189d_base_v148_signal,
    f44cds_f44_cyclical_distress_signature_stress_long_189d_base_v149_signal,
    f44cds_f44_cyclical_distress_signature_distress_long_378d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F44_CYCLICAL_DISTRESS_SIGNATURE_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ('_f44_distress_proxy', '_f44_collapse_risk', '_f44_cyclical_stress')
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
    print(f"OK f44_cyclical_distress_signature_base_076_150_claude: {n_features} features pass")
