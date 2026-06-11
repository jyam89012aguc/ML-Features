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


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


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


def f041vvc_f041_volume_volatility_compression_volrange21x_5d_jerk_v001_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_volrange21x_10d_jerk_v002_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_volrange21x_21d_jerk_v003_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_volrange21x_42d_jerk_v004_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_volrange21x_63d_jerk_v005_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_volrange21x_126d_jerk_v006_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_volrange63x_5d_jerk_v007_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_volrange63x_10d_jerk_v008_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_volrange63x_21d_jerk_v009_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_volrange63x_42d_jerk_v010_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_volrange63x_63d_jerk_v011_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_volrange63x_126d_jerk_v012_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_volrange126x_5d_jerk_v013_signal(closeadj, volume):
    base = _f041_vol_range(volume, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_volrange126x_10d_jerk_v014_signal(closeadj, volume):
    base = _f041_vol_range(volume, 126) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_volrange126x_21d_jerk_v015_signal(closeadj, volume):
    base = _f041_vol_range(volume, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_volrange126x_42d_jerk_v016_signal(closeadj, volume):
    base = _f041_vol_range(volume, 126) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_volrange126x_63d_jerk_v017_signal(closeadj, volume):
    base = _f041_vol_range(volume, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_volrange126x_126d_jerk_v018_signal(closeadj, volume):
    base = _f041_vol_range(volume, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_volrange252x_5d_jerk_v019_signal(closeadj, volume):
    base = _f041_vol_range(volume, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_volrange252x_10d_jerk_v020_signal(closeadj, volume):
    base = _f041_vol_range(volume, 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_volrange252x_21d_jerk_v021_signal(closeadj, volume):
    base = _f041_vol_range(volume, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_volrange252x_42d_jerk_v022_signal(closeadj, volume):
    base = _f041_vol_range(volume, 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_volrange252x_63d_jerk_v023_signal(closeadj, volume):
    base = _f041_vol_range(volume, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_volrange252x_126d_jerk_v024_signal(closeadj, volume):
    base = _f041_vol_range(volume, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_compress21x_5d_jerk_v025_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_compress21x_10d_jerk_v026_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_compress21x_21d_jerk_v027_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_compress21x_42d_jerk_v028_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_compress21x_63d_jerk_v029_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_compress21x_126d_jerk_v030_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_compress63x_5d_jerk_v031_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_compress63x_10d_jerk_v032_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_compress63x_21d_jerk_v033_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_compress63x_42d_jerk_v034_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_compress63x_63d_jerk_v035_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_compress63x_126d_jerk_v036_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_compress126x_5d_jerk_v037_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_compress126x_10d_jerk_v038_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 126) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_compress126x_21d_jerk_v039_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_compress126x_42d_jerk_v040_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 126) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_compress126x_63d_jerk_v041_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_compress126x_126d_jerk_v042_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_compress252x_5d_jerk_v043_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_compress252x_10d_jerk_v044_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_compress252x_21d_jerk_v045_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_compress252x_42d_jerk_v046_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_compress252x_63d_jerk_v047_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_compress252x_126d_jerk_v048_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietacc21_5d_jerk_v049_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietacc21_10d_jerk_v050_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietacc21_21d_jerk_v051_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietacc21_42d_jerk_v052_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietacc21_63d_jerk_v053_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietacc21_126d_jerk_v054_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietacc63_5d_jerk_v055_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietacc63_10d_jerk_v056_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietacc63_21d_jerk_v057_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietacc63_42d_jerk_v058_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietacc63_63d_jerk_v059_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietacc63_126d_jerk_v060_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietacc126_5d_jerk_v061_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietacc126_10d_jerk_v062_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietacc126_21d_jerk_v063_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietacc126_42d_jerk_v064_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 126)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietacc126_63d_jerk_v065_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietacc126_126d_jerk_v066_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 126)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietacc252_5d_jerk_v067_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietacc252_10d_jerk_v068_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietacc252_21d_jerk_v069_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietacc252_42d_jerk_v070_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietacc252_63d_jerk_v071_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietacc252_126d_jerk_v072_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_logvr21x_5d_jerk_v073_signal(closeadj, volume):
    base = np.log1p(_f041_vol_range(volume, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_logvr21x_10d_jerk_v074_signal(closeadj, volume):
    base = np.log1p(_f041_vol_range(volume, 21)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_logvr21x_21d_jerk_v075_signal(closeadj, volume):
    base = np.log1p(_f041_vol_range(volume, 21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_logvr21x_42d_jerk_v076_signal(closeadj, volume):
    base = np.log1p(_f041_vol_range(volume, 21)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_logvr21x_63d_jerk_v077_signal(closeadj, volume):
    base = np.log1p(_f041_vol_range(volume, 21)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_logvr21x_126d_jerk_v078_signal(closeadj, volume):
    base = np.log1p(_f041_vol_range(volume, 21)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_logvr63x_5d_jerk_v079_signal(closeadj, volume):
    base = np.log1p(_f041_vol_range(volume, 63)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_logvr63x_10d_jerk_v080_signal(closeadj, volume):
    base = np.log1p(_f041_vol_range(volume, 63)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_logvr63x_21d_jerk_v081_signal(closeadj, volume):
    base = np.log1p(_f041_vol_range(volume, 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_logvr63x_42d_jerk_v082_signal(closeadj, volume):
    base = np.log1p(_f041_vol_range(volume, 63)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_logvr63x_63d_jerk_v083_signal(closeadj, volume):
    base = np.log1p(_f041_vol_range(volume, 63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_logvr63x_126d_jerk_v084_signal(closeadj, volume):
    base = np.log1p(_f041_vol_range(volume, 63)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_logvr252x_5d_jerk_v085_signal(closeadj, volume):
    base = np.log1p(_f041_vol_range(volume, 252)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_logvr252x_10d_jerk_v086_signal(closeadj, volume):
    base = np.log1p(_f041_vol_range(volume, 252)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_logvr252x_21d_jerk_v087_signal(closeadj, volume):
    base = np.log1p(_f041_vol_range(volume, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_logvr252x_42d_jerk_v088_signal(closeadj, volume):
    base = np.log1p(_f041_vol_range(volume, 252)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_logvr252x_63d_jerk_v089_signal(closeadj, volume):
    base = np.log1p(_f041_vol_range(volume, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_logvr252x_126d_jerk_v090_signal(closeadj, volume):
    base = np.log1p(_f041_vol_range(volume, 252)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_cmpxdv21_5d_jerk_v091_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21) * (closeadj * volume)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_cmpxdv21_10d_jerk_v092_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21) * (closeadj * volume)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_cmpxdv21_21d_jerk_v093_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21) * (closeadj * volume)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_cmpxdv21_42d_jerk_v094_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21) * (closeadj * volume)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_cmpxdv21_63d_jerk_v095_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21) * (closeadj * volume)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_cmpxdv21_126d_jerk_v096_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21) * (closeadj * volume)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_cmpxdv63_5d_jerk_v097_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63) * (closeadj * volume)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_cmpxdv63_10d_jerk_v098_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63) * (closeadj * volume)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_cmpxdv63_21d_jerk_v099_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63) * (closeadj * volume)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_cmpxdv63_42d_jerk_v100_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63) * (closeadj * volume)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_cmpxdv63_63d_jerk_v101_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63) * (closeadj * volume)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_cmpxdv63_126d_jerk_v102_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63) * (closeadj * volume)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_vrxdv21_5d_jerk_v103_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21) * (closeadj * volume)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_vrxdv21_10d_jerk_v104_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21) * (closeadj * volume)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_vrxdv21_21d_jerk_v105_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21) * (closeadj * volume)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_vrxdv21_42d_jerk_v106_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21) * (closeadj * volume)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_vrxdv21_63d_jerk_v107_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21) * (closeadj * volume)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_vrxdv21_126d_jerk_v108_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21) * (closeadj * volume)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_vrxdv63_5d_jerk_v109_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63) * (closeadj * volume)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_vrxdv63_10d_jerk_v110_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63) * (closeadj * volume)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_vrxdv63_21d_jerk_v111_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63) * (closeadj * volume)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_vrxdv63_42d_jerk_v112_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63) * (closeadj * volume)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_vrxdv63_63d_jerk_v113_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63) * (closeadj * volume)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_vrxdv63_126d_jerk_v114_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63) * (closeadj * volume)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_cmpxlc21_5d_jerk_v115_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_cmpxlc21_10d_jerk_v116_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_cmpxlc21_21d_jerk_v117_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_cmpxlc21_42d_jerk_v118_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_cmpxlc21_63d_jerk_v119_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_cmpxlc21_126d_jerk_v120_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 21) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_cmpxlc63_5d_jerk_v121_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_cmpxlc63_10d_jerk_v122_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_cmpxlc63_21d_jerk_v123_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_cmpxlc63_42d_jerk_v124_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_cmpxlc63_63d_jerk_v125_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_cmpxlc63_126d_jerk_v126_signal(closeadj, volume):
    base = _f041_vol_vol_compression(volume, 63) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_vrxlc21_5d_jerk_v127_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_vrxlc21_10d_jerk_v128_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_vrxlc21_21d_jerk_v129_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_vrxlc21_42d_jerk_v130_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_vrxlc21_63d_jerk_v131_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_vrxlc21_126d_jerk_v132_signal(closeadj, volume):
    base = _f041_vol_range(volume, 21) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_vrxlc63_5d_jerk_v133_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_vrxlc63_10d_jerk_v134_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_vrxlc63_21d_jerk_v135_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_vrxlc63_42d_jerk_v136_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_vrxlc63_63d_jerk_v137_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_vrxlc63_126d_jerk_v138_signal(closeadj, volume):
    base = _f041_vol_range(volume, 63) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietxlc21_5d_jerk_v139_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 21) * np.log(closeadj.replace(0, np.nan).abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietxlc21_10d_jerk_v140_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 21) * np.log(closeadj.replace(0, np.nan).abs())
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietxlc21_21d_jerk_v141_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 21) * np.log(closeadj.replace(0, np.nan).abs())
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietxlc21_42d_jerk_v142_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 21) * np.log(closeadj.replace(0, np.nan).abs())
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietxlc21_63d_jerk_v143_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 21) * np.log(closeadj.replace(0, np.nan).abs())
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietxlc21_126d_jerk_v144_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 21) * np.log(closeadj.replace(0, np.nan).abs())
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietxlc63_5d_jerk_v145_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 63) * np.log(closeadj.replace(0, np.nan).abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietxlc63_10d_jerk_v146_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 63) * np.log(closeadj.replace(0, np.nan).abs())
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietxlc63_21d_jerk_v147_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 63) * np.log(closeadj.replace(0, np.nan).abs())
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietxlc63_42d_jerk_v148_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 63) * np.log(closeadj.replace(0, np.nan).abs())
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietxlc63_63d_jerk_v149_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 63) * np.log(closeadj.replace(0, np.nan).abs())
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f041vvc_f041_volume_volatility_compression_quietxlc63_126d_jerk_v150_signal(closeadj, volume):
    base = _f041_quiet_accumulation(closeadj, volume, 63) * np.log(closeadj.replace(0, np.nan).abs())
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f041vvc_f041_volume_volatility_compression_volrange21x_5d_jerk_v001_signal,
    f041vvc_f041_volume_volatility_compression_volrange21x_10d_jerk_v002_signal,
    f041vvc_f041_volume_volatility_compression_volrange21x_21d_jerk_v003_signal,
    f041vvc_f041_volume_volatility_compression_volrange21x_42d_jerk_v004_signal,
    f041vvc_f041_volume_volatility_compression_volrange21x_63d_jerk_v005_signal,
    f041vvc_f041_volume_volatility_compression_volrange21x_126d_jerk_v006_signal,
    f041vvc_f041_volume_volatility_compression_volrange63x_5d_jerk_v007_signal,
    f041vvc_f041_volume_volatility_compression_volrange63x_10d_jerk_v008_signal,
    f041vvc_f041_volume_volatility_compression_volrange63x_21d_jerk_v009_signal,
    f041vvc_f041_volume_volatility_compression_volrange63x_42d_jerk_v010_signal,
    f041vvc_f041_volume_volatility_compression_volrange63x_63d_jerk_v011_signal,
    f041vvc_f041_volume_volatility_compression_volrange63x_126d_jerk_v012_signal,
    f041vvc_f041_volume_volatility_compression_volrange126x_5d_jerk_v013_signal,
    f041vvc_f041_volume_volatility_compression_volrange126x_10d_jerk_v014_signal,
    f041vvc_f041_volume_volatility_compression_volrange126x_21d_jerk_v015_signal,
    f041vvc_f041_volume_volatility_compression_volrange126x_42d_jerk_v016_signal,
    f041vvc_f041_volume_volatility_compression_volrange126x_63d_jerk_v017_signal,
    f041vvc_f041_volume_volatility_compression_volrange126x_126d_jerk_v018_signal,
    f041vvc_f041_volume_volatility_compression_volrange252x_5d_jerk_v019_signal,
    f041vvc_f041_volume_volatility_compression_volrange252x_10d_jerk_v020_signal,
    f041vvc_f041_volume_volatility_compression_volrange252x_21d_jerk_v021_signal,
    f041vvc_f041_volume_volatility_compression_volrange252x_42d_jerk_v022_signal,
    f041vvc_f041_volume_volatility_compression_volrange252x_63d_jerk_v023_signal,
    f041vvc_f041_volume_volatility_compression_volrange252x_126d_jerk_v024_signal,
    f041vvc_f041_volume_volatility_compression_compress21x_5d_jerk_v025_signal,
    f041vvc_f041_volume_volatility_compression_compress21x_10d_jerk_v026_signal,
    f041vvc_f041_volume_volatility_compression_compress21x_21d_jerk_v027_signal,
    f041vvc_f041_volume_volatility_compression_compress21x_42d_jerk_v028_signal,
    f041vvc_f041_volume_volatility_compression_compress21x_63d_jerk_v029_signal,
    f041vvc_f041_volume_volatility_compression_compress21x_126d_jerk_v030_signal,
    f041vvc_f041_volume_volatility_compression_compress63x_5d_jerk_v031_signal,
    f041vvc_f041_volume_volatility_compression_compress63x_10d_jerk_v032_signal,
    f041vvc_f041_volume_volatility_compression_compress63x_21d_jerk_v033_signal,
    f041vvc_f041_volume_volatility_compression_compress63x_42d_jerk_v034_signal,
    f041vvc_f041_volume_volatility_compression_compress63x_63d_jerk_v035_signal,
    f041vvc_f041_volume_volatility_compression_compress63x_126d_jerk_v036_signal,
    f041vvc_f041_volume_volatility_compression_compress126x_5d_jerk_v037_signal,
    f041vvc_f041_volume_volatility_compression_compress126x_10d_jerk_v038_signal,
    f041vvc_f041_volume_volatility_compression_compress126x_21d_jerk_v039_signal,
    f041vvc_f041_volume_volatility_compression_compress126x_42d_jerk_v040_signal,
    f041vvc_f041_volume_volatility_compression_compress126x_63d_jerk_v041_signal,
    f041vvc_f041_volume_volatility_compression_compress126x_126d_jerk_v042_signal,
    f041vvc_f041_volume_volatility_compression_compress252x_5d_jerk_v043_signal,
    f041vvc_f041_volume_volatility_compression_compress252x_10d_jerk_v044_signal,
    f041vvc_f041_volume_volatility_compression_compress252x_21d_jerk_v045_signal,
    f041vvc_f041_volume_volatility_compression_compress252x_42d_jerk_v046_signal,
    f041vvc_f041_volume_volatility_compression_compress252x_63d_jerk_v047_signal,
    f041vvc_f041_volume_volatility_compression_compress252x_126d_jerk_v048_signal,
    f041vvc_f041_volume_volatility_compression_quietacc21_5d_jerk_v049_signal,
    f041vvc_f041_volume_volatility_compression_quietacc21_10d_jerk_v050_signal,
    f041vvc_f041_volume_volatility_compression_quietacc21_21d_jerk_v051_signal,
    f041vvc_f041_volume_volatility_compression_quietacc21_42d_jerk_v052_signal,
    f041vvc_f041_volume_volatility_compression_quietacc21_63d_jerk_v053_signal,
    f041vvc_f041_volume_volatility_compression_quietacc21_126d_jerk_v054_signal,
    f041vvc_f041_volume_volatility_compression_quietacc63_5d_jerk_v055_signal,
    f041vvc_f041_volume_volatility_compression_quietacc63_10d_jerk_v056_signal,
    f041vvc_f041_volume_volatility_compression_quietacc63_21d_jerk_v057_signal,
    f041vvc_f041_volume_volatility_compression_quietacc63_42d_jerk_v058_signal,
    f041vvc_f041_volume_volatility_compression_quietacc63_63d_jerk_v059_signal,
    f041vvc_f041_volume_volatility_compression_quietacc63_126d_jerk_v060_signal,
    f041vvc_f041_volume_volatility_compression_quietacc126_5d_jerk_v061_signal,
    f041vvc_f041_volume_volatility_compression_quietacc126_10d_jerk_v062_signal,
    f041vvc_f041_volume_volatility_compression_quietacc126_21d_jerk_v063_signal,
    f041vvc_f041_volume_volatility_compression_quietacc126_42d_jerk_v064_signal,
    f041vvc_f041_volume_volatility_compression_quietacc126_63d_jerk_v065_signal,
    f041vvc_f041_volume_volatility_compression_quietacc126_126d_jerk_v066_signal,
    f041vvc_f041_volume_volatility_compression_quietacc252_5d_jerk_v067_signal,
    f041vvc_f041_volume_volatility_compression_quietacc252_10d_jerk_v068_signal,
    f041vvc_f041_volume_volatility_compression_quietacc252_21d_jerk_v069_signal,
    f041vvc_f041_volume_volatility_compression_quietacc252_42d_jerk_v070_signal,
    f041vvc_f041_volume_volatility_compression_quietacc252_63d_jerk_v071_signal,
    f041vvc_f041_volume_volatility_compression_quietacc252_126d_jerk_v072_signal,
    f041vvc_f041_volume_volatility_compression_logvr21x_5d_jerk_v073_signal,
    f041vvc_f041_volume_volatility_compression_logvr21x_10d_jerk_v074_signal,
    f041vvc_f041_volume_volatility_compression_logvr21x_21d_jerk_v075_signal,
    f041vvc_f041_volume_volatility_compression_logvr21x_42d_jerk_v076_signal,
    f041vvc_f041_volume_volatility_compression_logvr21x_63d_jerk_v077_signal,
    f041vvc_f041_volume_volatility_compression_logvr21x_126d_jerk_v078_signal,
    f041vvc_f041_volume_volatility_compression_logvr63x_5d_jerk_v079_signal,
    f041vvc_f041_volume_volatility_compression_logvr63x_10d_jerk_v080_signal,
    f041vvc_f041_volume_volatility_compression_logvr63x_21d_jerk_v081_signal,
    f041vvc_f041_volume_volatility_compression_logvr63x_42d_jerk_v082_signal,
    f041vvc_f041_volume_volatility_compression_logvr63x_63d_jerk_v083_signal,
    f041vvc_f041_volume_volatility_compression_logvr63x_126d_jerk_v084_signal,
    f041vvc_f041_volume_volatility_compression_logvr252x_5d_jerk_v085_signal,
    f041vvc_f041_volume_volatility_compression_logvr252x_10d_jerk_v086_signal,
    f041vvc_f041_volume_volatility_compression_logvr252x_21d_jerk_v087_signal,
    f041vvc_f041_volume_volatility_compression_logvr252x_42d_jerk_v088_signal,
    f041vvc_f041_volume_volatility_compression_logvr252x_63d_jerk_v089_signal,
    f041vvc_f041_volume_volatility_compression_logvr252x_126d_jerk_v090_signal,
    f041vvc_f041_volume_volatility_compression_cmpxdv21_5d_jerk_v091_signal,
    f041vvc_f041_volume_volatility_compression_cmpxdv21_10d_jerk_v092_signal,
    f041vvc_f041_volume_volatility_compression_cmpxdv21_21d_jerk_v093_signal,
    f041vvc_f041_volume_volatility_compression_cmpxdv21_42d_jerk_v094_signal,
    f041vvc_f041_volume_volatility_compression_cmpxdv21_63d_jerk_v095_signal,
    f041vvc_f041_volume_volatility_compression_cmpxdv21_126d_jerk_v096_signal,
    f041vvc_f041_volume_volatility_compression_cmpxdv63_5d_jerk_v097_signal,
    f041vvc_f041_volume_volatility_compression_cmpxdv63_10d_jerk_v098_signal,
    f041vvc_f041_volume_volatility_compression_cmpxdv63_21d_jerk_v099_signal,
    f041vvc_f041_volume_volatility_compression_cmpxdv63_42d_jerk_v100_signal,
    f041vvc_f041_volume_volatility_compression_cmpxdv63_63d_jerk_v101_signal,
    f041vvc_f041_volume_volatility_compression_cmpxdv63_126d_jerk_v102_signal,
    f041vvc_f041_volume_volatility_compression_vrxdv21_5d_jerk_v103_signal,
    f041vvc_f041_volume_volatility_compression_vrxdv21_10d_jerk_v104_signal,
    f041vvc_f041_volume_volatility_compression_vrxdv21_21d_jerk_v105_signal,
    f041vvc_f041_volume_volatility_compression_vrxdv21_42d_jerk_v106_signal,
    f041vvc_f041_volume_volatility_compression_vrxdv21_63d_jerk_v107_signal,
    f041vvc_f041_volume_volatility_compression_vrxdv21_126d_jerk_v108_signal,
    f041vvc_f041_volume_volatility_compression_vrxdv63_5d_jerk_v109_signal,
    f041vvc_f041_volume_volatility_compression_vrxdv63_10d_jerk_v110_signal,
    f041vvc_f041_volume_volatility_compression_vrxdv63_21d_jerk_v111_signal,
    f041vvc_f041_volume_volatility_compression_vrxdv63_42d_jerk_v112_signal,
    f041vvc_f041_volume_volatility_compression_vrxdv63_63d_jerk_v113_signal,
    f041vvc_f041_volume_volatility_compression_vrxdv63_126d_jerk_v114_signal,
    f041vvc_f041_volume_volatility_compression_cmpxlc21_5d_jerk_v115_signal,
    f041vvc_f041_volume_volatility_compression_cmpxlc21_10d_jerk_v116_signal,
    f041vvc_f041_volume_volatility_compression_cmpxlc21_21d_jerk_v117_signal,
    f041vvc_f041_volume_volatility_compression_cmpxlc21_42d_jerk_v118_signal,
    f041vvc_f041_volume_volatility_compression_cmpxlc21_63d_jerk_v119_signal,
    f041vvc_f041_volume_volatility_compression_cmpxlc21_126d_jerk_v120_signal,
    f041vvc_f041_volume_volatility_compression_cmpxlc63_5d_jerk_v121_signal,
    f041vvc_f041_volume_volatility_compression_cmpxlc63_10d_jerk_v122_signal,
    f041vvc_f041_volume_volatility_compression_cmpxlc63_21d_jerk_v123_signal,
    f041vvc_f041_volume_volatility_compression_cmpxlc63_42d_jerk_v124_signal,
    f041vvc_f041_volume_volatility_compression_cmpxlc63_63d_jerk_v125_signal,
    f041vvc_f041_volume_volatility_compression_cmpxlc63_126d_jerk_v126_signal,
    f041vvc_f041_volume_volatility_compression_vrxlc21_5d_jerk_v127_signal,
    f041vvc_f041_volume_volatility_compression_vrxlc21_10d_jerk_v128_signal,
    f041vvc_f041_volume_volatility_compression_vrxlc21_21d_jerk_v129_signal,
    f041vvc_f041_volume_volatility_compression_vrxlc21_42d_jerk_v130_signal,
    f041vvc_f041_volume_volatility_compression_vrxlc21_63d_jerk_v131_signal,
    f041vvc_f041_volume_volatility_compression_vrxlc21_126d_jerk_v132_signal,
    f041vvc_f041_volume_volatility_compression_vrxlc63_5d_jerk_v133_signal,
    f041vvc_f041_volume_volatility_compression_vrxlc63_10d_jerk_v134_signal,
    f041vvc_f041_volume_volatility_compression_vrxlc63_21d_jerk_v135_signal,
    f041vvc_f041_volume_volatility_compression_vrxlc63_42d_jerk_v136_signal,
    f041vvc_f041_volume_volatility_compression_vrxlc63_63d_jerk_v137_signal,
    f041vvc_f041_volume_volatility_compression_vrxlc63_126d_jerk_v138_signal,
    f041vvc_f041_volume_volatility_compression_quietxlc21_5d_jerk_v139_signal,
    f041vvc_f041_volume_volatility_compression_quietxlc21_10d_jerk_v140_signal,
    f041vvc_f041_volume_volatility_compression_quietxlc21_21d_jerk_v141_signal,
    f041vvc_f041_volume_volatility_compression_quietxlc21_42d_jerk_v142_signal,
    f041vvc_f041_volume_volatility_compression_quietxlc21_63d_jerk_v143_signal,
    f041vvc_f041_volume_volatility_compression_quietxlc21_126d_jerk_v144_signal,
    f041vvc_f041_volume_volatility_compression_quietxlc63_5d_jerk_v145_signal,
    f041vvc_f041_volume_volatility_compression_quietxlc63_10d_jerk_v146_signal,
    f041vvc_f041_volume_volatility_compression_quietxlc63_21d_jerk_v147_signal,
    f041vvc_f041_volume_volatility_compression_quietxlc63_42d_jerk_v148_signal,
    f041vvc_f041_volume_volatility_compression_quietxlc63_63d_jerk_v149_signal,
    f041vvc_f041_volume_volatility_compression_quietxlc63_126d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F041_VOLUME_VOLATILITY_COMPRESSION_REGISTRY_JERK_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK {__file__}: {n_features} features pass")
