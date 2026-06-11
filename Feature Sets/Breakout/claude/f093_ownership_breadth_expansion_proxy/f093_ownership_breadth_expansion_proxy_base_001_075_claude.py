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
def _f093_volume_breadth(volume, w):
    return _mean(volume, w) / _mean(volume, w * 2).replace(0, np.nan)


def _f093_share_count_stable(sharesbas, w):
    return 1.0 - _std(sharesbas.pct_change(), w).fillna(0)


def _f093_breadth_proxy(volume, sharesbas, w):
    turnover = volume / sharesbas.replace(0, np.nan)
    return _mean(turnover, w)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrraw_5d_base_v001_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstraw_5d_base_v002_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyraw_5d_base_v003_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrraw_10d_base_v004_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstraw_10d_base_v005_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 10)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyraw_10d_base_v006_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrraw_21d_base_v007_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstraw_21d_base_v008_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 21)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyraw_21d_base_v009_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrraw_42d_base_v010_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 42)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstraw_42d_base_v011_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 42)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyraw_42d_base_v012_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrraw_63d_base_v013_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 63)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstraw_63d_base_v014_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 63)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyraw_63d_base_v015_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrraw_126d_base_v016_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 126)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstraw_126d_base_v017_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 126)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyraw_126d_base_v018_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 126)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrraw_189d_base_v019_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 189)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstraw_189d_base_v020_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 189)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyraw_189d_base_v021_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 189)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrraw_252d_base_v022_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 252)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstraw_252d_base_v023_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 252)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyraw_252d_base_v024_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 252)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrraw_378d_base_v025_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 378)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstraw_378d_base_v026_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 378)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyraw_378d_base_v027_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 378)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrraw_504d_base_v028_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 504)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstraw_504d_base_v029_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 504)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyraw_504d_base_v030_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 504)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrabs_5d_base_v031_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstabs_5d_base_v032_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyabs_5d_base_v033_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrabs_10d_base_v034_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstabs_10d_base_v035_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 10)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyabs_10d_base_v036_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrabs_21d_base_v037_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstabs_21d_base_v038_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 21)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyabs_21d_base_v039_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrabs_42d_base_v040_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 42)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstabs_42d_base_v041_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 42)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyabs_42d_base_v042_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrabs_63d_base_v043_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 63)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstabs_63d_base_v044_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 63)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyabs_63d_base_v045_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrabs_126d_base_v046_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 126)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstabs_126d_base_v047_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 126)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyabs_126d_base_v048_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 126)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrabs_189d_base_v049_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 189)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstabs_189d_base_v050_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 189)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyabs_189d_base_v051_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 189)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrabs_252d_base_v052_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 252)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstabs_252d_base_v053_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 252)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyabs_252d_base_v054_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 252)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrabs_378d_base_v055_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 378)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstabs_378d_base_v056_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 378)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyabs_378d_base_v057_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 378)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrabs_504d_base_v058_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 504)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstabs_504d_base_v059_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 504)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxyabs_504d_base_v060_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 504)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrsqs_5d_base_v061_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstsqs_5d_base_v062_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 5)
    result = _z(np.sign(base) * base.abs().pow(0.5), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxysqs_5d_base_v063_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrsqs_10d_base_v064_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 10)
    result = _z(np.sign(base) * base.abs().pow(0.5), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstsqs_10d_base_v065_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 10)
    result = _z(np.sign(base) * base.abs().pow(0.5), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxysqs_10d_base_v066_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrsqs_21d_base_v067_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 21)
    result = _z(np.sign(base) * base.abs().pow(0.5), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstsqs_21d_base_v068_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 21)
    result = _z(np.sign(base) * base.abs().pow(0.5), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxysqs_21d_base_v069_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 21)
    result = _z(np.sign(base) * base.abs().pow(0.5), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrsqs_42d_base_v070_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 42)
    result = _z(np.sign(base) * base.abs().pow(0.5), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstsqs_42d_base_v071_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 42)
    result = _z(np.sign(base) * base.abs().pow(0.5), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxysqs_42d_base_v072_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 42)
    result = _z(np.sign(base) * base.abs().pow(0.5), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_volbrsqs_63d_base_v073_signal(volume, sharesbas, closeadj):
    base = _f093_volume_breadth(volume, 63)
    result = _z(np.sign(base) * base.abs().pow(0.5), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_shcstsqs_63d_base_v074_signal(volume, sharesbas, closeadj):
    base = _f093_share_count_stable(sharesbas, 63)
    result = _z(np.sign(base) * base.abs().pow(0.5), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f093obe_f093_ownership_breadth_expansion_proxy_brpxysqs_63d_base_v075_signal(volume, sharesbas, closeadj):
    base = _f093_breadth_proxy(volume, sharesbas, 63)
    result = _z(np.sign(base) * base.abs().pow(0.5), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f093obe_f093_ownership_breadth_expansion_proxy_volbrraw_5d_base_v001_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstraw_5d_base_v002_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyraw_5d_base_v003_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrraw_10d_base_v004_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstraw_10d_base_v005_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyraw_10d_base_v006_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrraw_21d_base_v007_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstraw_21d_base_v008_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyraw_21d_base_v009_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrraw_42d_base_v010_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstraw_42d_base_v011_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyraw_42d_base_v012_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrraw_63d_base_v013_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstraw_63d_base_v014_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyraw_63d_base_v015_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrraw_126d_base_v016_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstraw_126d_base_v017_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyraw_126d_base_v018_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrraw_189d_base_v019_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstraw_189d_base_v020_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyraw_189d_base_v021_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrraw_252d_base_v022_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstraw_252d_base_v023_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyraw_252d_base_v024_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrraw_378d_base_v025_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstraw_378d_base_v026_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyraw_378d_base_v027_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrraw_504d_base_v028_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstraw_504d_base_v029_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyraw_504d_base_v030_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrabs_5d_base_v031_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstabs_5d_base_v032_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyabs_5d_base_v033_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrabs_10d_base_v034_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstabs_10d_base_v035_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyabs_10d_base_v036_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrabs_21d_base_v037_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstabs_21d_base_v038_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyabs_21d_base_v039_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrabs_42d_base_v040_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstabs_42d_base_v041_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyabs_42d_base_v042_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrabs_63d_base_v043_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstabs_63d_base_v044_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyabs_63d_base_v045_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrabs_126d_base_v046_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstabs_126d_base_v047_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyabs_126d_base_v048_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrabs_189d_base_v049_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstabs_189d_base_v050_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyabs_189d_base_v051_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrabs_252d_base_v052_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstabs_252d_base_v053_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyabs_252d_base_v054_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrabs_378d_base_v055_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstabs_378d_base_v056_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyabs_378d_base_v057_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrabs_504d_base_v058_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstabs_504d_base_v059_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxyabs_504d_base_v060_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrsqs_5d_base_v061_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstsqs_5d_base_v062_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxysqs_5d_base_v063_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrsqs_10d_base_v064_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstsqs_10d_base_v065_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxysqs_10d_base_v066_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrsqs_21d_base_v067_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstsqs_21d_base_v068_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxysqs_21d_base_v069_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrsqs_42d_base_v070_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstsqs_42d_base_v071_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxysqs_42d_base_v072_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_volbrsqs_63d_base_v073_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_shcstsqs_63d_base_v074_signal,
    f093obe_f093_ownership_breadth_expansion_proxy_brpxysqs_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F093_OWNERSHIP_BREADTH_EXPANSION_PROXY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    marketcap = pd.Series(closeadj * 1e8, name="marketcap")
    dps = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    payoutratio = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    roic = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    cols = {
        "closeadj": closeadj, "volume": volume, "sharesbas": sharesbas,
        "marketcap": marketcap, "dps": dps, "payoutratio": payoutratio,
        "roic": roic,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f093_volume_breadth", "_f093_share_count_stable", "_f093_breadth_proxy")
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
    print(f"OK f093_ownership_breadth_expansion_proxy_base_001_075_claude: {n_features} features pass")
