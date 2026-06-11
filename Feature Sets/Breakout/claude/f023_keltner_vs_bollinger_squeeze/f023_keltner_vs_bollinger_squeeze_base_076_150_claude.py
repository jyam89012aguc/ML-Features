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
def _f023_keltner(high, low, close, w):
    tr = (high - low).abs()
    atr = tr.rolling(w, min_periods=max(1, w // 2)).mean()
    m = close.rolling(w, min_periods=max(1, w // 2)).mean()
    upper = m + 1.5 * atr
    lower = m - 1.5 * atr
    return (upper - lower) / m.replace(0, np.nan).abs()


def _f023_bb_kc_squeeze(close, high, low, w):
    sd = close.rolling(w, min_periods=max(1, w // 2)).std()
    m = close.rolling(w, min_periods=max(1, w // 2)).mean()
    bb_w = (4.0 * sd) / m.replace(0, np.nan).abs()
    tr = (high - low).abs()
    atr = tr.rolling(w, min_periods=max(1, w // 2)).mean()
    kc_w = (3.0 * atr) / m.replace(0, np.nan).abs()
    return bb_w - kc_w


def _f023_ttm_squeeze(close, high, low, w):
    sd = close.rolling(w, min_periods=max(1, w // 2)).std()
    m = close.rolling(w, min_periods=max(1, w // 2)).mean()
    bb_w = (4.0 * sd) / m.replace(0, np.nan).abs()
    tr = (high - low).abs()
    atr = tr.rolling(w, min_periods=max(1, w // 2)).mean()
    kc_w = (3.0 * atr) / m.replace(0, np.nan).abs()
    diff = (bb_w - kc_w)
    return diff * close


def f023kbs_f023_keltner_vs_bollinger_squeeze_p2_126d_m63_base_v076_signal(closeadj, high, low):
    result = _mean(_f023_bb_kc_squeeze(closeadj, high, low, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p2_126d_s63_base_v077_signal(closeadj, high, low):
    result = _std(_f023_bb_kc_squeeze(closeadj, high, low, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p2_126d_z126_base_v078_signal(closeadj, high, low):
    result = _z(_f023_bb_kc_squeeze(closeadj, high, low, 126), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p2_126d_d63_base_v079_signal(closeadj, high, low):
    result = _f023_bb_kc_squeeze(closeadj, high, low, 126).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p2_126d_ed_base_v080_signal(closeadj, high, low):
    result = ((_f023_bb_kc_squeeze(closeadj, high, low, 126)).ewm(span=21, adjust=False).mean() - (_f023_bb_kc_squeeze(closeadj, high, low, 126)).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p2_189d_m63_base_v081_signal(closeadj, high, low):
    result = _mean(_f023_bb_kc_squeeze(closeadj, high, low, 189), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p2_189d_s63_base_v082_signal(closeadj, high, low):
    result = _std(_f023_bb_kc_squeeze(closeadj, high, low, 189), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p2_189d_z126_base_v083_signal(closeadj, high, low):
    result = _z(_f023_bb_kc_squeeze(closeadj, high, low, 189), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p2_189d_d63_base_v084_signal(closeadj, high, low):
    result = _f023_bb_kc_squeeze(closeadj, high, low, 189).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p2_189d_ed_base_v085_signal(closeadj, high, low):
    result = ((_f023_bb_kc_squeeze(closeadj, high, low, 189)).ewm(span=21, adjust=False).mean() - (_f023_bb_kc_squeeze(closeadj, high, low, 189)).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p2_252d_m63_base_v086_signal(closeadj, high, low):
    result = _mean(_f023_bb_kc_squeeze(closeadj, high, low, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p2_252d_s63_base_v087_signal(closeadj, high, low):
    result = _std(_f023_bb_kc_squeeze(closeadj, high, low, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p2_252d_z126_base_v088_signal(closeadj, high, low):
    result = _z(_f023_bb_kc_squeeze(closeadj, high, low, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p2_252d_d63_base_v089_signal(closeadj, high, low):
    result = _f023_bb_kc_squeeze(closeadj, high, low, 252).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p2_252d_ed_base_v090_signal(closeadj, high, low):
    result = ((_f023_bb_kc_squeeze(closeadj, high, low, 252)).ewm(span=21, adjust=False).mean() - (_f023_bb_kc_squeeze(closeadj, high, low, 252)).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p2_378d_m63_base_v091_signal(closeadj, high, low):
    result = _mean(_f023_bb_kc_squeeze(closeadj, high, low, 378), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p2_378d_s63_base_v092_signal(closeadj, high, low):
    result = _std(_f023_bb_kc_squeeze(closeadj, high, low, 378), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p2_378d_z126_base_v093_signal(closeadj, high, low):
    result = _z(_f023_bb_kc_squeeze(closeadj, high, low, 378), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p2_378d_d63_base_v094_signal(closeadj, high, low):
    result = _f023_bb_kc_squeeze(closeadj, high, low, 378).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p2_378d_ed_base_v095_signal(closeadj, high, low):
    result = ((_f023_bb_kc_squeeze(closeadj, high, low, 378)).ewm(span=21, adjust=False).mean() - (_f023_bb_kc_squeeze(closeadj, high, low, 378)).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p2_504d_m63_base_v096_signal(closeadj, high, low):
    result = _mean(_f023_bb_kc_squeeze(closeadj, high, low, 504), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p2_504d_s63_base_v097_signal(closeadj, high, low):
    result = _std(_f023_bb_kc_squeeze(closeadj, high, low, 504), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p2_504d_z126_base_v098_signal(closeadj, high, low):
    result = _z(_f023_bb_kc_squeeze(closeadj, high, low, 504), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p2_504d_d63_base_v099_signal(closeadj, high, low):
    result = _f023_bb_kc_squeeze(closeadj, high, low, 504).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p2_504d_ed_base_v100_signal(closeadj, high, low):
    result = ((_f023_bb_kc_squeeze(closeadj, high, low, 504)).ewm(span=21, adjust=False).mean() - (_f023_bb_kc_squeeze(closeadj, high, low, 504)).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_5d_s21_base_v101_signal(closeadj, high, low):
    result = _std(_f023_ttm_squeeze(closeadj, high, low, 5), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_5d_e21_base_v102_signal(closeadj, high, low):
    result = (_f023_ttm_squeeze(closeadj, high, low, 5)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_5d_smadf_base_v103_signal(closeadj, high, low):
    result = (_f023_ttm_squeeze(closeadj, high, low, 5) - _mean(_f023_ttm_squeeze(closeadj, high, low, 5), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_5d_smarat_base_v104_signal(closeadj, high, low):
    result = _safe_div(_f023_ttm_squeeze(closeadj, high, low, 5), _mean(_f023_ttm_squeeze(closeadj, high, low, 5), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_5d_zsq_base_v105_signal(closeadj, high, low):
    result = _z(_f023_ttm_squeeze(closeadj, high, low, 5), 252) * _z(_f023_ttm_squeeze(closeadj, high, low, 5), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_10d_s21_base_v106_signal(closeadj, high, low):
    result = _std(_f023_ttm_squeeze(closeadj, high, low, 10), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_10d_e21_base_v107_signal(closeadj, high, low):
    result = (_f023_ttm_squeeze(closeadj, high, low, 10)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_10d_smadf_base_v108_signal(closeadj, high, low):
    result = (_f023_ttm_squeeze(closeadj, high, low, 10) - _mean(_f023_ttm_squeeze(closeadj, high, low, 10), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_10d_smarat_base_v109_signal(closeadj, high, low):
    result = _safe_div(_f023_ttm_squeeze(closeadj, high, low, 10), _mean(_f023_ttm_squeeze(closeadj, high, low, 10), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_10d_zsq_base_v110_signal(closeadj, high, low):
    result = _z(_f023_ttm_squeeze(closeadj, high, low, 10), 252) * _z(_f023_ttm_squeeze(closeadj, high, low, 10), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_21d_s21_base_v111_signal(closeadj, high, low):
    result = _std(_f023_ttm_squeeze(closeadj, high, low, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_21d_e21_base_v112_signal(closeadj, high, low):
    result = (_f023_ttm_squeeze(closeadj, high, low, 21)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_21d_smadf_base_v113_signal(closeadj, high, low):
    result = (_f023_ttm_squeeze(closeadj, high, low, 21) - _mean(_f023_ttm_squeeze(closeadj, high, low, 21), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_21d_smarat_base_v114_signal(closeadj, high, low):
    result = _safe_div(_f023_ttm_squeeze(closeadj, high, low, 21), _mean(_f023_ttm_squeeze(closeadj, high, low, 21), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_21d_zsq_base_v115_signal(closeadj, high, low):
    result = _z(_f023_ttm_squeeze(closeadj, high, low, 21), 252) * _z(_f023_ttm_squeeze(closeadj, high, low, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_42d_s21_base_v116_signal(closeadj, high, low):
    result = _std(_f023_ttm_squeeze(closeadj, high, low, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_42d_e21_base_v117_signal(closeadj, high, low):
    result = (_f023_ttm_squeeze(closeadj, high, low, 42)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_42d_smadf_base_v118_signal(closeadj, high, low):
    result = (_f023_ttm_squeeze(closeadj, high, low, 42) - _mean(_f023_ttm_squeeze(closeadj, high, low, 42), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_42d_smarat_base_v119_signal(closeadj, high, low):
    result = _safe_div(_f023_ttm_squeeze(closeadj, high, low, 42), _mean(_f023_ttm_squeeze(closeadj, high, low, 42), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_42d_zsq_base_v120_signal(closeadj, high, low):
    result = _z(_f023_ttm_squeeze(closeadj, high, low, 42), 252) * _z(_f023_ttm_squeeze(closeadj, high, low, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_63d_s21_base_v121_signal(closeadj, high, low):
    result = _std(_f023_ttm_squeeze(closeadj, high, low, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_63d_e21_base_v122_signal(closeadj, high, low):
    result = (_f023_ttm_squeeze(closeadj, high, low, 63)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_63d_smadf_base_v123_signal(closeadj, high, low):
    result = (_f023_ttm_squeeze(closeadj, high, low, 63) - _mean(_f023_ttm_squeeze(closeadj, high, low, 63), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_63d_smarat_base_v124_signal(closeadj, high, low):
    result = _safe_div(_f023_ttm_squeeze(closeadj, high, low, 63), _mean(_f023_ttm_squeeze(closeadj, high, low, 63), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_63d_zsq_base_v125_signal(closeadj, high, low):
    result = _z(_f023_ttm_squeeze(closeadj, high, low, 63), 252) * _z(_f023_ttm_squeeze(closeadj, high, low, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_126d_s21_base_v126_signal(closeadj, high, low):
    result = _std(_f023_ttm_squeeze(closeadj, high, low, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_126d_e21_base_v127_signal(closeadj, high, low):
    result = (_f023_ttm_squeeze(closeadj, high, low, 126)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_126d_smadf_base_v128_signal(closeadj, high, low):
    result = (_f023_ttm_squeeze(closeadj, high, low, 126) - _mean(_f023_ttm_squeeze(closeadj, high, low, 126), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_126d_smarat_base_v129_signal(closeadj, high, low):
    result = _safe_div(_f023_ttm_squeeze(closeadj, high, low, 126), _mean(_f023_ttm_squeeze(closeadj, high, low, 126), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_126d_zsq_base_v130_signal(closeadj, high, low):
    result = _z(_f023_ttm_squeeze(closeadj, high, low, 126), 252) * _z(_f023_ttm_squeeze(closeadj, high, low, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_189d_s21_base_v131_signal(closeadj, high, low):
    result = _std(_f023_ttm_squeeze(closeadj, high, low, 189), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_189d_e21_base_v132_signal(closeadj, high, low):
    result = (_f023_ttm_squeeze(closeadj, high, low, 189)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_189d_smadf_base_v133_signal(closeadj, high, low):
    result = (_f023_ttm_squeeze(closeadj, high, low, 189) - _mean(_f023_ttm_squeeze(closeadj, high, low, 189), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_189d_smarat_base_v134_signal(closeadj, high, low):
    result = _safe_div(_f023_ttm_squeeze(closeadj, high, low, 189), _mean(_f023_ttm_squeeze(closeadj, high, low, 189), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_189d_zsq_base_v135_signal(closeadj, high, low):
    result = _z(_f023_ttm_squeeze(closeadj, high, low, 189), 252) * _z(_f023_ttm_squeeze(closeadj, high, low, 189), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_252d_s21_base_v136_signal(closeadj, high, low):
    result = _std(_f023_ttm_squeeze(closeadj, high, low, 252), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_252d_e21_base_v137_signal(closeadj, high, low):
    result = (_f023_ttm_squeeze(closeadj, high, low, 252)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_252d_smadf_base_v138_signal(closeadj, high, low):
    result = (_f023_ttm_squeeze(closeadj, high, low, 252) - _mean(_f023_ttm_squeeze(closeadj, high, low, 252), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_252d_smarat_base_v139_signal(closeadj, high, low):
    result = _safe_div(_f023_ttm_squeeze(closeadj, high, low, 252), _mean(_f023_ttm_squeeze(closeadj, high, low, 252), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_252d_zsq_base_v140_signal(closeadj, high, low):
    result = _z(_f023_ttm_squeeze(closeadj, high, low, 252), 252) * _z(_f023_ttm_squeeze(closeadj, high, low, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_378d_s21_base_v141_signal(closeadj, high, low):
    result = _std(_f023_ttm_squeeze(closeadj, high, low, 378), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_378d_e21_base_v142_signal(closeadj, high, low):
    result = (_f023_ttm_squeeze(closeadj, high, low, 378)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_378d_smadf_base_v143_signal(closeadj, high, low):
    result = (_f023_ttm_squeeze(closeadj, high, low, 378) - _mean(_f023_ttm_squeeze(closeadj, high, low, 378), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_378d_smarat_base_v144_signal(closeadj, high, low):
    result = _safe_div(_f023_ttm_squeeze(closeadj, high, low, 378), _mean(_f023_ttm_squeeze(closeadj, high, low, 378), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_378d_zsq_base_v145_signal(closeadj, high, low):
    result = _z(_f023_ttm_squeeze(closeadj, high, low, 378), 252) * _z(_f023_ttm_squeeze(closeadj, high, low, 378), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_504d_s21_base_v146_signal(closeadj, high, low):
    result = _std(_f023_ttm_squeeze(closeadj, high, low, 504), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_504d_e21_base_v147_signal(closeadj, high, low):
    result = (_f023_ttm_squeeze(closeadj, high, low, 504)).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_504d_smadf_base_v148_signal(closeadj, high, low):
    result = (_f023_ttm_squeeze(closeadj, high, low, 504) - _mean(_f023_ttm_squeeze(closeadj, high, low, 504), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_504d_smarat_base_v149_signal(closeadj, high, low):
    result = _safe_div(_f023_ttm_squeeze(closeadj, high, low, 504), _mean(_f023_ttm_squeeze(closeadj, high, low, 504), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f023kbs_f023_keltner_vs_bollinger_squeeze_p3_504d_zsq_base_v150_signal(closeadj, high, low):
    result = _z(_f023_ttm_squeeze(closeadj, high, low, 504), 252) * _z(_f023_ttm_squeeze(closeadj, high, low, 504), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f023kbs_f023_keltner_vs_bollinger_squeeze_p2_126d_m63_base_v076_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p2_126d_s63_base_v077_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p2_126d_z126_base_v078_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p2_126d_d63_base_v079_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p2_126d_ed_base_v080_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p2_189d_m63_base_v081_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p2_189d_s63_base_v082_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p2_189d_z126_base_v083_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p2_189d_d63_base_v084_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p2_189d_ed_base_v085_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p2_252d_m63_base_v086_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p2_252d_s63_base_v087_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p2_252d_z126_base_v088_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p2_252d_d63_base_v089_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p2_252d_ed_base_v090_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p2_378d_m63_base_v091_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p2_378d_s63_base_v092_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p2_378d_z126_base_v093_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p2_378d_d63_base_v094_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p2_378d_ed_base_v095_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p2_504d_m63_base_v096_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p2_504d_s63_base_v097_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p2_504d_z126_base_v098_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p2_504d_d63_base_v099_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p2_504d_ed_base_v100_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_5d_s21_base_v101_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_5d_e21_base_v102_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_5d_smadf_base_v103_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_5d_smarat_base_v104_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_5d_zsq_base_v105_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_10d_s21_base_v106_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_10d_e21_base_v107_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_10d_smadf_base_v108_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_10d_smarat_base_v109_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_10d_zsq_base_v110_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_21d_s21_base_v111_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_21d_e21_base_v112_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_21d_smadf_base_v113_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_21d_smarat_base_v114_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_21d_zsq_base_v115_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_42d_s21_base_v116_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_42d_e21_base_v117_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_42d_smadf_base_v118_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_42d_smarat_base_v119_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_42d_zsq_base_v120_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_63d_s21_base_v121_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_63d_e21_base_v122_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_63d_smadf_base_v123_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_63d_smarat_base_v124_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_63d_zsq_base_v125_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_126d_s21_base_v126_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_126d_e21_base_v127_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_126d_smadf_base_v128_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_126d_smarat_base_v129_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_126d_zsq_base_v130_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_189d_s21_base_v131_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_189d_e21_base_v132_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_189d_smadf_base_v133_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_189d_smarat_base_v134_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_189d_zsq_base_v135_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_252d_s21_base_v136_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_252d_e21_base_v137_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_252d_smadf_base_v138_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_252d_smarat_base_v139_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_252d_zsq_base_v140_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_378d_s21_base_v141_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_378d_e21_base_v142_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_378d_smadf_base_v143_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_378d_smarat_base_v144_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_378d_zsq_base_v145_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_504d_s21_base_v146_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_504d_e21_base_v147_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_504d_smadf_base_v148_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_504d_smarat_base_v149_signal,
    f023kbs_f023_keltner_vs_bollinger_squeeze_p3_504d_zsq_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F023_KELTNER_VS_BOLLINGER_SQUEEZE_REGISTRY_076_150 = REGISTRY


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

    cols = {"closeadj": closeadj, "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f023_keltner', '_f023_bb_kc_squeeze', '_f023_ttm_squeeze')
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
    print(f"OK f023_keltner_vs_bollinger_squeeze_base_076_150_claude: {n_features} features pass")
