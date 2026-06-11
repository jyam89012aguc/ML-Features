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
def _f041_vol_range(volume, w):
    hi = volume.rolling(w, min_periods=max(1, w // 2)).max()
    lo = volume.rolling(w, min_periods=max(1, w // 2)).min()
    return (hi - lo) / lo.replace(0, np.nan)


def _f041_vol_vol_compression(volume, w):
    sd = volume.rolling(w, min_periods=max(1, w // 2)).std()
    m = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    return sd / m.replace(0, np.nan)


def _f041_quiet_accumulation(closeadj, volume, w):
    vstd = volume.rolling(w, min_periods=max(1, w // 2)).std()
    pstd = closeadj.pct_change().rolling(w, min_periods=max(1, w // 2)).std()
    return -(vstd * pstd) * closeadj


# v001: 21d volume range scaled by close
def f041vvc_f041_volume_volatility_compression_volrange_21d_base_v001_signal(closeadj, volume):
    result = _f041_vol_range(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v002: 63d volume range scaled by close
def f041vvc_f041_volume_volatility_compression_volrange_63d_base_v002_signal(closeadj, volume):
    result = _f041_vol_range(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v003: 126d volume range scaled by close
def f041vvc_f041_volume_volatility_compression_volrange_126d_base_v003_signal(closeadj, volume):
    result = _f041_vol_range(volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v004: 252d volume range scaled by close
def f041vvc_f041_volume_volatility_compression_volrange_252d_base_v004_signal(closeadj, volume):
    result = _f041_vol_range(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v005: 504d volume range scaled by close
def f041vvc_f041_volume_volatility_compression_volrange_504d_base_v005_signal(closeadj, volume):
    result = _f041_vol_range(volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v006: 5d volume range scaled by close
def f041vvc_f041_volume_volatility_compression_volrange_5d_base_v006_signal(closeadj, volume):
    result = _f041_vol_range(volume, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v007: 10d volume range scaled by close
def f041vvc_f041_volume_volatility_compression_volrange_10d_base_v007_signal(closeadj, volume):
    result = _f041_vol_range(volume, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v008: 42d volume range scaled by close
def f041vvc_f041_volume_volatility_compression_volrange_42d_base_v008_signal(closeadj, volume):
    result = _f041_vol_range(volume, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v009: 189d volume range scaled by close
def f041vvc_f041_volume_volatility_compression_volrange_189d_base_v009_signal(closeadj, volume):
    result = _f041_vol_range(volume, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v010: 378d volume range scaled by close
def f041vvc_f041_volume_volatility_compression_volrange_378d_base_v010_signal(closeadj, volume):
    result = _f041_vol_range(volume, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v011: 21d vol compression × close
def f041vvc_f041_volume_volatility_compression_compress_21d_base_v011_signal(closeadj, volume):
    result = _f041_vol_vol_compression(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v012: 63d vol compression × close
def f041vvc_f041_volume_volatility_compression_compress_63d_base_v012_signal(closeadj, volume):
    result = _f041_vol_vol_compression(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v013: 126d vol compression × close
def f041vvc_f041_volume_volatility_compression_compress_126d_base_v013_signal(closeadj, volume):
    result = _f041_vol_vol_compression(volume, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v014: 252d vol compression × close
def f041vvc_f041_volume_volatility_compression_compress_252d_base_v014_signal(closeadj, volume):
    result = _f041_vol_vol_compression(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v015: 504d vol compression × close
def f041vvc_f041_volume_volatility_compression_compress_504d_base_v015_signal(closeadj, volume):
    result = _f041_vol_vol_compression(volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v016: 21d quiet accumulation
def f041vvc_f041_volume_volatility_compression_quietacc_21d_base_v016_signal(closeadj, volume):
    result = _f041_quiet_accumulation(closeadj, volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v017: 63d quiet accumulation
def f041vvc_f041_volume_volatility_compression_quietacc_63d_base_v017_signal(closeadj, volume):
    result = _f041_quiet_accumulation(closeadj, volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v018: 126d quiet accumulation
def f041vvc_f041_volume_volatility_compression_quietacc_126d_base_v018_signal(closeadj, volume):
    result = _f041_quiet_accumulation(closeadj, volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# v019: 252d quiet accumulation
def f041vvc_f041_volume_volatility_compression_quietacc_252d_base_v019_signal(closeadj, volume):
    result = _f041_quiet_accumulation(closeadj, volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v020: 504d quiet accumulation
def f041vvc_f041_volume_volatility_compression_quietacc_504d_base_v020_signal(closeadj, volume):
    result = _f041_quiet_accumulation(closeadj, volume, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v021: log volume range 21d × close
def f041vvc_f041_volume_volatility_compression_logvr_21d_base_v021_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21)
    result = np.log1p(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v022: log volume range 63d × close
def f041vvc_f041_volume_volatility_compression_logvr_63d_base_v022_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63)
    result = np.log1p(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v023: log volume range 252d × close
def f041vvc_f041_volume_volatility_compression_logvr_252d_base_v023_signal(closeadj, volume):
    base = _f041_vol_range(volume, 252)
    result = np.log1p(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v024: log volume range 504d × close
def f041vvc_f041_volume_volatility_compression_logvr_504d_base_v024_signal(closeadj, volume):
    base = _f041_vol_range(volume, 504)
    result = np.log1p(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v025: 21d z-score of vol compression × close
def f041vvc_f041_volume_volatility_compression_compressz_21d_base_v025_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v026: 63d z-score of vol compression × close
def f041vvc_f041_volume_volatility_compression_compressz_63d_base_v026_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v027: 252d z-score of vol compression × close
def f041vvc_f041_volume_volatility_compression_compressz_252d_base_v027_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v028: 21d compression × dollar volume
def f041vvc_f041_volume_volatility_compression_compressxdv_21d_base_v028_signal(closeadj, volume):
    result = _f041_vol_vol_compression(volume, 21) * (closeadj * volume)
    return result.replace([np.inf, -np.inf], np.nan)


# v029: 63d compression × dollar volume
def f041vvc_f041_volume_volatility_compression_compressxdv_63d_base_v029_signal(closeadj, volume):
    result = _f041_vol_vol_compression(volume, 63) * (closeadj * volume)
    return result.replace([np.inf, -np.inf], np.nan)


# v030: 252d compression × dollar volume
def f041vvc_f041_volume_volatility_compression_compressxdv_252d_base_v030_signal(closeadj, volume):
    result = _f041_vol_vol_compression(volume, 252) * (closeadj * volume)
    return result.replace([np.inf, -np.inf], np.nan)


# v031: 21d quiet acc × volume
def f041vvc_f041_volume_volatility_compression_quietaccxv_21d_base_v031_signal(closeadj, volume):
    result = _f041_quiet_accumulation(closeadj, volume, 21) * np.log1p(volume)
    return result.replace([np.inf, -np.inf], np.nan)


# v032: 63d quiet acc × volume
def f041vvc_f041_volume_volatility_compression_quietaccxv_63d_base_v032_signal(closeadj, volume):
    result = _f041_quiet_accumulation(closeadj, volume, 63) * np.log1p(volume)
    return result.replace([np.inf, -np.inf], np.nan)


# v033: 252d quiet acc × volume
def f041vvc_f041_volume_volatility_compression_quietaccxv_252d_base_v033_signal(closeadj, volume):
    result = _f041_quiet_accumulation(closeadj, volume, 252) * np.log1p(volume)
    return result.replace([np.inf, -np.inf], np.nan)


# v034: 21d range / mean (CV) × close
def f041vvc_f041_volume_volatility_compression_vrcv_21d_base_v034_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21)
    m = _mean(volume, 21)
    result = (base / m.replace(0, np.nan).abs()) * closeadj * m
    return result.replace([np.inf, -np.inf], np.nan)


# v035: 63d range / mean × close
def f041vvc_f041_volume_volatility_compression_vrcv_63d_base_v035_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63)
    m = _mean(volume, 63)
    result = (base / m.replace(0, np.nan).abs()) * closeadj * m
    return result.replace([np.inf, -np.inf], np.nan)


# v036: 252d range / mean × close
def f041vvc_f041_volume_volatility_compression_vrcv_252d_base_v036_signal(closeadj, volume):
    base = _f041_vol_range(volume, 252)
    m = _mean(volume, 252)
    result = (base / m.replace(0, np.nan).abs()) * closeadj * m
    return result.replace([np.inf, -np.inf], np.nan)


# v037: compression 21d × close × volume
def f041vvc_f041_volume_volatility_compression_compressxcv_21d_base_v037_signal(closeadj, volume):
    result = _f041_vol_vol_compression(volume, 21) * closeadj * np.log1p(volume)
    return result.replace([np.inf, -np.inf], np.nan)


# v038: compression 63d × close × volume
def f041vvc_f041_volume_volatility_compression_compressxcv_63d_base_v038_signal(closeadj, volume):
    result = _f041_vol_vol_compression(volume, 63) * closeadj * np.log1p(volume)
    return result.replace([np.inf, -np.inf], np.nan)


# v039: vol range × dollar volume
def f041vvc_f041_volume_volatility_compression_vrxdv_21d_base_v039_signal(closeadj, volume):
    result = _f041_vol_range(volume, 21) * (closeadj * volume)
    return result.replace([np.inf, -np.inf], np.nan)


# v040: vol range × dollar volume 63d
def f041vvc_f041_volume_volatility_compression_vrxdv_63d_base_v040_signal(closeadj, volume):
    result = _f041_vol_range(volume, 63) * (closeadj * volume)
    return result.replace([np.inf, -np.inf], np.nan)


# v041: vol range × dollar volume 252d
def f041vvc_f041_volume_volatility_compression_vrxdv_252d_base_v041_signal(closeadj, volume):
    result = _f041_vol_range(volume, 252) * (closeadj * volume)
    return result.replace([np.inf, -np.inf], np.nan)


# v042: compression × log close
def f041vvc_f041_volume_volatility_compression_compressxlc_21d_base_v042_signal(closeadj, volume):
    result = _f041_vol_vol_compression(volume, 21) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v043: compression × log close 63d
def f041vvc_f041_volume_volatility_compression_compressxlc_63d_base_v043_signal(closeadj, volume):
    result = _f041_vol_vol_compression(volume, 63) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v044: compression × log close 252d
def f041vvc_f041_volume_volatility_compression_compressxlc_252d_base_v044_signal(closeadj, volume):
    result = _f041_vol_vol_compression(volume, 252) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v045: 21d quiet acc × log close
def f041vvc_f041_volume_volatility_compression_quietaccxlc_21d_base_v045_signal(closeadj, volume):
    result = _f041_quiet_accumulation(closeadj, volume, 21) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# v046: 63d quiet acc × log close
def f041vvc_f041_volume_volatility_compression_quietaccxlc_63d_base_v046_signal(closeadj, volume):
    result = _f041_quiet_accumulation(closeadj, volume, 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# v047: 252d quiet acc × log close
def f041vvc_f041_volume_volatility_compression_quietaccxlc_252d_base_v047_signal(closeadj, volume):
    result = _f041_quiet_accumulation(closeadj, volume, 252) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# v048: 21d compression ratio 21vs63 × close
def f041vvc_f041_volume_volatility_compression_cmprtio_2163_base_v048_signal(closeadj, volume):
    a = _f041_vol_vol_compression(volume, 21)
    b = _f041_vol_vol_compression(volume, 63)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v049: compression ratio 63vs252 × close
def f041vvc_f041_volume_volatility_compression_cmprtio_63252_base_v049_signal(closeadj, volume):
    a = _f041_vol_vol_compression(volume, 63)
    b = _f041_vol_vol_compression(volume, 252)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v050: compression ratio 252vs504 × close
def f041vvc_f041_volume_volatility_compression_cmprtio_252504_base_v050_signal(closeadj, volume):
    a = _f041_vol_vol_compression(volume, 252)
    b = _f041_vol_vol_compression(volume, 504)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v051: 21d EMA of vol range × close
def f041vvc_f041_volume_volatility_compression_vrema_21d_base_v051_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v052: 63d EMA of vol range × close
def f041vvc_f041_volume_volatility_compression_vrema_63d_base_v052_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v053: 252d EMA of vol range × close
def f041vvc_f041_volume_volatility_compression_vrema_252d_base_v053_signal(closeadj, volume):
    base = _f041_vol_range(volume, 252)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v054: 21d EMA of vol compression × close
def f041vvc_f041_volume_volatility_compression_cmpema_21d_base_v054_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v055: 63d EMA of vol compression × close
def f041vvc_f041_volume_volatility_compression_cmpema_63d_base_v055_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v056: 252d EMA of vol compression × close
def f041vvc_f041_volume_volatility_compression_cmpema_252d_base_v056_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 252)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v057: 21d std of vol range × close
def f041vvc_f041_volume_volatility_compression_vrstd_21d_base_v057_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v058: 63d std of vol range × close
def f041vvc_f041_volume_volatility_compression_vrstd_63d_base_v058_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v059: 252d std of vol range × close
def f041vvc_f041_volume_volatility_compression_vrstd_252d_base_v059_signal(closeadj, volume):
    base = _f041_vol_range(volume, 252)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v060: 21d compression std × close
def f041vvc_f041_volume_volatility_compression_cmpstd_21d_base_v060_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v061: 63d compression std × close
def f041vvc_f041_volume_volatility_compression_cmpstd_63d_base_v061_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v062: 252d compression std × close
def f041vvc_f041_volume_volatility_compression_cmpstd_252d_base_v062_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 252)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v063: 21d sign of compression × close × volume
def f041vvc_f041_volume_volatility_compression_cmpsign_21d_base_v063_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21)
    avg = _mean(base, 63)
    result = np.sign(base - avg) * closeadj * np.log1p(volume)
    return result.replace([np.inf, -np.inf], np.nan)


# v064: 63d sign of compression × close × volume
def f041vvc_f041_volume_volatility_compression_cmpsign_63d_base_v064_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63)
    avg = _mean(base, 252)
    result = np.sign(base - avg) * closeadj * np.log1p(volume)
    return result.replace([np.inf, -np.inf], np.nan)


# v065: 21d quiet acc rank
def f041vvc_f041_volume_volatility_compression_quietrnk_21d_base_v065_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 21)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v066: 63d quiet acc rank
def f041vvc_f041_volume_volatility_compression_quietrnk_63d_base_v066_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 63)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v067: 252d quiet acc rank
def f041vvc_f041_volume_volatility_compression_quietrnk_252d_base_v067_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 252)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v068: 21d vol range × price range
def f041vvc_f041_volume_volatility_compression_vrxpr_21d_base_v068_signal(closeadj, volume):
    pr = (closeadj.rolling(21, min_periods=5).max() - closeadj.rolling(21, min_periods=5).min())
    result = _f041_vol_range(volume, 21) * pr
    return result.replace([np.inf, -np.inf], np.nan)


# v069: 63d vol range × price range
def f041vvc_f041_volume_volatility_compression_vrxpr_63d_base_v069_signal(closeadj, volume):
    pr = (closeadj.rolling(63, min_periods=21).max() - closeadj.rolling(63, min_periods=21).min())
    result = _f041_vol_range(volume, 63) * pr
    return result.replace([np.inf, -np.inf], np.nan)


# v070: 252d vol range × price range
def f041vvc_f041_volume_volatility_compression_vrxpr_252d_base_v070_signal(closeadj, volume):
    pr = (closeadj.rolling(252, min_periods=63).max() - closeadj.rolling(252, min_periods=63).min())
    result = _f041_vol_range(volume, 252) * pr
    return result.replace([np.inf, -np.inf], np.nan)


# v071: compression × abs return
def f041vvc_f041_volume_volatility_compression_cmpxabsret_21d_base_v071_signal(closeadj, volume):
    r = closeadj.pct_change().abs()
    result = _f041_vol_vol_compression(volume, 21) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v072: compression × abs return 63d
def f041vvc_f041_volume_volatility_compression_cmpxabsret_63d_base_v072_signal(closeadj, volume):
    r = closeadj.pct_change(periods=21).abs()
    result = _f041_vol_vol_compression(volume, 63) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v073: compression × abs return 252d
def f041vvc_f041_volume_volatility_compression_cmpxabsret_252d_base_v073_signal(closeadj, volume):
    r = closeadj.pct_change(periods=63).abs()
    result = _f041_vol_vol_compression(volume, 252) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v074: quiet acc × abs return 21d
def f041vvc_f041_volume_volatility_compression_quietxabsret_21d_base_v074_signal(closeadj, volume):
    r = closeadj.pct_change().abs()
    result = _f041_quiet_accumulation(closeadj, volume, 21) * r
    return result.replace([np.inf, -np.inf], np.nan)


# v075: quiet acc × abs return 63d
def f041vvc_f041_volume_volatility_compression_quietxabsret_63d_base_v075_signal(closeadj, volume):
    r = closeadj.pct_change(periods=21).abs()
    result = _f041_quiet_accumulation(closeadj, volume, 63) * r
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f041vvc_f041_volume_volatility_compression_volrange_21d_base_v001_signal,
    f041vvc_f041_volume_volatility_compression_volrange_63d_base_v002_signal,
    f041vvc_f041_volume_volatility_compression_volrange_126d_base_v003_signal,
    f041vvc_f041_volume_volatility_compression_volrange_252d_base_v004_signal,
    f041vvc_f041_volume_volatility_compression_volrange_504d_base_v005_signal,
    f041vvc_f041_volume_volatility_compression_volrange_5d_base_v006_signal,
    f041vvc_f041_volume_volatility_compression_volrange_10d_base_v007_signal,
    f041vvc_f041_volume_volatility_compression_volrange_42d_base_v008_signal,
    f041vvc_f041_volume_volatility_compression_volrange_189d_base_v009_signal,
    f041vvc_f041_volume_volatility_compression_volrange_378d_base_v010_signal,
    f041vvc_f041_volume_volatility_compression_compress_21d_base_v011_signal,
    f041vvc_f041_volume_volatility_compression_compress_63d_base_v012_signal,
    f041vvc_f041_volume_volatility_compression_compress_126d_base_v013_signal,
    f041vvc_f041_volume_volatility_compression_compress_252d_base_v014_signal,
    f041vvc_f041_volume_volatility_compression_compress_504d_base_v015_signal,
    f041vvc_f041_volume_volatility_compression_quietacc_21d_base_v016_signal,
    f041vvc_f041_volume_volatility_compression_quietacc_63d_base_v017_signal,
    f041vvc_f041_volume_volatility_compression_quietacc_126d_base_v018_signal,
    f041vvc_f041_volume_volatility_compression_quietacc_252d_base_v019_signal,
    f041vvc_f041_volume_volatility_compression_quietacc_504d_base_v020_signal,
    f041vvc_f041_volume_volatility_compression_logvr_21d_base_v021_signal,
    f041vvc_f041_volume_volatility_compression_logvr_63d_base_v022_signal,
    f041vvc_f041_volume_volatility_compression_logvr_252d_base_v023_signal,
    f041vvc_f041_volume_volatility_compression_logvr_504d_base_v024_signal,
    f041vvc_f041_volume_volatility_compression_compressz_21d_base_v025_signal,
    f041vvc_f041_volume_volatility_compression_compressz_63d_base_v026_signal,
    f041vvc_f041_volume_volatility_compression_compressz_252d_base_v027_signal,
    f041vvc_f041_volume_volatility_compression_compressxdv_21d_base_v028_signal,
    f041vvc_f041_volume_volatility_compression_compressxdv_63d_base_v029_signal,
    f041vvc_f041_volume_volatility_compression_compressxdv_252d_base_v030_signal,
    f041vvc_f041_volume_volatility_compression_quietaccxv_21d_base_v031_signal,
    f041vvc_f041_volume_volatility_compression_quietaccxv_63d_base_v032_signal,
    f041vvc_f041_volume_volatility_compression_quietaccxv_252d_base_v033_signal,
    f041vvc_f041_volume_volatility_compression_vrcv_21d_base_v034_signal,
    f041vvc_f041_volume_volatility_compression_vrcv_63d_base_v035_signal,
    f041vvc_f041_volume_volatility_compression_vrcv_252d_base_v036_signal,
    f041vvc_f041_volume_volatility_compression_compressxcv_21d_base_v037_signal,
    f041vvc_f041_volume_volatility_compression_compressxcv_63d_base_v038_signal,
    f041vvc_f041_volume_volatility_compression_vrxdv_21d_base_v039_signal,
    f041vvc_f041_volume_volatility_compression_vrxdv_63d_base_v040_signal,
    f041vvc_f041_volume_volatility_compression_vrxdv_252d_base_v041_signal,
    f041vvc_f041_volume_volatility_compression_compressxlc_21d_base_v042_signal,
    f041vvc_f041_volume_volatility_compression_compressxlc_63d_base_v043_signal,
    f041vvc_f041_volume_volatility_compression_compressxlc_252d_base_v044_signal,
    f041vvc_f041_volume_volatility_compression_quietaccxlc_21d_base_v045_signal,
    f041vvc_f041_volume_volatility_compression_quietaccxlc_63d_base_v046_signal,
    f041vvc_f041_volume_volatility_compression_quietaccxlc_252d_base_v047_signal,
    f041vvc_f041_volume_volatility_compression_cmprtio_2163_base_v048_signal,
    f041vvc_f041_volume_volatility_compression_cmprtio_63252_base_v049_signal,
    f041vvc_f041_volume_volatility_compression_cmprtio_252504_base_v050_signal,
    f041vvc_f041_volume_volatility_compression_vrema_21d_base_v051_signal,
    f041vvc_f041_volume_volatility_compression_vrema_63d_base_v052_signal,
    f041vvc_f041_volume_volatility_compression_vrema_252d_base_v053_signal,
    f041vvc_f041_volume_volatility_compression_cmpema_21d_base_v054_signal,
    f041vvc_f041_volume_volatility_compression_cmpema_63d_base_v055_signal,
    f041vvc_f041_volume_volatility_compression_cmpema_252d_base_v056_signal,
    f041vvc_f041_volume_volatility_compression_vrstd_21d_base_v057_signal,
    f041vvc_f041_volume_volatility_compression_vrstd_63d_base_v058_signal,
    f041vvc_f041_volume_volatility_compression_vrstd_252d_base_v059_signal,
    f041vvc_f041_volume_volatility_compression_cmpstd_21d_base_v060_signal,
    f041vvc_f041_volume_volatility_compression_cmpstd_63d_base_v061_signal,
    f041vvc_f041_volume_volatility_compression_cmpstd_252d_base_v062_signal,
    f041vvc_f041_volume_volatility_compression_cmpsign_21d_base_v063_signal,
    f041vvc_f041_volume_volatility_compression_cmpsign_63d_base_v064_signal,
    f041vvc_f041_volume_volatility_compression_quietrnk_21d_base_v065_signal,
    f041vvc_f041_volume_volatility_compression_quietrnk_63d_base_v066_signal,
    f041vvc_f041_volume_volatility_compression_quietrnk_252d_base_v067_signal,
    f041vvc_f041_volume_volatility_compression_vrxpr_21d_base_v068_signal,
    f041vvc_f041_volume_volatility_compression_vrxpr_63d_base_v069_signal,
    f041vvc_f041_volume_volatility_compression_vrxpr_252d_base_v070_signal,
    f041vvc_f041_volume_volatility_compression_cmpxabsret_21d_base_v071_signal,
    f041vvc_f041_volume_volatility_compression_cmpxabsret_63d_base_v072_signal,
    f041vvc_f041_volume_volatility_compression_cmpxabsret_252d_base_v073_signal,
    f041vvc_f041_volume_volatility_compression_quietxabsret_21d_base_v074_signal,
    f041vvc_f041_volume_volatility_compression_quietxabsret_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F041_VOLUME_VOLATILITY_COMPRESSION_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f041_vol_range", "_f041_vol_vol_compression", "_f041_quiet_accumulation")
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
    print(f"OK f041_volume_volatility_compression_base_001_075_claude: {n_features} features pass")
