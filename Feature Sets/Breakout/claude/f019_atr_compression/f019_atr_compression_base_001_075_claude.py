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

def _f019_atr(high, low, closeadj, w):
    prev_c = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(),
                    (high - prev_c).abs(),
                    (low - prev_c).abs()], axis=1).max(axis=1)
    return tr.rolling(w, min_periods=max(1, w // 2)).mean()


def _f019_atr_compression(high, low, closeadj, w):
    atr_s = _f019_atr(high, low, closeadj, w)
    atr_l = _f019_atr(high, low, closeadj, w * 4)
    return atr_s / atr_l.replace(0, np.nan)


def _f019_squeeze_score(high, low, closeadj, w):
    atr = _f019_atr(high, low, closeadj, w)
    atr_norm = atr / closeadj.replace(0, np.nan).abs()
    z = _z(atr_norm, w * 2)
    return -z



# ===== features =====
def f019atc_f019_atr_compression_p2_sma126_close_42d_base_v001_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 42)
    result = (_mean(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_raw_close_10d_base_v002_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 10)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_z252_closesma21_126d_base_v003_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 126)
    result = (_z(base, 252)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_z63_closesma63_378d_base_v004_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 378)
    result = (_z(base, 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_diff5_closesma63_126d_base_v005_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 126)
    result = ((base).diff(5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_diff63_closesma63_126d_base_v006_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 126)
    result = ((base).diff(63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_diff21_closesma21_189d_base_v007_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 189)
    result = ((base).diff(21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_std21_close_189d_base_v008_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 189)
    result = (_std(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_z21_closesma63_126d_base_v009_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 126)
    result = (_z(base, 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_sma21_close_10d_base_v010_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 10)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_diff5_closesq_10d_base_v011_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 10)
    result = ((base).diff(5)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_std21_closesq_5d_base_v012_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 5)
    result = (_std(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_sma63_closesq_504d_base_v013_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 504)
    result = (_mean(base, 63)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_std126_closesq_189d_base_v014_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 189)
    result = (_std(base, 126)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_z63_closesma21_63d_base_v015_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 63)
    result = (_z(base, 63)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_z21_closesq_63d_base_v016_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 63)
    result = (_z(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_z126_closesma63_378d_base_v017_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 378)
    result = (_z(base, 126)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_z126_closesma63_252d_base_v018_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 252)
    result = (_z(base, 126)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_z252_closesma21_252d_base_v019_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 252)
    result = (_z(base, 252)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_diff63_closesma21_5d_base_v020_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 5)
    result = ((base).diff(63)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_sma126_closesma21_21d_base_v021_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 21)
    result = (_mean(base, 126)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_sma21_closesma21_189d_base_v022_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 189)
    result = (_mean(base, 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_raw_closesma21_126d_base_v023_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 126)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_z63_closesma63_252d_base_v024_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 252)
    result = (_z(base, 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_z252_closesma21_42d_base_v025_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 42)
    result = (_z(base, 252)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_sma21_closesq_63d_base_v026_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 63)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_sma21_close_63d_base_v027_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 63)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_std126_closesma63_5d_base_v028_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 5)
    result = (_std(base, 126)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_raw_closesq_42d_base_v029_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 42)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_raw_closesma63_378d_base_v030_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 378)
    result = (base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_diff5_closesq_378d_base_v031_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 378)
    result = ((base).diff(5)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_z21_closesma21_21d_base_v032_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 21)
    result = (_z(base, 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_diff63_close_126d_base_v033_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 126)
    result = ((base).diff(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_raw_close_5d_base_v034_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 5)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_diff63_closesq_252d_base_v035_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 252)
    result = ((base).diff(63)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_sma126_closesq_21d_base_v036_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 21)
    result = (_mean(base, 126)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_diff21_closesq_10d_base_v037_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 10)
    result = ((base).diff(21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_z126_closesq_5d_base_v038_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 5)
    result = (_z(base, 126)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_std63_closesma63_42d_base_v039_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 42)
    result = (_std(base, 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_z252_close_378d_base_v040_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 378)
    result = (_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_z63_closesq_21d_base_v041_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 21)
    result = (_z(base, 63)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_std21_closesq_126d_base_v042_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 126)
    result = (_std(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_sma21_closesma21_63d_base_v043_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 63)
    result = (_mean(base, 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_std126_closesma63_5d_base_v044_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 5)
    result = (_std(base, 126)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_std21_close_126d_base_v045_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 126)
    result = (_std(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_std21_closesma63_63d_base_v046_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 63)
    result = (_std(base, 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_z126_closesma21_5d_base_v047_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 5)
    result = (_z(base, 126)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_std63_closesma21_21d_base_v048_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 21)
    result = (_std(base, 63)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_z252_close_504d_base_v049_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 504)
    result = (_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_std63_close_189d_base_v050_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 189)
    result = (_std(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_sma21_closesq_378d_base_v051_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 378)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_diff21_closesma21_126d_base_v052_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 126)
    result = ((base).diff(21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_raw_closesma21_63d_base_v053_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 63)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_z63_closesq_10d_base_v054_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 10)
    result = (_z(base, 63)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_sma126_closesma21_252d_base_v055_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 252)
    result = (_mean(base, 126)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_z63_closesma21_504d_base_v056_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 504)
    result = (_z(base, 63)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_sma63_closesma63_252d_base_v057_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 252)
    result = (_mean(base, 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_z21_closesq_378d_base_v058_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 378)
    result = (_z(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_diff5_closesma63_5d_base_v059_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 5)
    result = ((base).diff(5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_raw_closesma21_378d_base_v060_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 378)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_sma21_closesq_126d_base_v061_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 126)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_diff21_close_21d_base_v062_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 21)
    result = ((base).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_z126_close_63d_base_v063_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 63)
    result = (_z(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_diff5_closesma21_5d_base_v064_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 5)
    result = ((base).diff(5)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_sma126_closesma63_504d_base_v065_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 504)
    result = (_mean(base, 126)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_std21_closesma21_252d_base_v066_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 252)
    result = (_std(base, 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_diff63_closesma63_42d_base_v067_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 42)
    result = ((base).diff(63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_z21_close_63d_base_v068_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 63)
    result = (_z(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_z252_closesma21_126d_base_v069_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 126)
    result = (_z(base, 252)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_diff5_closesma63_378d_base_v070_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 378)
    result = ((base).diff(5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_z126_close_42d_base_v071_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 42)
    result = (_z(base, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p1_raw_closesma63_63d_base_v072_signal(high, low, closeadj):
    base = _f019_atr(high, low, closeadj, 63)
    result = (base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_z126_closesma63_63d_base_v073_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 63)
    result = (_z(base, 126)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p3_z21_closesq_252d_base_v074_signal(high, low, closeadj):
    base = _f019_squeeze_score(high, low, closeadj, 252)
    result = (_z(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f019atc_f019_atr_compression_p2_std126_closesq_252d_base_v075_signal(high, low, closeadj):
    base = _f019_atr_compression(high, low, closeadj, 252)
    result = (_std(base, 126)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f019atc_f019_atr_compression_p2_sma126_close_42d_base_v001_signal,
    f019atc_f019_atr_compression_p2_raw_close_10d_base_v002_signal,
    f019atc_f019_atr_compression_p2_z252_closesma21_126d_base_v003_signal,
    f019atc_f019_atr_compression_p3_z63_closesma63_378d_base_v004_signal,
    f019atc_f019_atr_compression_p3_diff5_closesma63_126d_base_v005_signal,
    f019atc_f019_atr_compression_p1_diff63_closesma63_126d_base_v006_signal,
    f019atc_f019_atr_compression_p1_diff21_closesma21_189d_base_v007_signal,
    f019atc_f019_atr_compression_p3_std21_close_189d_base_v008_signal,
    f019atc_f019_atr_compression_p3_z21_closesma63_126d_base_v009_signal,
    f019atc_f019_atr_compression_p3_sma21_close_10d_base_v010_signal,
    f019atc_f019_atr_compression_p3_diff5_closesq_10d_base_v011_signal,
    f019atc_f019_atr_compression_p2_std21_closesq_5d_base_v012_signal,
    f019atc_f019_atr_compression_p3_sma63_closesq_504d_base_v013_signal,
    f019atc_f019_atr_compression_p1_std126_closesq_189d_base_v014_signal,
    f019atc_f019_atr_compression_p1_z63_closesma21_63d_base_v015_signal,
    f019atc_f019_atr_compression_p1_z21_closesq_63d_base_v016_signal,
    f019atc_f019_atr_compression_p1_z126_closesma63_378d_base_v017_signal,
    f019atc_f019_atr_compression_p3_z126_closesma63_252d_base_v018_signal,
    f019atc_f019_atr_compression_p1_z252_closesma21_252d_base_v019_signal,
    f019atc_f019_atr_compression_p2_diff63_closesma21_5d_base_v020_signal,
    f019atc_f019_atr_compression_p1_sma126_closesma21_21d_base_v021_signal,
    f019atc_f019_atr_compression_p3_sma21_closesma21_189d_base_v022_signal,
    f019atc_f019_atr_compression_p2_raw_closesma21_126d_base_v023_signal,
    f019atc_f019_atr_compression_p2_z63_closesma63_252d_base_v024_signal,
    f019atc_f019_atr_compression_p1_z252_closesma21_42d_base_v025_signal,
    f019atc_f019_atr_compression_p1_sma21_closesq_63d_base_v026_signal,
    f019atc_f019_atr_compression_p2_sma21_close_63d_base_v027_signal,
    f019atc_f019_atr_compression_p1_std126_closesma63_5d_base_v028_signal,
    f019atc_f019_atr_compression_p3_raw_closesq_42d_base_v029_signal,
    f019atc_f019_atr_compression_p1_raw_closesma63_378d_base_v030_signal,
    f019atc_f019_atr_compression_p2_diff5_closesq_378d_base_v031_signal,
    f019atc_f019_atr_compression_p1_z21_closesma21_21d_base_v032_signal,
    f019atc_f019_atr_compression_p1_diff63_close_126d_base_v033_signal,
    f019atc_f019_atr_compression_p2_raw_close_5d_base_v034_signal,
    f019atc_f019_atr_compression_p2_diff63_closesq_252d_base_v035_signal,
    f019atc_f019_atr_compression_p2_sma126_closesq_21d_base_v036_signal,
    f019atc_f019_atr_compression_p3_diff21_closesq_10d_base_v037_signal,
    f019atc_f019_atr_compression_p2_z126_closesq_5d_base_v038_signal,
    f019atc_f019_atr_compression_p1_std63_closesma63_42d_base_v039_signal,
    f019atc_f019_atr_compression_p2_z252_close_378d_base_v040_signal,
    f019atc_f019_atr_compression_p2_z63_closesq_21d_base_v041_signal,
    f019atc_f019_atr_compression_p2_std21_closesq_126d_base_v042_signal,
    f019atc_f019_atr_compression_p3_sma21_closesma21_63d_base_v043_signal,
    f019atc_f019_atr_compression_p2_std126_closesma63_5d_base_v044_signal,
    f019atc_f019_atr_compression_p1_std21_close_126d_base_v045_signal,
    f019atc_f019_atr_compression_p1_std21_closesma63_63d_base_v046_signal,
    f019atc_f019_atr_compression_p1_z126_closesma21_5d_base_v047_signal,
    f019atc_f019_atr_compression_p3_std63_closesma21_21d_base_v048_signal,
    f019atc_f019_atr_compression_p3_z252_close_504d_base_v049_signal,
    f019atc_f019_atr_compression_p3_std63_close_189d_base_v050_signal,
    f019atc_f019_atr_compression_p3_sma21_closesq_378d_base_v051_signal,
    f019atc_f019_atr_compression_p3_diff21_closesma21_126d_base_v052_signal,
    f019atc_f019_atr_compression_p1_raw_closesma21_63d_base_v053_signal,
    f019atc_f019_atr_compression_p2_z63_closesq_10d_base_v054_signal,
    f019atc_f019_atr_compression_p3_sma126_closesma21_252d_base_v055_signal,
    f019atc_f019_atr_compression_p3_z63_closesma21_504d_base_v056_signal,
    f019atc_f019_atr_compression_p2_sma63_closesma63_252d_base_v057_signal,
    f019atc_f019_atr_compression_p1_z21_closesq_378d_base_v058_signal,
    f019atc_f019_atr_compression_p2_diff5_closesma63_5d_base_v059_signal,
    f019atc_f019_atr_compression_p1_raw_closesma21_378d_base_v060_signal,
    f019atc_f019_atr_compression_p3_sma21_closesq_126d_base_v061_signal,
    f019atc_f019_atr_compression_p3_diff21_close_21d_base_v062_signal,
    f019atc_f019_atr_compression_p3_z126_close_63d_base_v063_signal,
    f019atc_f019_atr_compression_p2_diff5_closesma21_5d_base_v064_signal,
    f019atc_f019_atr_compression_p1_sma126_closesma63_504d_base_v065_signal,
    f019atc_f019_atr_compression_p1_std21_closesma21_252d_base_v066_signal,
    f019atc_f019_atr_compression_p1_diff63_closesma63_42d_base_v067_signal,
    f019atc_f019_atr_compression_p3_z21_close_63d_base_v068_signal,
    f019atc_f019_atr_compression_p1_z252_closesma21_126d_base_v069_signal,
    f019atc_f019_atr_compression_p3_diff5_closesma63_378d_base_v070_signal,
    f019atc_f019_atr_compression_p2_z126_close_42d_base_v071_signal,
    f019atc_f019_atr_compression_p1_raw_closesma63_63d_base_v072_signal,
    f019atc_f019_atr_compression_p3_z126_closesma63_63d_base_v073_signal,
    f019atc_f019_atr_compression_p3_z21_closesq_252d_base_v074_signal,
    f019atc_f019_atr_compression_p2_std126_closesq_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F019_ATR_COMPRESSION_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high.values, name="high")
    low = pd.Series(low.values, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f019_atr', '_f019_atr_compression', '_f019_squeeze_score')
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
    print(f"OK f019_atr_compression_base_001_075_claude: {n_features} features pass")
