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


def _f027_parkinson(high, low, w):
    hi = high.replace(0, np.nan).abs()
    lo = low.replace(0, np.nan).abs()
    lr = np.log(hi / lo)
    sq = (lr * lr) / (4.0 * np.log(2.0))
    return sq.rolling(w, min_periods=max(1, w // 2)).mean().pow(0.5)


def _f027_garman_klass(high, low, closeadj, w):
    hi = high.replace(0, np.nan).abs()
    lo = low.replace(0, np.nan).abs()
    cl = closeadj.replace(0, np.nan).abs()
    op = cl.shift(1).replace(0, np.nan)
    lr_hl = np.log(hi / lo)
    lr_co = np.log(cl / op)
    val = 0.5 * lr_hl * lr_hl - (2.0 * np.log(2.0) - 1.0) * lr_co * lr_co
    return val.rolling(w, min_periods=max(1, w // 2)).mean().clip(lower=0).pow(0.5)


def _f027_hl_vol_compress(high, low, w):
    rng = (high - low).abs()
    short_std = rng.rolling(max(2, w // 4), min_periods=1).std()
    long_std = rng.rolling(w, min_periods=max(1, w // 2)).std()
    return short_std / long_std.replace(0, np.nan)


def f027pgv_f027_parkinson_garman_klass_vol_parkinsonraw_5d_base_v001_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 5)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklassraw_5d_base_v002_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompressraw_5d_base_v003_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonraw_10d_base_v004_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 10)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklassraw_10d_base_v005_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompressraw_10d_base_v006_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonraw_21d_base_v007_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 21)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklassraw_21d_base_v008_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompressraw_21d_base_v009_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonraw_42d_base_v010_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 42)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklassraw_42d_base_v011_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompressraw_42d_base_v012_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonraw_63d_base_v013_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 63)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklassraw_63d_base_v014_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompressraw_63d_base_v015_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonraw_126d_base_v016_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 126)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklassraw_126d_base_v017_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompressraw_126d_base_v018_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonraw_189d_base_v019_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 189)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklassraw_189d_base_v020_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompressraw_189d_base_v021_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonraw_252d_base_v022_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 252)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklassraw_252d_base_v023_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompressraw_252d_base_v024_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonraw_378d_base_v025_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 378)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklassraw_378d_base_v026_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompressraw_378d_base_v027_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonraw_504d_base_v028_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 504)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklassraw_504d_base_v029_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompressraw_504d_base_v030_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonabs_5d_base_v031_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 5)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklassabs_5d_base_v032_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompressabs_5d_base_v033_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonabs_10d_base_v034_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 10)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklassabs_10d_base_v035_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompressabs_10d_base_v036_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonabs_21d_base_v037_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 21)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklassabs_21d_base_v038_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompressabs_21d_base_v039_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonabs_42d_base_v040_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 42)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklassabs_42d_base_v041_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompressabs_42d_base_v042_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonabs_63d_base_v043_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 63)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklassabs_63d_base_v044_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompressabs_63d_base_v045_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonabs_126d_base_v046_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 126)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklassabs_126d_base_v047_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompressabs_126d_base_v048_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonabs_189d_base_v049_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 189)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklassabs_189d_base_v050_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompressabs_189d_base_v051_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonabs_252d_base_v052_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 252)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklassabs_252d_base_v053_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompressabs_252d_base_v054_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonabs_378d_base_v055_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 378)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklassabs_378d_base_v056_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompressabs_378d_base_v057_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonabs_504d_base_v058_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 504)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklassabs_504d_base_v059_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompressabs_504d_base_v060_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonsqrt_5d_base_v061_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 5)
    result = np.tanh(_z(base, 63)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklasssqrt_5d_base_v062_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompresssqrt_5d_base_v063_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonsqrt_10d_base_v064_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 10)
    result = np.tanh(_z(base, 63)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklasssqrt_10d_base_v065_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompresssqrt_10d_base_v066_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonsqrt_21d_base_v067_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 21)
    result = np.tanh(_z(base, 63)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklasssqrt_21d_base_v068_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompresssqrt_21d_base_v069_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonsqrt_42d_base_v070_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 42)
    result = np.tanh(_z(base, 63)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklasssqrt_42d_base_v071_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompresssqrt_42d_base_v072_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_parkinsonsqrt_63d_base_v073_signal(high, low, closeadj):
    base = _f027_parkinson(high, low, 63)
    result = np.tanh(_z(base, 63)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_garmanklasssqrt_63d_base_v074_signal(high, low, closeadj):
    base = _f027_garman_klass(high, low, closeadj, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f027pgv_f027_parkinson_garman_klass_vol_hlcompresssqrt_63d_base_v075_signal(high, low, closeadj):
    base = _f027_hl_vol_compress(high, low, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonraw_5d_base_v001_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklassraw_5d_base_v002_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompressraw_5d_base_v003_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonraw_10d_base_v004_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklassraw_10d_base_v005_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompressraw_10d_base_v006_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonraw_21d_base_v007_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklassraw_21d_base_v008_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompressraw_21d_base_v009_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonraw_42d_base_v010_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklassraw_42d_base_v011_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompressraw_42d_base_v012_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonraw_63d_base_v013_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklassraw_63d_base_v014_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompressraw_63d_base_v015_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonraw_126d_base_v016_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklassraw_126d_base_v017_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompressraw_126d_base_v018_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonraw_189d_base_v019_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklassraw_189d_base_v020_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompressraw_189d_base_v021_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonraw_252d_base_v022_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklassraw_252d_base_v023_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompressraw_252d_base_v024_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonraw_378d_base_v025_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklassraw_378d_base_v026_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompressraw_378d_base_v027_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonraw_504d_base_v028_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklassraw_504d_base_v029_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompressraw_504d_base_v030_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonabs_5d_base_v031_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklassabs_5d_base_v032_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompressabs_5d_base_v033_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonabs_10d_base_v034_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklassabs_10d_base_v035_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompressabs_10d_base_v036_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonabs_21d_base_v037_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklassabs_21d_base_v038_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompressabs_21d_base_v039_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonabs_42d_base_v040_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklassabs_42d_base_v041_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompressabs_42d_base_v042_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonabs_63d_base_v043_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklassabs_63d_base_v044_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompressabs_63d_base_v045_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonabs_126d_base_v046_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklassabs_126d_base_v047_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompressabs_126d_base_v048_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonabs_189d_base_v049_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklassabs_189d_base_v050_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompressabs_189d_base_v051_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonabs_252d_base_v052_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklassabs_252d_base_v053_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompressabs_252d_base_v054_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonabs_378d_base_v055_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklassabs_378d_base_v056_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompressabs_378d_base_v057_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonabs_504d_base_v058_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklassabs_504d_base_v059_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompressabs_504d_base_v060_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonsqrt_5d_base_v061_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklasssqrt_5d_base_v062_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompresssqrt_5d_base_v063_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonsqrt_10d_base_v064_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklasssqrt_10d_base_v065_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompresssqrt_10d_base_v066_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonsqrt_21d_base_v067_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklasssqrt_21d_base_v068_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompresssqrt_21d_base_v069_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonsqrt_42d_base_v070_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklasssqrt_42d_base_v071_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompresssqrt_42d_base_v072_signal,
    f027pgv_f027_parkinson_garman_klass_vol_parkinsonsqrt_63d_base_v073_signal,
    f027pgv_f027_parkinson_garman_klass_vol_garmanklasssqrt_63d_base_v074_signal,
    f027pgv_f027_parkinson_garman_klass_vol_hlcompresssqrt_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F027_PARKINSON_GARMAN_KLASS_VOL_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ('_f027_parkinson', '_f027_garman_klass', '_f027_hl_vol_compress')
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
    print(f"OK f027_parkinson_garman_klass_vol_base_001_075_claude: {n_features} features pass")
