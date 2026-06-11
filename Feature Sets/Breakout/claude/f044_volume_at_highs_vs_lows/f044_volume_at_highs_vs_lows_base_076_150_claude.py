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
def _f044_near_high(closeadj, w):
    hi = closeadj.rolling(w, min_periods=max(1, w // 2)).max()
    lo = closeadj.rolling(w, min_periods=max(1, w // 2)).min()
    rng = (hi - lo).replace(0, np.nan)
    return (closeadj - lo) / rng


def _f044_vol_at_highs(closeadj, volume, w):
    pos = _f044_near_high(closeadj, w)
    return (volume * pos).rolling(w, min_periods=max(1, w // 2)).sum()


def _f044_vol_at_lows(closeadj, volume, w):
    pos = _f044_near_high(closeadj, w)
    return (volume * (1.0 - pos)).rolling(w, min_periods=max(1, w // 2)).sum()

def f044vhl_f044_volume_at_highs_vs_lows_nhtanh_5d_base_v001_signal(closeadj, volume):
    base = _f044_near_high(closeadj, 5)
    result = np.tanh(base) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_vahtanh_5d_base_v002_signal(closeadj, volume):
    base = _f044_vol_at_highs(closeadj, volume, 5)
    result = np.tanh(_z(base, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_valtanh_5d_base_v003_signal(closeadj, volume):
    base = _f044_vol_at_lows(closeadj, volume, 5)
    result = np.tanh(_z(base, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_nhtanh_10d_base_v004_signal(closeadj, volume):
    base = _f044_near_high(closeadj, 10)
    result = np.tanh(base) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_vahtanh_10d_base_v005_signal(closeadj, volume):
    base = _f044_vol_at_highs(closeadj, volume, 10)
    result = np.tanh(_z(base, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_valtanh_10d_base_v006_signal(closeadj, volume):
    base = _f044_vol_at_lows(closeadj, volume, 10)
    result = np.tanh(_z(base, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_nhtanh_21d_base_v007_signal(closeadj, volume):
    base = _f044_near_high(closeadj, 21)
    result = np.tanh(base) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_vahtanh_21d_base_v008_signal(closeadj, volume):
    base = _f044_vol_at_highs(closeadj, volume, 21)
    result = np.tanh(_z(base, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_valtanh_21d_base_v009_signal(closeadj, volume):
    base = _f044_vol_at_lows(closeadj, volume, 21)
    result = np.tanh(_z(base, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_nhtanh_42d_base_v010_signal(closeadj, volume):
    base = _f044_near_high(closeadj, 42)
    result = np.tanh(base) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_vahtanh_42d_base_v011_signal(closeadj, volume):
    base = _f044_vol_at_highs(closeadj, volume, 42)
    result = np.tanh(_z(base, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_valtanh_42d_base_v012_signal(closeadj, volume):
    base = _f044_vol_at_lows(closeadj, volume, 42)
    result = np.tanh(_z(base, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_nhtanh_63d_base_v013_signal(closeadj, volume):
    base = _f044_near_high(closeadj, 63)
    result = np.tanh(base) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_vahtanh_63d_base_v014_signal(closeadj, volume):
    base = _f044_vol_at_highs(closeadj, volume, 63)
    result = np.tanh(_z(base, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_valtanh_63d_base_v015_signal(closeadj, volume):
    base = _f044_vol_at_lows(closeadj, volume, 63)
    result = np.tanh(_z(base, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_nhtanh_126d_base_v016_signal(closeadj, volume):
    base = _f044_near_high(closeadj, 126)
    result = np.tanh(base) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_vahtanh_126d_base_v017_signal(closeadj, volume):
    base = _f044_vol_at_highs(closeadj, volume, 126)
    result = np.tanh(_z(base, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_valtanh_126d_base_v018_signal(closeadj, volume):
    base = _f044_vol_at_lows(closeadj, volume, 126)
    result = np.tanh(_z(base, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_nhtanh_189d_base_v019_signal(closeadj, volume):
    base = _f044_near_high(closeadj, 189)
    result = np.tanh(base) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_vahtanh_189d_base_v020_signal(closeadj, volume):
    base = _f044_vol_at_highs(closeadj, volume, 189)
    result = np.tanh(_z(base, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_valtanh_189d_base_v021_signal(closeadj, volume):
    base = _f044_vol_at_lows(closeadj, volume, 189)
    result = np.tanh(_z(base, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_nhtanh_252d_base_v022_signal(closeadj, volume):
    base = _f044_near_high(closeadj, 252)
    result = np.tanh(base) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_vahtanh_252d_base_v023_signal(closeadj, volume):
    base = _f044_vol_at_highs(closeadj, volume, 252)
    result = np.tanh(_z(base, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_valtanh_252d_base_v024_signal(closeadj, volume):
    base = _f044_vol_at_lows(closeadj, volume, 252)
    result = np.tanh(_z(base, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_nhtanh_378d_base_v025_signal(closeadj, volume):
    base = _f044_near_high(closeadj, 378)
    result = np.tanh(base) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_vahtanh_378d_base_v026_signal(closeadj, volume):
    base = _f044_vol_at_highs(closeadj, volume, 378)
    result = np.tanh(_z(base, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_valtanh_378d_base_v027_signal(closeadj, volume):
    base = _f044_vol_at_lows(closeadj, volume, 378)
    result = np.tanh(_z(base, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_nhtanh_504d_base_v028_signal(closeadj, volume):
    base = _f044_near_high(closeadj, 504)
    result = np.tanh(base) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_vahtanh_504d_base_v029_signal(closeadj, volume):
    base = _f044_vol_at_highs(closeadj, volume, 504)
    result = np.tanh(_z(base, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_valtanh_504d_base_v030_signal(closeadj, volume):
    base = _f044_vol_at_lows(closeadj, volume, 504)
    result = np.tanh(_z(base, 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_nhclip_5d_base_v031_signal(closeadj, volume):
    base = _f044_near_high(closeadj, 5)
    result = base.clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_vahclip_5d_base_v032_signal(closeadj, volume):
    base = _f044_vol_at_highs(closeadj, volume, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_valclip_5d_base_v033_signal(closeadj, volume):
    base = _f044_vol_at_lows(closeadj, volume, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_nhclip_10d_base_v034_signal(closeadj, volume):
    base = _f044_near_high(closeadj, 10)
    result = base.clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_vahclip_10d_base_v035_signal(closeadj, volume):
    base = _f044_vol_at_highs(closeadj, volume, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_valclip_10d_base_v036_signal(closeadj, volume):
    base = _f044_vol_at_lows(closeadj, volume, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_nhclip_21d_base_v037_signal(closeadj, volume):
    base = _f044_near_high(closeadj, 21)
    result = base.clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_vahclip_21d_base_v038_signal(closeadj, volume):
    base = _f044_vol_at_highs(closeadj, volume, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_valclip_21d_base_v039_signal(closeadj, volume):
    base = _f044_vol_at_lows(closeadj, volume, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_nhclip_42d_base_v040_signal(closeadj, volume):
    base = _f044_near_high(closeadj, 42)
    result = base.clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_vahclip_42d_base_v041_signal(closeadj, volume):
    base = _f044_vol_at_highs(closeadj, volume, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_valclip_42d_base_v042_signal(closeadj, volume):
    base = _f044_vol_at_lows(closeadj, volume, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_nhclip_63d_base_v043_signal(closeadj, volume):
    base = _f044_near_high(closeadj, 63)
    result = base.clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_vahclip_63d_base_v044_signal(closeadj, volume):
    base = _f044_vol_at_highs(closeadj, volume, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_valclip_63d_base_v045_signal(closeadj, volume):
    base = _f044_vol_at_lows(closeadj, volume, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_nhclip_126d_base_v046_signal(closeadj, volume):
    base = _f044_near_high(closeadj, 126)
    result = base.clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_vahclip_126d_base_v047_signal(closeadj, volume):
    base = _f044_vol_at_highs(closeadj, volume, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_valclip_126d_base_v048_signal(closeadj, volume):
    base = _f044_vol_at_lows(closeadj, volume, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_nhclip_189d_base_v049_signal(closeadj, volume):
    base = _f044_near_high(closeadj, 189)
    result = base.clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_vahclip_189d_base_v050_signal(closeadj, volume):
    base = _f044_vol_at_highs(closeadj, volume, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_valclip_189d_base_v051_signal(closeadj, volume):
    base = _f044_vol_at_lows(closeadj, volume, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_nhclip_252d_base_v052_signal(closeadj, volume):
    base = _f044_near_high(closeadj, 252)
    result = base.clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_vahclip_252d_base_v053_signal(closeadj, volume):
    base = _f044_vol_at_highs(closeadj, volume, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_valclip_252d_base_v054_signal(closeadj, volume):
    base = _f044_vol_at_lows(closeadj, volume, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_nhclip_378d_base_v055_signal(closeadj, volume):
    base = _f044_near_high(closeadj, 378)
    result = base.clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_vahclip_378d_base_v056_signal(closeadj, volume):
    base = _f044_vol_at_highs(closeadj, volume, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_valclip_378d_base_v057_signal(closeadj, volume):
    base = _f044_vol_at_lows(closeadj, volume, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_nhclip_504d_base_v058_signal(closeadj, volume):
    base = _f044_near_high(closeadj, 504)
    result = base.clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_vahclip_504d_base_v059_signal(closeadj, volume):
    base = _f044_vol_at_highs(closeadj, volume, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_valclip_504d_base_v060_signal(closeadj, volume):
    base = _f044_vol_at_lows(closeadj, volume, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_nhcube_5d_base_v061_signal(closeadj, volume):
    base = _f044_near_high(closeadj, 5)
    result = np.sign(base) * base.abs().pow(1.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_vahcube_5d_base_v062_signal(closeadj, volume):
    base = _f044_vol_at_highs(closeadj, volume, 5)
    result = np.sign(_z(base, 252)) * _z(base, 252).abs().pow(1.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_valcube_5d_base_v063_signal(closeadj, volume):
    base = _f044_vol_at_lows(closeadj, volume, 5)
    result = np.sign(_z(base, 252)) * _z(base, 252).abs().pow(1.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_nhcube_10d_base_v064_signal(closeadj, volume):
    base = _f044_near_high(closeadj, 10)
    result = np.sign(base) * base.abs().pow(1.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_vahcube_10d_base_v065_signal(closeadj, volume):
    base = _f044_vol_at_highs(closeadj, volume, 10)
    result = np.sign(_z(base, 252)) * _z(base, 252).abs().pow(1.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_valcube_10d_base_v066_signal(closeadj, volume):
    base = _f044_vol_at_lows(closeadj, volume, 10)
    result = np.sign(_z(base, 252)) * _z(base, 252).abs().pow(1.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_nhcube_21d_base_v067_signal(closeadj, volume):
    base = _f044_near_high(closeadj, 21)
    result = np.sign(base) * base.abs().pow(1.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_vahcube_21d_base_v068_signal(closeadj, volume):
    base = _f044_vol_at_highs(closeadj, volume, 21)
    result = np.sign(_z(base, 252)) * _z(base, 252).abs().pow(1.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_valcube_21d_base_v069_signal(closeadj, volume):
    base = _f044_vol_at_lows(closeadj, volume, 21)
    result = np.sign(_z(base, 252)) * _z(base, 252).abs().pow(1.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_nhcube_42d_base_v070_signal(closeadj, volume):
    base = _f044_near_high(closeadj, 42)
    result = np.sign(base) * base.abs().pow(1.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_vahcube_42d_base_v071_signal(closeadj, volume):
    base = _f044_vol_at_highs(closeadj, volume, 42)
    result = np.sign(_z(base, 252)) * _z(base, 252).abs().pow(1.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_valcube_42d_base_v072_signal(closeadj, volume):
    base = _f044_vol_at_lows(closeadj, volume, 42)
    result = np.sign(_z(base, 252)) * _z(base, 252).abs().pow(1.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_nhcube_63d_base_v073_signal(closeadj, volume):
    base = _f044_near_high(closeadj, 63)
    result = np.sign(base) * base.abs().pow(1.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_vahcube_63d_base_v074_signal(closeadj, volume):
    base = _f044_vol_at_highs(closeadj, volume, 63)
    result = np.sign(_z(base, 252)) * _z(base, 252).abs().pow(1.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f044vhl_f044_volume_at_highs_vs_lows_valcube_63d_base_v075_signal(closeadj, volume):
    base = _f044_vol_at_lows(closeadj, volume, 63)
    result = np.sign(_z(base, 252)) * _z(base, 252).abs().pow(1.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f044vhl_f044_volume_at_highs_vs_lows_nhtanh_5d_base_v001_signal,
    f044vhl_f044_volume_at_highs_vs_lows_vahtanh_5d_base_v002_signal,
    f044vhl_f044_volume_at_highs_vs_lows_valtanh_5d_base_v003_signal,
    f044vhl_f044_volume_at_highs_vs_lows_nhtanh_10d_base_v004_signal,
    f044vhl_f044_volume_at_highs_vs_lows_vahtanh_10d_base_v005_signal,
    f044vhl_f044_volume_at_highs_vs_lows_valtanh_10d_base_v006_signal,
    f044vhl_f044_volume_at_highs_vs_lows_nhtanh_21d_base_v007_signal,
    f044vhl_f044_volume_at_highs_vs_lows_vahtanh_21d_base_v008_signal,
    f044vhl_f044_volume_at_highs_vs_lows_valtanh_21d_base_v009_signal,
    f044vhl_f044_volume_at_highs_vs_lows_nhtanh_42d_base_v010_signal,
    f044vhl_f044_volume_at_highs_vs_lows_vahtanh_42d_base_v011_signal,
    f044vhl_f044_volume_at_highs_vs_lows_valtanh_42d_base_v012_signal,
    f044vhl_f044_volume_at_highs_vs_lows_nhtanh_63d_base_v013_signal,
    f044vhl_f044_volume_at_highs_vs_lows_vahtanh_63d_base_v014_signal,
    f044vhl_f044_volume_at_highs_vs_lows_valtanh_63d_base_v015_signal,
    f044vhl_f044_volume_at_highs_vs_lows_nhtanh_126d_base_v016_signal,
    f044vhl_f044_volume_at_highs_vs_lows_vahtanh_126d_base_v017_signal,
    f044vhl_f044_volume_at_highs_vs_lows_valtanh_126d_base_v018_signal,
    f044vhl_f044_volume_at_highs_vs_lows_nhtanh_189d_base_v019_signal,
    f044vhl_f044_volume_at_highs_vs_lows_vahtanh_189d_base_v020_signal,
    f044vhl_f044_volume_at_highs_vs_lows_valtanh_189d_base_v021_signal,
    f044vhl_f044_volume_at_highs_vs_lows_nhtanh_252d_base_v022_signal,
    f044vhl_f044_volume_at_highs_vs_lows_vahtanh_252d_base_v023_signal,
    f044vhl_f044_volume_at_highs_vs_lows_valtanh_252d_base_v024_signal,
    f044vhl_f044_volume_at_highs_vs_lows_nhtanh_378d_base_v025_signal,
    f044vhl_f044_volume_at_highs_vs_lows_vahtanh_378d_base_v026_signal,
    f044vhl_f044_volume_at_highs_vs_lows_valtanh_378d_base_v027_signal,
    f044vhl_f044_volume_at_highs_vs_lows_nhtanh_504d_base_v028_signal,
    f044vhl_f044_volume_at_highs_vs_lows_vahtanh_504d_base_v029_signal,
    f044vhl_f044_volume_at_highs_vs_lows_valtanh_504d_base_v030_signal,
    f044vhl_f044_volume_at_highs_vs_lows_nhclip_5d_base_v031_signal,
    f044vhl_f044_volume_at_highs_vs_lows_vahclip_5d_base_v032_signal,
    f044vhl_f044_volume_at_highs_vs_lows_valclip_5d_base_v033_signal,
    f044vhl_f044_volume_at_highs_vs_lows_nhclip_10d_base_v034_signal,
    f044vhl_f044_volume_at_highs_vs_lows_vahclip_10d_base_v035_signal,
    f044vhl_f044_volume_at_highs_vs_lows_valclip_10d_base_v036_signal,
    f044vhl_f044_volume_at_highs_vs_lows_nhclip_21d_base_v037_signal,
    f044vhl_f044_volume_at_highs_vs_lows_vahclip_21d_base_v038_signal,
    f044vhl_f044_volume_at_highs_vs_lows_valclip_21d_base_v039_signal,
    f044vhl_f044_volume_at_highs_vs_lows_nhclip_42d_base_v040_signal,
    f044vhl_f044_volume_at_highs_vs_lows_vahclip_42d_base_v041_signal,
    f044vhl_f044_volume_at_highs_vs_lows_valclip_42d_base_v042_signal,
    f044vhl_f044_volume_at_highs_vs_lows_nhclip_63d_base_v043_signal,
    f044vhl_f044_volume_at_highs_vs_lows_vahclip_63d_base_v044_signal,
    f044vhl_f044_volume_at_highs_vs_lows_valclip_63d_base_v045_signal,
    f044vhl_f044_volume_at_highs_vs_lows_nhclip_126d_base_v046_signal,
    f044vhl_f044_volume_at_highs_vs_lows_vahclip_126d_base_v047_signal,
    f044vhl_f044_volume_at_highs_vs_lows_valclip_126d_base_v048_signal,
    f044vhl_f044_volume_at_highs_vs_lows_nhclip_189d_base_v049_signal,
    f044vhl_f044_volume_at_highs_vs_lows_vahclip_189d_base_v050_signal,
    f044vhl_f044_volume_at_highs_vs_lows_valclip_189d_base_v051_signal,
    f044vhl_f044_volume_at_highs_vs_lows_nhclip_252d_base_v052_signal,
    f044vhl_f044_volume_at_highs_vs_lows_vahclip_252d_base_v053_signal,
    f044vhl_f044_volume_at_highs_vs_lows_valclip_252d_base_v054_signal,
    f044vhl_f044_volume_at_highs_vs_lows_nhclip_378d_base_v055_signal,
    f044vhl_f044_volume_at_highs_vs_lows_vahclip_378d_base_v056_signal,
    f044vhl_f044_volume_at_highs_vs_lows_valclip_378d_base_v057_signal,
    f044vhl_f044_volume_at_highs_vs_lows_nhclip_504d_base_v058_signal,
    f044vhl_f044_volume_at_highs_vs_lows_vahclip_504d_base_v059_signal,
    f044vhl_f044_volume_at_highs_vs_lows_valclip_504d_base_v060_signal,
    f044vhl_f044_volume_at_highs_vs_lows_nhcube_5d_base_v061_signal,
    f044vhl_f044_volume_at_highs_vs_lows_vahcube_5d_base_v062_signal,
    f044vhl_f044_volume_at_highs_vs_lows_valcube_5d_base_v063_signal,
    f044vhl_f044_volume_at_highs_vs_lows_nhcube_10d_base_v064_signal,
    f044vhl_f044_volume_at_highs_vs_lows_vahcube_10d_base_v065_signal,
    f044vhl_f044_volume_at_highs_vs_lows_valcube_10d_base_v066_signal,
    f044vhl_f044_volume_at_highs_vs_lows_nhcube_21d_base_v067_signal,
    f044vhl_f044_volume_at_highs_vs_lows_vahcube_21d_base_v068_signal,
    f044vhl_f044_volume_at_highs_vs_lows_valcube_21d_base_v069_signal,
    f044vhl_f044_volume_at_highs_vs_lows_nhcube_42d_base_v070_signal,
    f044vhl_f044_volume_at_highs_vs_lows_vahcube_42d_base_v071_signal,
    f044vhl_f044_volume_at_highs_vs_lows_valcube_42d_base_v072_signal,
    f044vhl_f044_volume_at_highs_vs_lows_nhcube_63d_base_v073_signal,
    f044vhl_f044_volume_at_highs_vs_lows_vahcube_63d_base_v074_signal,
    f044vhl_f044_volume_at_highs_vs_lows_valcube_63d_base_v075_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F044_VOLUME_AT_HIGHS_VS_LOWS_REGISTRY_076_150 = REGISTRY



if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f044_near_high", "_f044_vol_at_highs", "_f044_vol_at_lows")
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
    print(f"OK {__file__}: {n_features} features pass")
