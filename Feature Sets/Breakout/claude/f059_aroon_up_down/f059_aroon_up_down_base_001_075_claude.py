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



# aup base_w=5 variant=xclose
def f059aud_f059_aroon_up_down_aup_5d_xclose_base_v001_signal(closeadj):
    result = _f059_aroon_up(closeadj, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=xmean21
def f059aud_f059_aroon_up_down_aup_5d_xmean21_base_v002_signal(closeadj):
    result = _f059_aroon_up(closeadj, 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=xmean63
def f059aud_f059_aroon_up_down_aup_5d_xmean63_base_v003_signal(closeadj):
    result = _f059_aroon_up(closeadj, 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=xmean252
def f059aud_f059_aroon_up_down_aup_5d_xmean252_base_v004_signal(closeadj):
    result = _f059_aroon_up(closeadj, 5) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=xstd63
def f059aud_f059_aroon_up_down_aup_5d_xstd63_base_v005_signal(closeadj):
    result = _f059_aroon_up(closeadj, 5) * _std(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=xstd252
def f059aud_f059_aroon_up_down_aup_5d_xstd252_base_v006_signal(closeadj):
    result = _f059_aroon_up(closeadj, 5) * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=xclosesq
def f059aud_f059_aroon_up_down_aup_5d_xclosesq_base_v007_signal(closeadj):
    result = _f059_aroon_up(closeadj, 5) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=xema21
def f059aud_f059_aroon_up_down_aup_5d_xema21_base_v008_signal(closeadj):
    result = _f059_aroon_up(closeadj, 5) * closeadj.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=xema63
def f059aud_f059_aroon_up_down_aup_5d_xema63_base_v009_signal(closeadj):
    result = _f059_aroon_up(closeadj, 5) * closeadj.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=xema126
def f059aud_f059_aroon_up_down_aup_5d_xema126_base_v010_signal(closeadj):
    result = _f059_aroon_up(closeadj, 5) * closeadj.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=plusmean
def f059aud_f059_aroon_up_down_aup_5d_plusmean_base_v011_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 5) + _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=minusmean
def f059aud_f059_aroon_up_down_aup_5d_minusmean_base_v012_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 5) - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=addclose
def f059aud_f059_aroon_up_down_aup_5d_addclose_base_v013_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 5) + closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=subclose
def f059aud_f059_aroon_up_down_aup_5d_subclose_base_v014_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 5) - closeadj * 0.0 + closeadj * _f059_aroon_up(closeadj, 5))
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=squared
def f059aud_f059_aroon_up_down_aup_5d_squared_base_v015_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 5) * _f059_aroon_up(closeadj, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=absxclose
def f059aud_f059_aroon_up_down_aup_5d_absxclose_base_v016_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 5)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=signxmean
def f059aud_f059_aroon_up_down_aup_5d_signxmean_base_v017_signal(closeadj):
    result = np.sign(_f059_aroon_up(closeadj, 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=signxclose
def f059aud_f059_aroon_up_down_aup_5d_signxclose_base_v018_signal(closeadj):
    result = np.sign(_f059_aroon_up(closeadj, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=zclose63
def f059aud_f059_aroon_up_down_aup_5d_zclose63_base_v019_signal(closeadj):
    result = _z(_f059_aroon_up(closeadj, 5), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=zclose252
def f059aud_f059_aroon_up_down_aup_5d_zclose252_base_v020_signal(closeadj):
    result = _z(_f059_aroon_up(closeadj, 5), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=rankxclose
def f059aud_f059_aroon_up_down_aup_5d_rankxclose_base_v021_signal(closeadj):
    result = _f059_aroon_up(closeadj, 5).rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=logmag
def f059aud_f059_aroon_up_down_aup_5d_logmag_base_v022_signal(closeadj):
    result = np.sign(_f059_aroon_up(closeadj, 5)) * np.log(1.0 + (_f059_aroon_up(closeadj, 5)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=xclosediff
def f059aud_f059_aroon_up_down_aup_5d_xclosediff_base_v023_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 5)) * closeadj.diff(5).rolling(21, min_periods=5).mean().abs()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=xrunmean63
def f059aud_f059_aroon_up_down_aup_5d_xrunmean63_base_v024_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 5)) * _mean(closeadj * closeadj, 63) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=ratio252
def f059aud_f059_aroon_up_down_aup_5d_ratio252_base_v025_signal(closeadj):
    result = _safe_div(_f059_aroon_up(closeadj, 5), _mean(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=xstd21
def f059aud_f059_aroon_up_down_aup_5d_xstd21_base_v026_signal(closeadj):
    result = _f059_aroon_up(closeadj, 5) * _std(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=zclose126
def f059aud_f059_aroon_up_down_aup_5d_zclose126_base_v027_signal(closeadj):
    result = _z(_f059_aroon_up(closeadj, 5), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=plusclose
def f059aud_f059_aroon_up_down_aup_5d_plusclose_base_v028_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 5) + closeadj) * np.sign(closeadj.diff(21))
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=xema5
def f059aud_f059_aroon_up_down_aup_5d_xema5_base_v029_signal(closeadj):
    result = _f059_aroon_up(closeadj, 5) * closeadj.ewm(span=5, min_periods=3).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=5 variant=xema252
def f059aud_f059_aroon_up_down_aup_5d_xema252_base_v030_signal(closeadj):
    result = _f059_aroon_up(closeadj, 5) * closeadj.ewm(span=252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=xclose
def f059aud_f059_aroon_up_down_aup_10d_xclose_base_v031_signal(closeadj):
    result = _f059_aroon_up(closeadj, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=xmean21
def f059aud_f059_aroon_up_down_aup_10d_xmean21_base_v032_signal(closeadj):
    result = _f059_aroon_up(closeadj, 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=xmean63
def f059aud_f059_aroon_up_down_aup_10d_xmean63_base_v033_signal(closeadj):
    result = _f059_aroon_up(closeadj, 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=xmean252
def f059aud_f059_aroon_up_down_aup_10d_xmean252_base_v034_signal(closeadj):
    result = _f059_aroon_up(closeadj, 10) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=xstd63
def f059aud_f059_aroon_up_down_aup_10d_xstd63_base_v035_signal(closeadj):
    result = _f059_aroon_up(closeadj, 10) * _std(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=xstd252
def f059aud_f059_aroon_up_down_aup_10d_xstd252_base_v036_signal(closeadj):
    result = _f059_aroon_up(closeadj, 10) * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=xclosesq
def f059aud_f059_aroon_up_down_aup_10d_xclosesq_base_v037_signal(closeadj):
    result = _f059_aroon_up(closeadj, 10) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=xema21
def f059aud_f059_aroon_up_down_aup_10d_xema21_base_v038_signal(closeadj):
    result = _f059_aroon_up(closeadj, 10) * closeadj.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=xema63
def f059aud_f059_aroon_up_down_aup_10d_xema63_base_v039_signal(closeadj):
    result = _f059_aroon_up(closeadj, 10) * closeadj.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=xema126
def f059aud_f059_aroon_up_down_aup_10d_xema126_base_v040_signal(closeadj):
    result = _f059_aroon_up(closeadj, 10) * closeadj.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=plusmean
def f059aud_f059_aroon_up_down_aup_10d_plusmean_base_v041_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 10) + _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=minusmean
def f059aud_f059_aroon_up_down_aup_10d_minusmean_base_v042_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 10) - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=addclose
def f059aud_f059_aroon_up_down_aup_10d_addclose_base_v043_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 10) + closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=subclose
def f059aud_f059_aroon_up_down_aup_10d_subclose_base_v044_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 10) - closeadj * 0.0 + closeadj * _f059_aroon_up(closeadj, 10))
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=squared
def f059aud_f059_aroon_up_down_aup_10d_squared_base_v045_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 10) * _f059_aroon_up(closeadj, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=absxclose
def f059aud_f059_aroon_up_down_aup_10d_absxclose_base_v046_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 10)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=signxmean
def f059aud_f059_aroon_up_down_aup_10d_signxmean_base_v047_signal(closeadj):
    result = np.sign(_f059_aroon_up(closeadj, 10)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=signxclose
def f059aud_f059_aroon_up_down_aup_10d_signxclose_base_v048_signal(closeadj):
    result = np.sign(_f059_aroon_up(closeadj, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=zclose63
def f059aud_f059_aroon_up_down_aup_10d_zclose63_base_v049_signal(closeadj):
    result = _z(_f059_aroon_up(closeadj, 10), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=zclose252
def f059aud_f059_aroon_up_down_aup_10d_zclose252_base_v050_signal(closeadj):
    result = _z(_f059_aroon_up(closeadj, 10), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=rankxclose
def f059aud_f059_aroon_up_down_aup_10d_rankxclose_base_v051_signal(closeadj):
    result = _f059_aroon_up(closeadj, 10).rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=logmag
def f059aud_f059_aroon_up_down_aup_10d_logmag_base_v052_signal(closeadj):
    result = np.sign(_f059_aroon_up(closeadj, 10)) * np.log(1.0 + (_f059_aroon_up(closeadj, 10)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=xclosediff
def f059aud_f059_aroon_up_down_aup_10d_xclosediff_base_v053_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 10)) * closeadj.diff(5).rolling(21, min_periods=5).mean().abs()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=xrunmean63
def f059aud_f059_aroon_up_down_aup_10d_xrunmean63_base_v054_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 10)) * _mean(closeadj * closeadj, 63) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=ratio252
def f059aud_f059_aroon_up_down_aup_10d_ratio252_base_v055_signal(closeadj):
    result = _safe_div(_f059_aroon_up(closeadj, 10), _mean(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=xstd21
def f059aud_f059_aroon_up_down_aup_10d_xstd21_base_v056_signal(closeadj):
    result = _f059_aroon_up(closeadj, 10) * _std(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=zclose126
def f059aud_f059_aroon_up_down_aup_10d_zclose126_base_v057_signal(closeadj):
    result = _z(_f059_aroon_up(closeadj, 10), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=plusclose
def f059aud_f059_aroon_up_down_aup_10d_plusclose_base_v058_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 10) + closeadj) * np.sign(closeadj.diff(21))
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=xema5
def f059aud_f059_aroon_up_down_aup_10d_xema5_base_v059_signal(closeadj):
    result = _f059_aroon_up(closeadj, 10) * closeadj.ewm(span=5, min_periods=3).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=10 variant=xema252
def f059aud_f059_aroon_up_down_aup_10d_xema252_base_v060_signal(closeadj):
    result = _f059_aroon_up(closeadj, 10) * closeadj.ewm(span=252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=xclose
def f059aud_f059_aroon_up_down_aup_21d_xclose_base_v061_signal(closeadj):
    result = _f059_aroon_up(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=xmean21
def f059aud_f059_aroon_up_down_aup_21d_xmean21_base_v062_signal(closeadj):
    result = _f059_aroon_up(closeadj, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=xmean63
def f059aud_f059_aroon_up_down_aup_21d_xmean63_base_v063_signal(closeadj):
    result = _f059_aroon_up(closeadj, 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=xmean252
def f059aud_f059_aroon_up_down_aup_21d_xmean252_base_v064_signal(closeadj):
    result = _f059_aroon_up(closeadj, 21) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=xstd63
def f059aud_f059_aroon_up_down_aup_21d_xstd63_base_v065_signal(closeadj):
    result = _f059_aroon_up(closeadj, 21) * _std(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=xstd252
def f059aud_f059_aroon_up_down_aup_21d_xstd252_base_v066_signal(closeadj):
    result = _f059_aroon_up(closeadj, 21) * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=xclosesq
def f059aud_f059_aroon_up_down_aup_21d_xclosesq_base_v067_signal(closeadj):
    result = _f059_aroon_up(closeadj, 21) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=xema21
def f059aud_f059_aroon_up_down_aup_21d_xema21_base_v068_signal(closeadj):
    result = _f059_aroon_up(closeadj, 21) * closeadj.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=xema63
def f059aud_f059_aroon_up_down_aup_21d_xema63_base_v069_signal(closeadj):
    result = _f059_aroon_up(closeadj, 21) * closeadj.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=xema126
def f059aud_f059_aroon_up_down_aup_21d_xema126_base_v070_signal(closeadj):
    result = _f059_aroon_up(closeadj, 21) * closeadj.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=plusmean
def f059aud_f059_aroon_up_down_aup_21d_plusmean_base_v071_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 21) + _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=minusmean
def f059aud_f059_aroon_up_down_aup_21d_minusmean_base_v072_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 21) - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=addclose
def f059aud_f059_aroon_up_down_aup_21d_addclose_base_v073_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 21) + closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=subclose
def f059aud_f059_aroon_up_down_aup_21d_subclose_base_v074_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 21) - closeadj * 0.0 + closeadj * _f059_aroon_up(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# aup base_w=21 variant=squared
def f059aud_f059_aroon_up_down_aup_21d_squared_base_v075_signal(closeadj):
    result = (_f059_aroon_up(closeadj, 21) * _f059_aroon_up(closeadj, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f059aud_f059_aroon_up_down_aup_5d_xclose_base_v001_signal,
    f059aud_f059_aroon_up_down_aup_5d_xmean21_base_v002_signal,
    f059aud_f059_aroon_up_down_aup_5d_xmean63_base_v003_signal,
    f059aud_f059_aroon_up_down_aup_5d_xmean252_base_v004_signal,
    f059aud_f059_aroon_up_down_aup_5d_xstd63_base_v005_signal,
    f059aud_f059_aroon_up_down_aup_5d_xstd252_base_v006_signal,
    f059aud_f059_aroon_up_down_aup_5d_xclosesq_base_v007_signal,
    f059aud_f059_aroon_up_down_aup_5d_xema21_base_v008_signal,
    f059aud_f059_aroon_up_down_aup_5d_xema63_base_v009_signal,
    f059aud_f059_aroon_up_down_aup_5d_xema126_base_v010_signal,
    f059aud_f059_aroon_up_down_aup_5d_plusmean_base_v011_signal,
    f059aud_f059_aroon_up_down_aup_5d_minusmean_base_v012_signal,
    f059aud_f059_aroon_up_down_aup_5d_addclose_base_v013_signal,
    f059aud_f059_aroon_up_down_aup_5d_subclose_base_v014_signal,
    f059aud_f059_aroon_up_down_aup_5d_squared_base_v015_signal,
    f059aud_f059_aroon_up_down_aup_5d_absxclose_base_v016_signal,
    f059aud_f059_aroon_up_down_aup_5d_signxmean_base_v017_signal,
    f059aud_f059_aroon_up_down_aup_5d_signxclose_base_v018_signal,
    f059aud_f059_aroon_up_down_aup_5d_zclose63_base_v019_signal,
    f059aud_f059_aroon_up_down_aup_5d_zclose252_base_v020_signal,
    f059aud_f059_aroon_up_down_aup_5d_rankxclose_base_v021_signal,
    f059aud_f059_aroon_up_down_aup_5d_logmag_base_v022_signal,
    f059aud_f059_aroon_up_down_aup_5d_xclosediff_base_v023_signal,
    f059aud_f059_aroon_up_down_aup_5d_xrunmean63_base_v024_signal,
    f059aud_f059_aroon_up_down_aup_5d_ratio252_base_v025_signal,
    f059aud_f059_aroon_up_down_aup_5d_xstd21_base_v026_signal,
    f059aud_f059_aroon_up_down_aup_5d_zclose126_base_v027_signal,
    f059aud_f059_aroon_up_down_aup_5d_plusclose_base_v028_signal,
    f059aud_f059_aroon_up_down_aup_5d_xema5_base_v029_signal,
    f059aud_f059_aroon_up_down_aup_5d_xema252_base_v030_signal,
    f059aud_f059_aroon_up_down_aup_10d_xclose_base_v031_signal,
    f059aud_f059_aroon_up_down_aup_10d_xmean21_base_v032_signal,
    f059aud_f059_aroon_up_down_aup_10d_xmean63_base_v033_signal,
    f059aud_f059_aroon_up_down_aup_10d_xmean252_base_v034_signal,
    f059aud_f059_aroon_up_down_aup_10d_xstd63_base_v035_signal,
    f059aud_f059_aroon_up_down_aup_10d_xstd252_base_v036_signal,
    f059aud_f059_aroon_up_down_aup_10d_xclosesq_base_v037_signal,
    f059aud_f059_aroon_up_down_aup_10d_xema21_base_v038_signal,
    f059aud_f059_aroon_up_down_aup_10d_xema63_base_v039_signal,
    f059aud_f059_aroon_up_down_aup_10d_xema126_base_v040_signal,
    f059aud_f059_aroon_up_down_aup_10d_plusmean_base_v041_signal,
    f059aud_f059_aroon_up_down_aup_10d_minusmean_base_v042_signal,
    f059aud_f059_aroon_up_down_aup_10d_addclose_base_v043_signal,
    f059aud_f059_aroon_up_down_aup_10d_subclose_base_v044_signal,
    f059aud_f059_aroon_up_down_aup_10d_squared_base_v045_signal,
    f059aud_f059_aroon_up_down_aup_10d_absxclose_base_v046_signal,
    f059aud_f059_aroon_up_down_aup_10d_signxmean_base_v047_signal,
    f059aud_f059_aroon_up_down_aup_10d_signxclose_base_v048_signal,
    f059aud_f059_aroon_up_down_aup_10d_zclose63_base_v049_signal,
    f059aud_f059_aroon_up_down_aup_10d_zclose252_base_v050_signal,
    f059aud_f059_aroon_up_down_aup_10d_rankxclose_base_v051_signal,
    f059aud_f059_aroon_up_down_aup_10d_logmag_base_v052_signal,
    f059aud_f059_aroon_up_down_aup_10d_xclosediff_base_v053_signal,
    f059aud_f059_aroon_up_down_aup_10d_xrunmean63_base_v054_signal,
    f059aud_f059_aroon_up_down_aup_10d_ratio252_base_v055_signal,
    f059aud_f059_aroon_up_down_aup_10d_xstd21_base_v056_signal,
    f059aud_f059_aroon_up_down_aup_10d_zclose126_base_v057_signal,
    f059aud_f059_aroon_up_down_aup_10d_plusclose_base_v058_signal,
    f059aud_f059_aroon_up_down_aup_10d_xema5_base_v059_signal,
    f059aud_f059_aroon_up_down_aup_10d_xema252_base_v060_signal,
    f059aud_f059_aroon_up_down_aup_21d_xclose_base_v061_signal,
    f059aud_f059_aroon_up_down_aup_21d_xmean21_base_v062_signal,
    f059aud_f059_aroon_up_down_aup_21d_xmean63_base_v063_signal,
    f059aud_f059_aroon_up_down_aup_21d_xmean252_base_v064_signal,
    f059aud_f059_aroon_up_down_aup_21d_xstd63_base_v065_signal,
    f059aud_f059_aroon_up_down_aup_21d_xstd252_base_v066_signal,
    f059aud_f059_aroon_up_down_aup_21d_xclosesq_base_v067_signal,
    f059aud_f059_aroon_up_down_aup_21d_xema21_base_v068_signal,
    f059aud_f059_aroon_up_down_aup_21d_xema63_base_v069_signal,
    f059aud_f059_aroon_up_down_aup_21d_xema126_base_v070_signal,
    f059aud_f059_aroon_up_down_aup_21d_plusmean_base_v071_signal,
    f059aud_f059_aroon_up_down_aup_21d_minusmean_base_v072_signal,
    f059aud_f059_aroon_up_down_aup_21d_addclose_base_v073_signal,
    f059aud_f059_aroon_up_down_aup_21d_subclose_base_v074_signal,
    f059aud_f059_aroon_up_down_aup_21d_squared_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F059_AROON_UP_DOWN_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f059_aroon_up_down_base_001_075_claude: {n_features} features pass")
