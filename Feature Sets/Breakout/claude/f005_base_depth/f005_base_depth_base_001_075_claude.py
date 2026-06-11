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
def _f005_base_range(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return (hi - lo) / hi.replace(0, np.nan).abs()


def _f005_base_depth(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return (hi - lo) / lo.replace(0, np.nan).abs()


def _f005_base_tightness(close, w):
    m = close.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = close.rolling(w, min_periods=max(1, w // 2)).std()
    return sd / m.replace(0, np.nan).abs()


def f005bdp_f005_base_depth_brgid_5d_base_v001_signal(closeadj):
    base = _f005_base_range(closeadj, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_bdpid_5d_base_v002_signal(closeadj):
    base = _f005_base_depth(closeadj, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_btgid_5d_base_v003_signal(closeadj):
    base = _f005_base_tightness(closeadj, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_brgid_10d_base_v004_signal(closeadj):
    base = _f005_base_range(closeadj, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_bdpid_10d_base_v005_signal(closeadj):
    base = _f005_base_depth(closeadj, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_btgid_10d_base_v006_signal(closeadj):
    base = _f005_base_tightness(closeadj, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_brgid_21d_base_v007_signal(closeadj):
    base = _f005_base_range(closeadj, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_bdpid_21d_base_v008_signal(closeadj):
    base = _f005_base_depth(closeadj, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_btgid_21d_base_v009_signal(closeadj):
    base = _f005_base_tightness(closeadj, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_brgid_42d_base_v010_signal(closeadj):
    base = _f005_base_range(closeadj, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_bdpid_42d_base_v011_signal(closeadj):
    base = _f005_base_depth(closeadj, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_btgid_42d_base_v012_signal(closeadj):
    base = _f005_base_tightness(closeadj, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_brgid_63d_base_v013_signal(closeadj):
    base = _f005_base_range(closeadj, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_bdpid_63d_base_v014_signal(closeadj):
    base = _f005_base_depth(closeadj, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_btgid_63d_base_v015_signal(closeadj):
    base = _f005_base_tightness(closeadj, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_brgid_126d_base_v016_signal(closeadj):
    base = _f005_base_range(closeadj, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_bdpid_126d_base_v017_signal(closeadj):
    base = _f005_base_depth(closeadj, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_btgid_126d_base_v018_signal(closeadj):
    base = _f005_base_tightness(closeadj, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_brgid_189d_base_v019_signal(closeadj):
    base = _f005_base_range(closeadj, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_bdpid_189d_base_v020_signal(closeadj):
    base = _f005_base_depth(closeadj, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_btgid_189d_base_v021_signal(closeadj):
    base = _f005_base_tightness(closeadj, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_brgid_252d_base_v022_signal(closeadj):
    base = _f005_base_range(closeadj, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_bdpid_252d_base_v023_signal(closeadj):
    base = _f005_base_depth(closeadj, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_btgid_252d_base_v024_signal(closeadj):
    base = _f005_base_tightness(closeadj, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_brgid_378d_base_v025_signal(closeadj):
    base = _f005_base_range(closeadj, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_bdpid_378d_base_v026_signal(closeadj):
    base = _f005_base_depth(closeadj, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_btgid_378d_base_v027_signal(closeadj):
    base = _f005_base_tightness(closeadj, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_brgid_504d_base_v028_signal(closeadj):
    base = _f005_base_range(closeadj, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_bdpid_504d_base_v029_signal(closeadj):
    base = _f005_base_depth(closeadj, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_btgid_504d_base_v030_signal(closeadj):
    base = _f005_base_tightness(closeadj, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_brgab_5d_base_v031_signal(closeadj):
    base = _f005_base_range(closeadj, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_bdpab_5d_base_v032_signal(closeadj):
    base = _f005_base_depth(closeadj, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_btgab_5d_base_v033_signal(closeadj):
    base = _f005_base_tightness(closeadj, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_brgab_10d_base_v034_signal(closeadj):
    base = _f005_base_range(closeadj, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_bdpab_10d_base_v035_signal(closeadj):
    base = _f005_base_depth(closeadj, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_btgab_10d_base_v036_signal(closeadj):
    base = _f005_base_tightness(closeadj, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_brgab_21d_base_v037_signal(closeadj):
    base = _f005_base_range(closeadj, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_bdpab_21d_base_v038_signal(closeadj):
    base = _f005_base_depth(closeadj, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_btgab_21d_base_v039_signal(closeadj):
    base = _f005_base_tightness(closeadj, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_brgab_42d_base_v040_signal(closeadj):
    base = _f005_base_range(closeadj, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_bdpab_42d_base_v041_signal(closeadj):
    base = _f005_base_depth(closeadj, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_btgab_42d_base_v042_signal(closeadj):
    base = _f005_base_tightness(closeadj, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_brgab_63d_base_v043_signal(closeadj):
    base = _f005_base_range(closeadj, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_bdpab_63d_base_v044_signal(closeadj):
    base = _f005_base_depth(closeadj, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_btgab_63d_base_v045_signal(closeadj):
    base = _f005_base_tightness(closeadj, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_brgab_126d_base_v046_signal(closeadj):
    base = _f005_base_range(closeadj, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_bdpab_126d_base_v047_signal(closeadj):
    base = _f005_base_depth(closeadj, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_btgab_126d_base_v048_signal(closeadj):
    base = _f005_base_tightness(closeadj, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_brgab_189d_base_v049_signal(closeadj):
    base = _f005_base_range(closeadj, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_bdpab_189d_base_v050_signal(closeadj):
    base = _f005_base_depth(closeadj, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_btgab_189d_base_v051_signal(closeadj):
    base = _f005_base_tightness(closeadj, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_brgab_252d_base_v052_signal(closeadj):
    base = _f005_base_range(closeadj, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_bdpab_252d_base_v053_signal(closeadj):
    base = _f005_base_depth(closeadj, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_btgab_252d_base_v054_signal(closeadj):
    base = _f005_base_tightness(closeadj, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_brgab_378d_base_v055_signal(closeadj):
    base = _f005_base_range(closeadj, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_bdpab_378d_base_v056_signal(closeadj):
    base = _f005_base_depth(closeadj, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_btgab_378d_base_v057_signal(closeadj):
    base = _f005_base_tightness(closeadj, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_brgab_504d_base_v058_signal(closeadj):
    base = _f005_base_range(closeadj, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_bdpab_504d_base_v059_signal(closeadj):
    base = _f005_base_depth(closeadj, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_btgab_504d_base_v060_signal(closeadj):
    base = _f005_base_tightness(closeadj, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_brgsq_5d_base_v061_signal(closeadj):
    base = _f005_base_range(closeadj, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_bdpsq_5d_base_v062_signal(closeadj):
    base = _f005_base_depth(closeadj, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_btgsq_5d_base_v063_signal(closeadj):
    base = _f005_base_tightness(closeadj, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_brgsq_10d_base_v064_signal(closeadj):
    base = _f005_base_range(closeadj, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_bdpsq_10d_base_v065_signal(closeadj):
    base = _f005_base_depth(closeadj, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_btgsq_10d_base_v066_signal(closeadj):
    base = _f005_base_tightness(closeadj, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_brgsq_21d_base_v067_signal(closeadj):
    base = _f005_base_range(closeadj, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_bdpsq_21d_base_v068_signal(closeadj):
    base = _f005_base_depth(closeadj, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_btgsq_21d_base_v069_signal(closeadj):
    base = _f005_base_tightness(closeadj, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_brgsq_42d_base_v070_signal(closeadj):
    base = _f005_base_range(closeadj, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_bdpsq_42d_base_v071_signal(closeadj):
    base = _f005_base_depth(closeadj, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_btgsq_42d_base_v072_signal(closeadj):
    base = _f005_base_tightness(closeadj, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_brgsq_63d_base_v073_signal(closeadj):
    base = _f005_base_range(closeadj, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_bdpsq_63d_base_v074_signal(closeadj):
    base = _f005_base_depth(closeadj, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_btgsq_63d_base_v075_signal(closeadj):
    base = _f005_base_tightness(closeadj, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f005bdp_f005_base_depth_brgid_5d_base_v001_signal,
    f005bdp_f005_base_depth_bdpid_5d_base_v002_signal,
    f005bdp_f005_base_depth_btgid_5d_base_v003_signal,
    f005bdp_f005_base_depth_brgid_10d_base_v004_signal,
    f005bdp_f005_base_depth_bdpid_10d_base_v005_signal,
    f005bdp_f005_base_depth_btgid_10d_base_v006_signal,
    f005bdp_f005_base_depth_brgid_21d_base_v007_signal,
    f005bdp_f005_base_depth_bdpid_21d_base_v008_signal,
    f005bdp_f005_base_depth_btgid_21d_base_v009_signal,
    f005bdp_f005_base_depth_brgid_42d_base_v010_signal,
    f005bdp_f005_base_depth_bdpid_42d_base_v011_signal,
    f005bdp_f005_base_depth_btgid_42d_base_v012_signal,
    f005bdp_f005_base_depth_brgid_63d_base_v013_signal,
    f005bdp_f005_base_depth_bdpid_63d_base_v014_signal,
    f005bdp_f005_base_depth_btgid_63d_base_v015_signal,
    f005bdp_f005_base_depth_brgid_126d_base_v016_signal,
    f005bdp_f005_base_depth_bdpid_126d_base_v017_signal,
    f005bdp_f005_base_depth_btgid_126d_base_v018_signal,
    f005bdp_f005_base_depth_brgid_189d_base_v019_signal,
    f005bdp_f005_base_depth_bdpid_189d_base_v020_signal,
    f005bdp_f005_base_depth_btgid_189d_base_v021_signal,
    f005bdp_f005_base_depth_brgid_252d_base_v022_signal,
    f005bdp_f005_base_depth_bdpid_252d_base_v023_signal,
    f005bdp_f005_base_depth_btgid_252d_base_v024_signal,
    f005bdp_f005_base_depth_brgid_378d_base_v025_signal,
    f005bdp_f005_base_depth_bdpid_378d_base_v026_signal,
    f005bdp_f005_base_depth_btgid_378d_base_v027_signal,
    f005bdp_f005_base_depth_brgid_504d_base_v028_signal,
    f005bdp_f005_base_depth_bdpid_504d_base_v029_signal,
    f005bdp_f005_base_depth_btgid_504d_base_v030_signal,
    f005bdp_f005_base_depth_brgab_5d_base_v031_signal,
    f005bdp_f005_base_depth_bdpab_5d_base_v032_signal,
    f005bdp_f005_base_depth_btgab_5d_base_v033_signal,
    f005bdp_f005_base_depth_brgab_10d_base_v034_signal,
    f005bdp_f005_base_depth_bdpab_10d_base_v035_signal,
    f005bdp_f005_base_depth_btgab_10d_base_v036_signal,
    f005bdp_f005_base_depth_brgab_21d_base_v037_signal,
    f005bdp_f005_base_depth_bdpab_21d_base_v038_signal,
    f005bdp_f005_base_depth_btgab_21d_base_v039_signal,
    f005bdp_f005_base_depth_brgab_42d_base_v040_signal,
    f005bdp_f005_base_depth_bdpab_42d_base_v041_signal,
    f005bdp_f005_base_depth_btgab_42d_base_v042_signal,
    f005bdp_f005_base_depth_brgab_63d_base_v043_signal,
    f005bdp_f005_base_depth_bdpab_63d_base_v044_signal,
    f005bdp_f005_base_depth_btgab_63d_base_v045_signal,
    f005bdp_f005_base_depth_brgab_126d_base_v046_signal,
    f005bdp_f005_base_depth_bdpab_126d_base_v047_signal,
    f005bdp_f005_base_depth_btgab_126d_base_v048_signal,
    f005bdp_f005_base_depth_brgab_189d_base_v049_signal,
    f005bdp_f005_base_depth_bdpab_189d_base_v050_signal,
    f005bdp_f005_base_depth_btgab_189d_base_v051_signal,
    f005bdp_f005_base_depth_brgab_252d_base_v052_signal,
    f005bdp_f005_base_depth_bdpab_252d_base_v053_signal,
    f005bdp_f005_base_depth_btgab_252d_base_v054_signal,
    f005bdp_f005_base_depth_brgab_378d_base_v055_signal,
    f005bdp_f005_base_depth_bdpab_378d_base_v056_signal,
    f005bdp_f005_base_depth_btgab_378d_base_v057_signal,
    f005bdp_f005_base_depth_brgab_504d_base_v058_signal,
    f005bdp_f005_base_depth_bdpab_504d_base_v059_signal,
    f005bdp_f005_base_depth_btgab_504d_base_v060_signal,
    f005bdp_f005_base_depth_brgsq_5d_base_v061_signal,
    f005bdp_f005_base_depth_bdpsq_5d_base_v062_signal,
    f005bdp_f005_base_depth_btgsq_5d_base_v063_signal,
    f005bdp_f005_base_depth_brgsq_10d_base_v064_signal,
    f005bdp_f005_base_depth_bdpsq_10d_base_v065_signal,
    f005bdp_f005_base_depth_btgsq_10d_base_v066_signal,
    f005bdp_f005_base_depth_brgsq_21d_base_v067_signal,
    f005bdp_f005_base_depth_bdpsq_21d_base_v068_signal,
    f005bdp_f005_base_depth_btgsq_21d_base_v069_signal,
    f005bdp_f005_base_depth_brgsq_42d_base_v070_signal,
    f005bdp_f005_base_depth_bdpsq_42d_base_v071_signal,
    f005bdp_f005_base_depth_btgsq_42d_base_v072_signal,
    f005bdp_f005_base_depth_brgsq_63d_base_v073_signal,
    f005bdp_f005_base_depth_bdpsq_63d_base_v074_signal,
    f005bdp_f005_base_depth_btgsq_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F005_BASE_DEPTH_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f005_base_range", "_f005_base_depth", "_f005_base_tightness")
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
    print(f"OK f005_base_depth_base_001_075_claude: {n_features} features pass")
