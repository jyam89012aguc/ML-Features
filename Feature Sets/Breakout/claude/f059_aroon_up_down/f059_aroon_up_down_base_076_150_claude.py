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
def _f059_aroon_up(close, w):
    rolling_max_idx = close.rolling(w, min_periods=max(1, w // 2)).apply(
        lambda x: float(len(x) - 1 - x.values.argmax()) if len(x) > 0 else np.nan, raw=False)
    return 100.0 * (float(w) - rolling_max_idx) / float(w)


def _f059_aroon_down(close, w):
    rolling_min_idx = close.rolling(w, min_periods=max(1, w // 2)).apply(
        lambda x: float(len(x) - 1 - x.values.argmin()) if len(x) > 0 else np.nan, raw=False)
    return 100.0 * (float(w) - rolling_min_idx) / float(w)


def _f059_aroon_oscillator(close, w):
    up_idx = close.rolling(w, min_periods=max(1, w // 2)).apply(
        lambda x: float(len(x) - 1 - x.values.argmax()) if len(x) > 0 else np.nan, raw=False)
    dn_idx = close.rolling(w, min_periods=max(1, w // 2)).apply(
        lambda x: float(len(x) - 1 - x.values.argmin()) if len(x) > 0 else np.nan, raw=False)
    up = 100.0 * (float(w) - up_idx) / float(w)
    dn = 100.0 * (float(w) - dn_idx) / float(w)
    return up - dn



# aup base_w=21 variant=absxclose
def f059aud_f059_aroon_up_down_aup_21d_absxclose_base_v076_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 21)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=signxmean
def f059aud_f059_aroon_up_down_aup_21d_signxmean_base_v077_signal(closeadj):
    result = np.sign(_f059_aroon_up(closeadj, 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=signxclose
def f059aud_f059_aroon_up_down_aup_21d_signxclose_base_v078_signal(closeadj):
    result = np.sign(_f059_aroon_up(closeadj, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=zclose63
def f059aud_f059_aroon_up_down_aup_21d_zclose63_base_v079_signal(closeadj):
    result = _z(_f059_aroon_up(closeadj, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=zclose252
def f059aud_f059_aroon_up_down_aup_21d_zclose252_base_v080_signal(closeadj):
    result = _z(_f059_aroon_up(closeadj, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=rankxclose
def f059aud_f059_aroon_up_down_aup_21d_rankxclose_base_v081_signal(closeadj):
    result = _f059_aroon_up(closeadj, 21).rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=logmag
def f059aud_f059_aroon_up_down_aup_21d_logmag_base_v082_signal(closeadj):
    result = np.sign(_f059_aroon_up(closeadj, 21)) * np.log(1.0 + (_f059_aroon_up(closeadj, 21)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=xclosediff
def f059aud_f059_aroon_up_down_aup_21d_xclosediff_base_v083_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 21)) * closeadj.diff(5).rolling(21, min_periods=5).mean().abs()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=xrunmean63
def f059aud_f059_aroon_up_down_aup_21d_xrunmean63_base_v084_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 21)) * _mean(closeadj * closeadj, 63) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=ratio252
def f059aud_f059_aroon_up_down_aup_21d_ratio252_base_v085_signal(closeadj):
    result = _safe_div(_f059_aroon_up(closeadj, 21), _mean(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=xstd21
def f059aud_f059_aroon_up_down_aup_21d_xstd21_base_v086_signal(closeadj):
    result = _f059_aroon_up(closeadj, 21) * _std(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=zclose126
def f059aud_f059_aroon_up_down_aup_21d_zclose126_base_v087_signal(closeadj):
    result = _z(_f059_aroon_up(closeadj, 21), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=plusclose
def f059aud_f059_aroon_up_down_aup_21d_plusclose_base_v088_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 21) + closeadj) * np.sign(closeadj.diff(21))
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=xema5
def f059aud_f059_aroon_up_down_aup_21d_xema5_base_v089_signal(closeadj):
    result = _f059_aroon_up(closeadj, 21) * closeadj.ewm(span=5, min_periods=3).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=xema252
def f059aud_f059_aroon_up_down_aup_21d_xema252_base_v090_signal(closeadj):
    result = _f059_aroon_up(closeadj, 21) * closeadj.ewm(span=252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=xclose
def f059aud_f059_aroon_up_down_aup_42d_xclose_base_v091_signal(closeadj):
    result = _f059_aroon_up(closeadj, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=xmean21
def f059aud_f059_aroon_up_down_aup_42d_xmean21_base_v092_signal(closeadj):
    result = _f059_aroon_up(closeadj, 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=xmean63
def f059aud_f059_aroon_up_down_aup_42d_xmean63_base_v093_signal(closeadj):
    result = _f059_aroon_up(closeadj, 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=xmean252
def f059aud_f059_aroon_up_down_aup_42d_xmean252_base_v094_signal(closeadj):
    result = _f059_aroon_up(closeadj, 42) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=xstd63
def f059aud_f059_aroon_up_down_aup_42d_xstd63_base_v095_signal(closeadj):
    result = _f059_aroon_up(closeadj, 42) * _std(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=xstd252
def f059aud_f059_aroon_up_down_aup_42d_xstd252_base_v096_signal(closeadj):
    result = _f059_aroon_up(closeadj, 42) * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=xclosesq
def f059aud_f059_aroon_up_down_aup_42d_xclosesq_base_v097_signal(closeadj):
    result = _f059_aroon_up(closeadj, 42) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=xema21
def f059aud_f059_aroon_up_down_aup_42d_xema21_base_v098_signal(closeadj):
    result = _f059_aroon_up(closeadj, 42) * closeadj.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=xema63
def f059aud_f059_aroon_up_down_aup_42d_xema63_base_v099_signal(closeadj):
    result = _f059_aroon_up(closeadj, 42) * closeadj.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=xema126
def f059aud_f059_aroon_up_down_aup_42d_xema126_base_v100_signal(closeadj):
    result = _f059_aroon_up(closeadj, 42) * closeadj.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=plusmean
def f059aud_f059_aroon_up_down_aup_42d_plusmean_base_v101_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 42) + _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=minusmean
def f059aud_f059_aroon_up_down_aup_42d_minusmean_base_v102_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 42) - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=addclose
def f059aud_f059_aroon_up_down_aup_42d_addclose_base_v103_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 42) + closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=subclose
def f059aud_f059_aroon_up_down_aup_42d_subclose_base_v104_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 42) - closeadj * 0.0 + closeadj * _f059_aroon_up(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=squared
def f059aud_f059_aroon_up_down_aup_42d_squared_base_v105_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 42) * _f059_aroon_up(closeadj, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=absxclose
def f059aud_f059_aroon_up_down_aup_42d_absxclose_base_v106_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 42)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=signxmean
def f059aud_f059_aroon_up_down_aup_42d_signxmean_base_v107_signal(closeadj):
    result = np.sign(_f059_aroon_up(closeadj, 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=signxclose
def f059aud_f059_aroon_up_down_aup_42d_signxclose_base_v108_signal(closeadj):
    result = np.sign(_f059_aroon_up(closeadj, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=zclose63
def f059aud_f059_aroon_up_down_aup_42d_zclose63_base_v109_signal(closeadj):
    result = _z(_f059_aroon_up(closeadj, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=zclose252
def f059aud_f059_aroon_up_down_aup_42d_zclose252_base_v110_signal(closeadj):
    result = _z(_f059_aroon_up(closeadj, 42), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=rankxclose
def f059aud_f059_aroon_up_down_aup_42d_rankxclose_base_v111_signal(closeadj):
    result = _f059_aroon_up(closeadj, 42).rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=logmag
def f059aud_f059_aroon_up_down_aup_42d_logmag_base_v112_signal(closeadj):
    result = np.sign(_f059_aroon_up(closeadj, 42)) * np.log(1.0 + (_f059_aroon_up(closeadj, 42)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=xclosediff
def f059aud_f059_aroon_up_down_aup_42d_xclosediff_base_v113_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 42)) * closeadj.diff(5).rolling(21, min_periods=5).mean().abs()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=xrunmean63
def f059aud_f059_aroon_up_down_aup_42d_xrunmean63_base_v114_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 42)) * _mean(closeadj * closeadj, 63) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=ratio252
def f059aud_f059_aroon_up_down_aup_42d_ratio252_base_v115_signal(closeadj):
    result = _safe_div(_f059_aroon_up(closeadj, 42), _mean(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=xstd21
def f059aud_f059_aroon_up_down_aup_42d_xstd21_base_v116_signal(closeadj):
    result = _f059_aroon_up(closeadj, 42) * _std(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=zclose126
def f059aud_f059_aroon_up_down_aup_42d_zclose126_base_v117_signal(closeadj):
    result = _z(_f059_aroon_up(closeadj, 42), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=plusclose
def f059aud_f059_aroon_up_down_aup_42d_plusclose_base_v118_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 42) + closeadj) * np.sign(closeadj.diff(21))
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=xema5
def f059aud_f059_aroon_up_down_aup_42d_xema5_base_v119_signal(closeadj):
    result = _f059_aroon_up(closeadj, 42) * closeadj.ewm(span=5, min_periods=3).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=42 variant=xema252
def f059aud_f059_aroon_up_down_aup_42d_xema252_base_v120_signal(closeadj):
    result = _f059_aroon_up(closeadj, 42) * closeadj.ewm(span=252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=xclose
def f059aud_f059_aroon_up_down_aup_63d_xclose_base_v121_signal(closeadj):
    result = _f059_aroon_up(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=xmean21
def f059aud_f059_aroon_up_down_aup_63d_xmean21_base_v122_signal(closeadj):
    result = _f059_aroon_up(closeadj, 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=xmean63
def f059aud_f059_aroon_up_down_aup_63d_xmean63_base_v123_signal(closeadj):
    result = _f059_aroon_up(closeadj, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=xmean252
def f059aud_f059_aroon_up_down_aup_63d_xmean252_base_v124_signal(closeadj):
    result = _f059_aroon_up(closeadj, 63) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=xstd63
def f059aud_f059_aroon_up_down_aup_63d_xstd63_base_v125_signal(closeadj):
    result = _f059_aroon_up(closeadj, 63) * _std(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=xstd252
def f059aud_f059_aroon_up_down_aup_63d_xstd252_base_v126_signal(closeadj):
    result = _f059_aroon_up(closeadj, 63) * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=xclosesq
def f059aud_f059_aroon_up_down_aup_63d_xclosesq_base_v127_signal(closeadj):
    result = _f059_aroon_up(closeadj, 63) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=xema21
def f059aud_f059_aroon_up_down_aup_63d_xema21_base_v128_signal(closeadj):
    result = _f059_aroon_up(closeadj, 63) * closeadj.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=xema63
def f059aud_f059_aroon_up_down_aup_63d_xema63_base_v129_signal(closeadj):
    result = _f059_aroon_up(closeadj, 63) * closeadj.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=xema126
def f059aud_f059_aroon_up_down_aup_63d_xema126_base_v130_signal(closeadj):
    result = _f059_aroon_up(closeadj, 63) * closeadj.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=plusmean
def f059aud_f059_aroon_up_down_aup_63d_plusmean_base_v131_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 63) + _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=minusmean
def f059aud_f059_aroon_up_down_aup_63d_minusmean_base_v132_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 63) - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=addclose
def f059aud_f059_aroon_up_down_aup_63d_addclose_base_v133_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 63) + closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=subclose
def f059aud_f059_aroon_up_down_aup_63d_subclose_base_v134_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 63) - closeadj * 0.0 + closeadj * _f059_aroon_up(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=squared
def f059aud_f059_aroon_up_down_aup_63d_squared_base_v135_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 63) * _f059_aroon_up(closeadj, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=absxclose
def f059aud_f059_aroon_up_down_aup_63d_absxclose_base_v136_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 63)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=signxmean
def f059aud_f059_aroon_up_down_aup_63d_signxmean_base_v137_signal(closeadj):
    result = np.sign(_f059_aroon_up(closeadj, 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=signxclose
def f059aud_f059_aroon_up_down_aup_63d_signxclose_base_v138_signal(closeadj):
    result = np.sign(_f059_aroon_up(closeadj, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=zclose63
def f059aud_f059_aroon_up_down_aup_63d_zclose63_base_v139_signal(closeadj):
    result = _z(_f059_aroon_up(closeadj, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=zclose252
def f059aud_f059_aroon_up_down_aup_63d_zclose252_base_v140_signal(closeadj):
    result = _z(_f059_aroon_up(closeadj, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=rankxclose
def f059aud_f059_aroon_up_down_aup_63d_rankxclose_base_v141_signal(closeadj):
    result = _f059_aroon_up(closeadj, 63).rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=logmag
def f059aud_f059_aroon_up_down_aup_63d_logmag_base_v142_signal(closeadj):
    result = np.sign(_f059_aroon_up(closeadj, 63)) * np.log(1.0 + (_f059_aroon_up(closeadj, 63)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=xclosediff
def f059aud_f059_aroon_up_down_aup_63d_xclosediff_base_v143_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 63)) * closeadj.diff(5).rolling(21, min_periods=5).mean().abs()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=xrunmean63
def f059aud_f059_aroon_up_down_aup_63d_xrunmean63_base_v144_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 63)) * _mean(closeadj * closeadj, 63) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=ratio252
def f059aud_f059_aroon_up_down_aup_63d_ratio252_base_v145_signal(closeadj):
    result = _safe_div(_f059_aroon_up(closeadj, 63), _mean(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=xstd21
def f059aud_f059_aroon_up_down_aup_63d_xstd21_base_v146_signal(closeadj):
    result = _f059_aroon_up(closeadj, 63) * _std(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=zclose126
def f059aud_f059_aroon_up_down_aup_63d_zclose126_base_v147_signal(closeadj):
    result = _z(_f059_aroon_up(closeadj, 63), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=plusclose
def f059aud_f059_aroon_up_down_aup_63d_plusclose_base_v148_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 63) + closeadj) * np.sign(closeadj.diff(21))
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=xema5
def f059aud_f059_aroon_up_down_aup_63d_xema5_base_v149_signal(closeadj):
    result = _f059_aroon_up(closeadj, 63) * closeadj.ewm(span=5, min_periods=3).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=63 variant=xema252
def f059aud_f059_aroon_up_down_aup_63d_xema252_base_v150_signal(closeadj):
    result = _f059_aroon_up(closeadj, 63) * closeadj.ewm(span=252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f059aud_f059_aroon_up_down_aup_21d_absxclose_base_v076_signal,
    f059aud_f059_aroon_up_down_aup_21d_signxmean_base_v077_signal,
    f059aud_f059_aroon_up_down_aup_21d_signxclose_base_v078_signal,
    f059aud_f059_aroon_up_down_aup_21d_zclose63_base_v079_signal,
    f059aud_f059_aroon_up_down_aup_21d_zclose252_base_v080_signal,
    f059aud_f059_aroon_up_down_aup_21d_rankxclose_base_v081_signal,
    f059aud_f059_aroon_up_down_aup_21d_logmag_base_v082_signal,
    f059aud_f059_aroon_up_down_aup_21d_xclosediff_base_v083_signal,
    f059aud_f059_aroon_up_down_aup_21d_xrunmean63_base_v084_signal,
    f059aud_f059_aroon_up_down_aup_21d_ratio252_base_v085_signal,
    f059aud_f059_aroon_up_down_aup_21d_xstd21_base_v086_signal,
    f059aud_f059_aroon_up_down_aup_21d_zclose126_base_v087_signal,
    f059aud_f059_aroon_up_down_aup_21d_plusclose_base_v088_signal,
    f059aud_f059_aroon_up_down_aup_21d_xema5_base_v089_signal,
    f059aud_f059_aroon_up_down_aup_21d_xema252_base_v090_signal,
    f059aud_f059_aroon_up_down_aup_42d_xclose_base_v091_signal,
    f059aud_f059_aroon_up_down_aup_42d_xmean21_base_v092_signal,
    f059aud_f059_aroon_up_down_aup_42d_xmean63_base_v093_signal,
    f059aud_f059_aroon_up_down_aup_42d_xmean252_base_v094_signal,
    f059aud_f059_aroon_up_down_aup_42d_xstd63_base_v095_signal,
    f059aud_f059_aroon_up_down_aup_42d_xstd252_base_v096_signal,
    f059aud_f059_aroon_up_down_aup_42d_xclosesq_base_v097_signal,
    f059aud_f059_aroon_up_down_aup_42d_xema21_base_v098_signal,
    f059aud_f059_aroon_up_down_aup_42d_xema63_base_v099_signal,
    f059aud_f059_aroon_up_down_aup_42d_xema126_base_v100_signal,
    f059aud_f059_aroon_up_down_aup_42d_plusmean_base_v101_signal,
    f059aud_f059_aroon_up_down_aup_42d_minusmean_base_v102_signal,
    f059aud_f059_aroon_up_down_aup_42d_addclose_base_v103_signal,
    f059aud_f059_aroon_up_down_aup_42d_subclose_base_v104_signal,
    f059aud_f059_aroon_up_down_aup_42d_squared_base_v105_signal,
    f059aud_f059_aroon_up_down_aup_42d_absxclose_base_v106_signal,
    f059aud_f059_aroon_up_down_aup_42d_signxmean_base_v107_signal,
    f059aud_f059_aroon_up_down_aup_42d_signxclose_base_v108_signal,
    f059aud_f059_aroon_up_down_aup_42d_zclose63_base_v109_signal,
    f059aud_f059_aroon_up_down_aup_42d_zclose252_base_v110_signal,
    f059aud_f059_aroon_up_down_aup_42d_rankxclose_base_v111_signal,
    f059aud_f059_aroon_up_down_aup_42d_logmag_base_v112_signal,
    f059aud_f059_aroon_up_down_aup_42d_xclosediff_base_v113_signal,
    f059aud_f059_aroon_up_down_aup_42d_xrunmean63_base_v114_signal,
    f059aud_f059_aroon_up_down_aup_42d_ratio252_base_v115_signal,
    f059aud_f059_aroon_up_down_aup_42d_xstd21_base_v116_signal,
    f059aud_f059_aroon_up_down_aup_42d_zclose126_base_v117_signal,
    f059aud_f059_aroon_up_down_aup_42d_plusclose_base_v118_signal,
    f059aud_f059_aroon_up_down_aup_42d_xema5_base_v119_signal,
    f059aud_f059_aroon_up_down_aup_42d_xema252_base_v120_signal,
    f059aud_f059_aroon_up_down_aup_63d_xclose_base_v121_signal,
    f059aud_f059_aroon_up_down_aup_63d_xmean21_base_v122_signal,
    f059aud_f059_aroon_up_down_aup_63d_xmean63_base_v123_signal,
    f059aud_f059_aroon_up_down_aup_63d_xmean252_base_v124_signal,
    f059aud_f059_aroon_up_down_aup_63d_xstd63_base_v125_signal,
    f059aud_f059_aroon_up_down_aup_63d_xstd252_base_v126_signal,
    f059aud_f059_aroon_up_down_aup_63d_xclosesq_base_v127_signal,
    f059aud_f059_aroon_up_down_aup_63d_xema21_base_v128_signal,
    f059aud_f059_aroon_up_down_aup_63d_xema63_base_v129_signal,
    f059aud_f059_aroon_up_down_aup_63d_xema126_base_v130_signal,
    f059aud_f059_aroon_up_down_aup_63d_plusmean_base_v131_signal,
    f059aud_f059_aroon_up_down_aup_63d_minusmean_base_v132_signal,
    f059aud_f059_aroon_up_down_aup_63d_addclose_base_v133_signal,
    f059aud_f059_aroon_up_down_aup_63d_subclose_base_v134_signal,
    f059aud_f059_aroon_up_down_aup_63d_squared_base_v135_signal,
    f059aud_f059_aroon_up_down_aup_63d_absxclose_base_v136_signal,
    f059aud_f059_aroon_up_down_aup_63d_signxmean_base_v137_signal,
    f059aud_f059_aroon_up_down_aup_63d_signxclose_base_v138_signal,
    f059aud_f059_aroon_up_down_aup_63d_zclose63_base_v139_signal,
    f059aud_f059_aroon_up_down_aup_63d_zclose252_base_v140_signal,
    f059aud_f059_aroon_up_down_aup_63d_rankxclose_base_v141_signal,
    f059aud_f059_aroon_up_down_aup_63d_logmag_base_v142_signal,
    f059aud_f059_aroon_up_down_aup_63d_xclosediff_base_v143_signal,
    f059aud_f059_aroon_up_down_aup_63d_xrunmean63_base_v144_signal,
    f059aud_f059_aroon_up_down_aup_63d_ratio252_base_v145_signal,
    f059aud_f059_aroon_up_down_aup_63d_xstd21_base_v146_signal,
    f059aud_f059_aroon_up_down_aup_63d_zclose126_base_v147_signal,
    f059aud_f059_aroon_up_down_aup_63d_plusclose_base_v148_signal,
    f059aud_f059_aroon_up_down_aup_63d_xema5_base_v149_signal,
    f059aud_f059_aroon_up_down_aup_63d_xema252_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F059_AROON_UP_DOWN_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f059_aroon_up", "_f059_aroon_down", "_f059_aroon_oscillator",)
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
    print(f"OK f059_aroon_up_down_base_076_150_claude: {n_features} features pass")
