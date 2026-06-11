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
def _f42_evebitda_dynamics(evebitda, w):
    base = _mean(evebitda, max(2, w // 4))
    return base - base.shift(w)


def _f42_premium_proxy(evebitda, ebitdamargin, w):
    margin_z = _z(ebitdamargin, w)
    return evebitda * margin_z


def _f42_consolidation_signal(ev, ebitda, revenue, w):
    ev_per_rev = ev / revenue.replace(0, np.nan)
    eb_per_rev = ebitda / revenue.replace(0, np.nan)
    return ev_per_rev.rolling(w, min_periods=max(1, w // 2)).mean() - eb_per_rev.rolling(w, min_periods=max(1, w // 2)).mean()

# v076: premproxcum_21d
def f42mcp_f42_medtech_consolidation_premium_premproxcum_21d_base_v076_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 21).rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v077: premproxcum_63d
def f42mcp_f42_medtech_consolidation_premium_premproxcum_63d_base_v077_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 63).rolling(252, min_periods=84).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v078: premproxcum_252d
def f42mcp_f42_medtech_consolidation_premium_premproxcum_252d_base_v078_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 252).rolling(504, min_periods=168).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v079: consolcum_21d
def f42mcp_f42_medtech_consolidation_premium_consolcum_21d_base_v079_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 21).rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v080: consolcum_63d
def f42mcp_f42_medtech_consolidation_premium_consolcum_63d_base_v080_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 63).rolling(252, min_periods=84).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v081: consolcum_252d
def f42mcp_f42_medtech_consolidation_premium_consolcum_252d_base_v081_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 252).rolling(504, min_periods=168).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v082: evdynqr_21d
def f42mcp_f42_medtech_consolidation_premium_evdynqr_21d_base_v082_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 21).rolling(252, min_periods=84).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v083: evdynqr_63d
def f42mcp_f42_medtech_consolidation_premium_evdynqr_63d_base_v083_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 63).rolling(252, min_periods=84).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v084: evdynqr_252d
def f42mcp_f42_medtech_consolidation_premium_evdynqr_252d_base_v084_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 252).rolling(504, min_periods=168).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v085: premproxqr_21d
def f42mcp_f42_medtech_consolidation_premium_premproxqr_21d_base_v085_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 21).rolling(252, min_periods=84).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v086: premproxqr_63d
def f42mcp_f42_medtech_consolidation_premium_premproxqr_63d_base_v086_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 63).rolling(252, min_periods=84).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v087: premproxqr_252d
def f42mcp_f42_medtech_consolidation_premium_premproxqr_252d_base_v087_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 252).rolling(504, min_periods=168).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v088: consolqr_21d
def f42mcp_f42_medtech_consolidation_premium_consolqr_21d_base_v088_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 21).rolling(252, min_periods=84).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v089: consolqr_63d
def f42mcp_f42_medtech_consolidation_premium_consolqr_63d_base_v089_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 63).rolling(252, min_periods=84).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v090: consolqr_252d
def f42mcp_f42_medtech_consolidation_premium_consolqr_252d_base_v090_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 252).rolling(504, min_periods=168).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v091: evdyndiff_21_21
def f42mcp_f42_medtech_consolidation_premium_evdyndiff_21_21_base_v091_signal(evebitda, closeadj):
    result = (_f42_evebitda_dynamics(evebitda, 21) - _f42_evebitda_dynamics(evebitda, 21).shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v092: evdyndiff_63_63
def f42mcp_f42_medtech_consolidation_premium_evdyndiff_63_63_base_v092_signal(evebitda, closeadj):
    result = (_f42_evebitda_dynamics(evebitda, 63) - _f42_evebitda_dynamics(evebitda, 63).shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v093: evdyndiff_252_63
def f42mcp_f42_medtech_consolidation_premium_evdyndiff_252_63_base_v093_signal(evebitda, closeadj):
    result = (_f42_evebitda_dynamics(evebitda, 252) - _f42_evebitda_dynamics(evebitda, 252).shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v094: premproxdiff_21_21
def f42mcp_f42_medtech_consolidation_premium_premproxdiff_21_21_base_v094_signal(evebitda, ebitdamargin, closeadj):
    result = (_f42_premium_proxy(evebitda, ebitdamargin, 21) - _f42_premium_proxy(evebitda, ebitdamargin, 21).shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v095: premproxdiff_63_63
def f42mcp_f42_medtech_consolidation_premium_premproxdiff_63_63_base_v095_signal(evebitda, ebitdamargin, closeadj):
    result = (_f42_premium_proxy(evebitda, ebitdamargin, 63) - _f42_premium_proxy(evebitda, ebitdamargin, 63).shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v096: premproxdiff_252_63
def f42mcp_f42_medtech_consolidation_premium_premproxdiff_252_63_base_v096_signal(evebitda, ebitdamargin, closeadj):
    result = (_f42_premium_proxy(evebitda, ebitdamargin, 252) - _f42_premium_proxy(evebitda, ebitdamargin, 252).shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v097: consoldiff_21_21
def f42mcp_f42_medtech_consolidation_premium_consoldiff_21_21_base_v097_signal(ev, ebitda, revenue, closeadj):
    result = (_f42_consolidation_signal(ev, ebitda, revenue, 21) - _f42_consolidation_signal(ev, ebitda, revenue, 21).shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v098: consoldiff_63_63
def f42mcp_f42_medtech_consolidation_premium_consoldiff_63_63_base_v098_signal(ev, ebitda, revenue, closeadj):
    result = (_f42_consolidation_signal(ev, ebitda, revenue, 63) - _f42_consolidation_signal(ev, ebitda, revenue, 63).shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v099: consoldiff_252_63
def f42mcp_f42_medtech_consolidation_premium_consoldiff_252_63_base_v099_signal(ev, ebitda, revenue, closeadj):
    result = (_f42_consolidation_signal(ev, ebitda, revenue, 252) - _f42_consolidation_signal(ev, ebitda, revenue, 252).shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v100: evdynxmargin_21d
def f42mcp_f42_medtech_consolidation_premium_evdynxmargin_21d_base_v100_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 21) * _mean(ebitdamargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v101: evdynxmargin_63d
def f42mcp_f42_medtech_consolidation_premium_evdynxmargin_63d_base_v101_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 63) * _mean(ebitdamargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v102: evdynxmargin_252d
def f42mcp_f42_medtech_consolidation_premium_evdynxmargin_252d_base_v102_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 252) * _mean(ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v103: premproxsignabs_21d
def f42mcp_f42_medtech_consolidation_premium_premproxsignabs_21d_base_v103_signal(evebitda, ebitdamargin, closeadj):
    result = np.sign(_f42_premium_proxy(evebitda, ebitdamargin, 21)) * _f42_evebitda_dynamics(evebitda, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v104: premproxsignabs_63d
def f42mcp_f42_medtech_consolidation_premium_premproxsignabs_63d_base_v104_signal(evebitda, ebitdamargin, closeadj):
    result = np.sign(_f42_premium_proxy(evebitda, ebitdamargin, 63)) * _f42_evebitda_dynamics(evebitda, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v105: premproxsignabs_252d
def f42mcp_f42_medtech_consolidation_premium_premproxsignabs_252d_base_v105_signal(evebitda, ebitdamargin, closeadj):
    result = np.sign(_f42_premium_proxy(evebitda, ebitdamargin, 252)) * _f42_evebitda_dynamics(evebitda, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v106: consolsignabs_21d
def f42mcp_f42_medtech_consolidation_premium_consolsignabs_21d_base_v106_signal(evebitda, ev, ebitda, revenue, closeadj):
    result = np.sign(_f42_consolidation_signal(ev, ebitda, revenue, 21)) * _f42_evebitda_dynamics(evebitda, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v107: consolsignabs_63d
def f42mcp_f42_medtech_consolidation_premium_consolsignabs_63d_base_v107_signal(evebitda, ev, ebitda, revenue, closeadj):
    result = np.sign(_f42_consolidation_signal(ev, ebitda, revenue, 63)) * _f42_evebitda_dynamics(evebitda, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v108: consolsignabs_252d
def f42mcp_f42_medtech_consolidation_premium_consolsignabs_252d_base_v108_signal(evebitda, ev, ebitda, revenue, closeadj):
    result = np.sign(_f42_consolidation_signal(ev, ebitda, revenue, 252)) * _f42_evebitda_dynamics(evebitda, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v109: evdynlog_21d
def f42mcp_f42_medtech_consolidation_premium_evdynlog_21d_base_v109_signal(evebitda, closeadj):
    result = np.sign(_f42_evebitda_dynamics(evebitda, 21)) * np.log1p(_f42_evebitda_dynamics(evebitda, 21).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v110: evdynlog_63d
def f42mcp_f42_medtech_consolidation_premium_evdynlog_63d_base_v110_signal(evebitda, closeadj):
    result = np.sign(_f42_evebitda_dynamics(evebitda, 63)) * np.log1p(_f42_evebitda_dynamics(evebitda, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v111: evdynlog_252d
def f42mcp_f42_medtech_consolidation_premium_evdynlog_252d_base_v111_signal(evebitda, closeadj):
    result = np.sign(_f42_evebitda_dynamics(evebitda, 252)) * np.log1p(_f42_evebitda_dynamics(evebitda, 252).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v112: premproxlog_21d
def f42mcp_f42_medtech_consolidation_premium_premproxlog_21d_base_v112_signal(evebitda, ebitdamargin, closeadj):
    result = np.sign(_f42_premium_proxy(evebitda, ebitdamargin, 21)) * np.log1p(_f42_premium_proxy(evebitda, ebitdamargin, 21).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v113: premproxlog_63d
def f42mcp_f42_medtech_consolidation_premium_premproxlog_63d_base_v113_signal(evebitda, ebitdamargin, closeadj):
    result = np.sign(_f42_premium_proxy(evebitda, ebitdamargin, 63)) * np.log1p(_f42_premium_proxy(evebitda, ebitdamargin, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v114: premproxlog_252d
def f42mcp_f42_medtech_consolidation_premium_premproxlog_252d_base_v114_signal(evebitda, ebitdamargin, closeadj):
    result = np.sign(_f42_premium_proxy(evebitda, ebitdamargin, 252)) * np.log1p(_f42_premium_proxy(evebitda, ebitdamargin, 252).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v115: consollog_21d
def f42mcp_f42_medtech_consolidation_premium_consollog_21d_base_v115_signal(ev, ebitda, revenue, closeadj):
    result = np.sign(_f42_consolidation_signal(ev, ebitda, revenue, 21)) * np.log1p(_f42_consolidation_signal(ev, ebitda, revenue, 21).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v116: consollog_63d
def f42mcp_f42_medtech_consolidation_premium_consollog_63d_base_v116_signal(ev, ebitda, revenue, closeadj):
    result = np.sign(_f42_consolidation_signal(ev, ebitda, revenue, 63)) * np.log1p(_f42_consolidation_signal(ev, ebitda, revenue, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v117: consollog_252d
def f42mcp_f42_medtech_consolidation_premium_consollog_252d_base_v117_signal(ev, ebitda, revenue, closeadj):
    result = np.sign(_f42_consolidation_signal(ev, ebitda, revenue, 252)) * np.log1p(_f42_consolidation_signal(ev, ebitda, revenue, 252).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v118: evdynx_21x63
def f42mcp_f42_medtech_consolidation_premium_evdynx_21x63_base_v118_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 21) * _f42_evebitda_dynamics(evebitda, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v119: evdynx_21x252
def f42mcp_f42_medtech_consolidation_premium_evdynx_21x252_base_v119_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 21) * _f42_evebitda_dynamics(evebitda, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v120: evdynx_63x252
def f42mcp_f42_medtech_consolidation_premium_evdynx_63x252_base_v120_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 63) * _f42_evebitda_dynamics(evebitda, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v121: evdynx_63x504
def f42mcp_f42_medtech_consolidation_premium_evdynx_63x504_base_v121_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 63) * _f42_evebitda_dynamics(evebitda, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v122: evdynx_126x504
def f42mcp_f42_medtech_consolidation_premium_evdynx_126x504_base_v122_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 126) * _f42_evebitda_dynamics(evebitda, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v123: premproxx_21x63
def f42mcp_f42_medtech_consolidation_premium_premproxx_21x63_base_v123_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 21) * _f42_premium_proxy(evebitda, ebitdamargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v124: premproxx_21x252
def f42mcp_f42_medtech_consolidation_premium_premproxx_21x252_base_v124_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 21) * _f42_premium_proxy(evebitda, ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v125: premproxx_63x252
def f42mcp_f42_medtech_consolidation_premium_premproxx_63x252_base_v125_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 63) * _f42_premium_proxy(evebitda, ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v126: premproxx_63x504
def f42mcp_f42_medtech_consolidation_premium_premproxx_63x504_base_v126_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 63) * _f42_premium_proxy(evebitda, ebitdamargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v127: premproxx_126x504
def f42mcp_f42_medtech_consolidation_premium_premproxx_126x504_base_v127_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 126) * _f42_premium_proxy(evebitda, ebitdamargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v128: consolx_21x63
def f42mcp_f42_medtech_consolidation_premium_consolx_21x63_base_v128_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 21) * _f42_consolidation_signal(ev, ebitda, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v129: consolx_21x252
def f42mcp_f42_medtech_consolidation_premium_consolx_21x252_base_v129_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 21) * _f42_consolidation_signal(ev, ebitda, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v130: consolx_63x252
def f42mcp_f42_medtech_consolidation_premium_consolx_63x252_base_v130_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 63) * _f42_consolidation_signal(ev, ebitda, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v131: consolx_63x504
def f42mcp_f42_medtech_consolidation_premium_consolx_63x504_base_v131_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 63) * _f42_consolidation_signal(ev, ebitda, revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v132: consolx_126x504
def f42mcp_f42_medtech_consolidation_premium_consolx_126x504_base_v132_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 126) * _f42_consolidation_signal(ev, ebitda, revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v133: evdyntri_2163252
def f42mcp_f42_medtech_consolidation_premium_evdyntri_2163252_base_v133_signal(evebitda, closeadj):
    result = (_f42_evebitda_dynamics(evebitda, 21) + _f42_evebitda_dynamics(evebitda, 63) + _f42_evebitda_dynamics(evebitda, 252)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v134: evdyntri_63126252
def f42mcp_f42_medtech_consolidation_premium_evdyntri_63126252_base_v134_signal(evebitda, closeadj):
    result = (_f42_evebitda_dynamics(evebitda, 63) + _f42_evebitda_dynamics(evebitda, 126) + _f42_evebitda_dynamics(evebitda, 252)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v135: evdyntri_126252504
def f42mcp_f42_medtech_consolidation_premium_evdyntri_126252504_base_v135_signal(evebitda, closeadj):
    result = (_f42_evebitda_dynamics(evebitda, 126) + _f42_evebitda_dynamics(evebitda, 252) + _f42_evebitda_dynamics(evebitda, 504)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v136: premproxtri_2163252
def f42mcp_f42_medtech_consolidation_premium_premproxtri_2163252_base_v136_signal(evebitda, ebitdamargin, closeadj):
    result = (_f42_premium_proxy(evebitda, ebitdamargin, 21) + _f42_premium_proxy(evebitda, ebitdamargin, 63) + _f42_premium_proxy(evebitda, ebitdamargin, 252)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v137: premproxtri_63126252
def f42mcp_f42_medtech_consolidation_premium_premproxtri_63126252_base_v137_signal(evebitda, ebitdamargin, closeadj):
    result = (_f42_premium_proxy(evebitda, ebitdamargin, 63) + _f42_premium_proxy(evebitda, ebitdamargin, 126) + _f42_premium_proxy(evebitda, ebitdamargin, 252)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v138: premproxtri_126252504
def f42mcp_f42_medtech_consolidation_premium_premproxtri_126252504_base_v138_signal(evebitda, ebitdamargin, closeadj):
    result = (_f42_premium_proxy(evebitda, ebitdamargin, 126) + _f42_premium_proxy(evebitda, ebitdamargin, 252) + _f42_premium_proxy(evebitda, ebitdamargin, 504)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v139: consoltri_2163252
def f42mcp_f42_medtech_consolidation_premium_consoltri_2163252_base_v139_signal(ev, ebitda, revenue, closeadj):
    result = (_f42_consolidation_signal(ev, ebitda, revenue, 21) + _f42_consolidation_signal(ev, ebitda, revenue, 63) + _f42_consolidation_signal(ev, ebitda, revenue, 252)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v140: consoltri_63126252
def f42mcp_f42_medtech_consolidation_premium_consoltri_63126252_base_v140_signal(ev, ebitda, revenue, closeadj):
    result = (_f42_consolidation_signal(ev, ebitda, revenue, 63) + _f42_consolidation_signal(ev, ebitda, revenue, 126) + _f42_consolidation_signal(ev, ebitda, revenue, 252)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v141: consoltri_126252504
def f42mcp_f42_medtech_consolidation_premium_consoltri_126252504_base_v141_signal(ev, ebitda, revenue, closeadj):
    result = (_f42_consolidation_signal(ev, ebitda, revenue, 126) + _f42_consolidation_signal(ev, ebitda, revenue, 252) + _f42_consolidation_signal(ev, ebitda, revenue, 504)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v142: evdynxmarginema_21d
def f42mcp_f42_medtech_consolidation_premium_evdynxmarginema_21d_base_v142_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 21) * ebitdamargin.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v143: evdynxmarginema_63d
def f42mcp_f42_medtech_consolidation_premium_evdynxmarginema_63d_base_v143_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 63) * ebitdamargin.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v144: evdynxmarginema_252d
def f42mcp_f42_medtech_consolidation_premium_evdynxmarginema_252d_base_v144_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 252) * ebitdamargin.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v145: consol_5d_alt
def f42mcp_f42_medtech_consolidation_premium_consol_5d_alt_base_v145_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 5) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v146: consol_10d_alt
def f42mcp_f42_medtech_consolidation_premium_consol_10d_alt_base_v146_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 10) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v147: consol_42d_alt
def f42mcp_f42_medtech_consolidation_premium_consol_42d_alt_base_v147_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 42) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v148: consol_189d_alt
def f42mcp_f42_medtech_consolidation_premium_consol_189d_alt_base_v148_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 189) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v149: consol_378d_alt
def f42mcp_f42_medtech_consolidation_premium_consol_378d_alt_base_v149_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 378) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v150: evdynstrong_21d
def f42mcp_f42_medtech_consolidation_premium_evdynstrong_21d_base_v150_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 21).clip(lower=0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f42mcp_f42_medtech_consolidation_premium_premproxcum_21d_base_v076_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxcum_63d_base_v077_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxcum_252d_base_v078_signal,
    f42mcp_f42_medtech_consolidation_premium_consolcum_21d_base_v079_signal,
    f42mcp_f42_medtech_consolidation_premium_consolcum_63d_base_v080_signal,
    f42mcp_f42_medtech_consolidation_premium_consolcum_252d_base_v081_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynqr_21d_base_v082_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynqr_63d_base_v083_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynqr_252d_base_v084_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxqr_21d_base_v085_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxqr_63d_base_v086_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxqr_252d_base_v087_signal,
    f42mcp_f42_medtech_consolidation_premium_consolqr_21d_base_v088_signal,
    f42mcp_f42_medtech_consolidation_premium_consolqr_63d_base_v089_signal,
    f42mcp_f42_medtech_consolidation_premium_consolqr_252d_base_v090_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyndiff_21_21_base_v091_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyndiff_63_63_base_v092_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyndiff_252_63_base_v093_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxdiff_21_21_base_v094_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxdiff_63_63_base_v095_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxdiff_252_63_base_v096_signal,
    f42mcp_f42_medtech_consolidation_premium_consoldiff_21_21_base_v097_signal,
    f42mcp_f42_medtech_consolidation_premium_consoldiff_63_63_base_v098_signal,
    f42mcp_f42_medtech_consolidation_premium_consoldiff_252_63_base_v099_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxmargin_21d_base_v100_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxmargin_63d_base_v101_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxmargin_252d_base_v102_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxsignabs_21d_base_v103_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxsignabs_63d_base_v104_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxsignabs_252d_base_v105_signal,
    f42mcp_f42_medtech_consolidation_premium_consolsignabs_21d_base_v106_signal,
    f42mcp_f42_medtech_consolidation_premium_consolsignabs_63d_base_v107_signal,
    f42mcp_f42_medtech_consolidation_premium_consolsignabs_252d_base_v108_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynlog_21d_base_v109_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynlog_63d_base_v110_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynlog_252d_base_v111_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxlog_21d_base_v112_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxlog_63d_base_v113_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxlog_252d_base_v114_signal,
    f42mcp_f42_medtech_consolidation_premium_consollog_21d_base_v115_signal,
    f42mcp_f42_medtech_consolidation_premium_consollog_63d_base_v116_signal,
    f42mcp_f42_medtech_consolidation_premium_consollog_252d_base_v117_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynx_21x63_base_v118_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynx_21x252_base_v119_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynx_63x252_base_v120_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynx_63x504_base_v121_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynx_126x504_base_v122_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxx_21x63_base_v123_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxx_21x252_base_v124_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxx_63x252_base_v125_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxx_63x504_base_v126_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxx_126x504_base_v127_signal,
    f42mcp_f42_medtech_consolidation_premium_consolx_21x63_base_v128_signal,
    f42mcp_f42_medtech_consolidation_premium_consolx_21x252_base_v129_signal,
    f42mcp_f42_medtech_consolidation_premium_consolx_63x252_base_v130_signal,
    f42mcp_f42_medtech_consolidation_premium_consolx_63x504_base_v131_signal,
    f42mcp_f42_medtech_consolidation_premium_consolx_126x504_base_v132_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyntri_2163252_base_v133_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyntri_63126252_base_v134_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyntri_126252504_base_v135_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxtri_2163252_base_v136_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxtri_63126252_base_v137_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxtri_126252504_base_v138_signal,
    f42mcp_f42_medtech_consolidation_premium_consoltri_2163252_base_v139_signal,
    f42mcp_f42_medtech_consolidation_premium_consoltri_63126252_base_v140_signal,
    f42mcp_f42_medtech_consolidation_premium_consoltri_126252504_base_v141_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxmarginema_21d_base_v142_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxmarginema_63d_base_v143_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxmarginema_252d_base_v144_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_5d_alt_base_v145_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_10d_alt_base_v146_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_42d_alt_base_v147_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_189d_alt_base_v148_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_378d_alt_base_v149_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynstrong_21d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F42_MEDTECH_CONSOLIDATION_PREMIUM_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    debt = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    cashneq = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    ebitda = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    ev = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    evebitda = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")

    cols = {
        "closeadj": closeadj,
        "ebitda": ebitda,
        "ebitdamargin": ebitdamargin,
        "ev": ev,
        "evebitda": evebitda,
        "revenue": revenue,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f42_evebitda_dynamics', '_f42_premium_proxy', '_f42_consolidation_signal',)
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
    print(f"OK f42_medtech_consolidation_premium_base_076_150_claude: {n_features} features pass")
