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
def _f042_typical_price(high, low, closeadj):
    return (high + low + closeadj) / 3.0


def _f042_money_flow(high, low, closeadj, volume, w):
    tp = (high + low + closeadj) / 3.0
    mf = tp * volume
    return mf.rolling(w, min_periods=max(1, w // 2)).sum()


def _f042_mfi(high, low, closeadj, volume, w):
    tp = (high + low + closeadj) / 3.0
    mf = tp * volume
    delta_tp = tp.diff()
    pos = mf.where(delta_tp > 0, 0.0)
    neg = mf.where(delta_tp < 0, 0.0)
    pos_sum = pos.rolling(w, min_periods=max(1, w // 2)).sum()
    neg_sum = neg.rolling(w, min_periods=max(1, w // 2)).sum()
    mr = pos_sum / neg_sum.replace(0, np.nan)
    return 100.0 - (100.0 / (1.0 + mr))

def f042mfi_f042_money_flow_index_tpraw_5d_base_v001_signal(high, low, closeadj, volume):
    base = _z(_f042_typical_price(high, low, closeadj), 5)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfraw_5d_base_v002_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 5)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfiraw_5d_base_v003_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 5)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_tpraw_10d_base_v004_signal(high, low, closeadj, volume):
    base = _z(_f042_typical_price(high, low, closeadj), 10)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfraw_10d_base_v005_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 10)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfiraw_10d_base_v006_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 10)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_tpraw_21d_base_v007_signal(high, low, closeadj, volume):
    base = _z(_f042_typical_price(high, low, closeadj), 21)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfraw_21d_base_v008_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 21)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfiraw_21d_base_v009_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 21)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_tpraw_42d_base_v010_signal(high, low, closeadj, volume):
    base = _z(_f042_typical_price(high, low, closeadj), 42)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfraw_42d_base_v011_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 42)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfiraw_42d_base_v012_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 42)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_tpraw_63d_base_v013_signal(high, low, closeadj, volume):
    base = _z(_f042_typical_price(high, low, closeadj), 63)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfraw_63d_base_v014_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 63)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfiraw_63d_base_v015_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 63)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_tpraw_126d_base_v016_signal(high, low, closeadj, volume):
    base = _z(_f042_typical_price(high, low, closeadj), 126)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfraw_126d_base_v017_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 126)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfiraw_126d_base_v018_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 126)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_tpraw_189d_base_v019_signal(high, low, closeadj, volume):
    base = _z(_f042_typical_price(high, low, closeadj), 189)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfraw_189d_base_v020_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 189)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfiraw_189d_base_v021_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 189)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_tpraw_252d_base_v022_signal(high, low, closeadj, volume):
    base = _z(_f042_typical_price(high, low, closeadj), 252)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfraw_252d_base_v023_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 252)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfiraw_252d_base_v024_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 252)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_tpraw_378d_base_v025_signal(high, low, closeadj, volume):
    base = _z(_f042_typical_price(high, low, closeadj), 378)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfraw_378d_base_v026_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 378)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfiraw_378d_base_v027_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 378)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_tpraw_504d_base_v028_signal(high, low, closeadj, volume):
    base = _z(_f042_typical_price(high, low, closeadj), 504)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfraw_504d_base_v029_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 504)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfiraw_504d_base_v030_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 504)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_tpabs_5d_base_v031_signal(high, low, closeadj, volume):
    base = _z(_f042_typical_price(high, low, closeadj), 5)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfabs_5d_base_v032_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 5)
    result = _z(base, 252).abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfiabs_5d_base_v033_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 5)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_tpabs_10d_base_v034_signal(high, low, closeadj, volume):
    base = _z(_f042_typical_price(high, low, closeadj), 10)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfabs_10d_base_v035_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 10)
    result = _z(base, 252).abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfiabs_10d_base_v036_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 10)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_tpabs_21d_base_v037_signal(high, low, closeadj, volume):
    base = _z(_f042_typical_price(high, low, closeadj), 21)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfabs_21d_base_v038_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 21)
    result = _z(base, 252).abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfiabs_21d_base_v039_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 21)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_tpabs_42d_base_v040_signal(high, low, closeadj, volume):
    base = _z(_f042_typical_price(high, low, closeadj), 42)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfabs_42d_base_v041_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 42)
    result = _z(base, 252).abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfiabs_42d_base_v042_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 42)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_tpabs_63d_base_v043_signal(high, low, closeadj, volume):
    base = _z(_f042_typical_price(high, low, closeadj), 63)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfabs_63d_base_v044_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 63)
    result = _z(base, 252).abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfiabs_63d_base_v045_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 63)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_tpabs_126d_base_v046_signal(high, low, closeadj, volume):
    base = _z(_f042_typical_price(high, low, closeadj), 126)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfabs_126d_base_v047_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 126)
    result = _z(base, 252).abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfiabs_126d_base_v048_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 126)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_tpabs_189d_base_v049_signal(high, low, closeadj, volume):
    base = _z(_f042_typical_price(high, low, closeadj), 189)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfabs_189d_base_v050_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 189)
    result = _z(base, 252).abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfiabs_189d_base_v051_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 189)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_tpabs_252d_base_v052_signal(high, low, closeadj, volume):
    base = _z(_f042_typical_price(high, low, closeadj), 252)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfabs_252d_base_v053_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 252)
    result = _z(base, 252).abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfiabs_252d_base_v054_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 252)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_tpabs_378d_base_v055_signal(high, low, closeadj, volume):
    base = _z(_f042_typical_price(high, low, closeadj), 378)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfabs_378d_base_v056_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 378)
    result = _z(base, 252).abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfiabs_378d_base_v057_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 378)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_tpabs_504d_base_v058_signal(high, low, closeadj, volume):
    base = _z(_f042_typical_price(high, low, closeadj), 504)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfabs_504d_base_v059_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 504)
    result = _z(base, 252).abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfiabs_504d_base_v060_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 504)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_tpsqrt_5d_base_v061_signal(high, low, closeadj, volume):
    base = _z(_f042_typical_price(high, low, closeadj), 5)
    result = np.sign(base) * base.abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfsqrt_5d_base_v062_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 5)
    result = np.sign(_z(base, 252)) * _z(base, 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfisqrt_5d_base_v063_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 5)
    result = np.sign(base) * base.abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_tpsqrt_10d_base_v064_signal(high, low, closeadj, volume):
    base = _z(_f042_typical_price(high, low, closeadj), 10)
    result = np.sign(base) * base.abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfsqrt_10d_base_v065_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 10)
    result = np.sign(_z(base, 252)) * _z(base, 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfisqrt_10d_base_v066_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 10)
    result = np.sign(base) * base.abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_tpsqrt_21d_base_v067_signal(high, low, closeadj, volume):
    base = _z(_f042_typical_price(high, low, closeadj), 21)
    result = np.sign(base) * base.abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfsqrt_21d_base_v068_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 21)
    result = np.sign(_z(base, 252)) * _z(base, 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfisqrt_21d_base_v069_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 21)
    result = np.sign(base) * base.abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_tpsqrt_42d_base_v070_signal(high, low, closeadj, volume):
    base = _z(_f042_typical_price(high, low, closeadj), 42)
    result = np.sign(base) * base.abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfsqrt_42d_base_v071_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 42)
    result = np.sign(_z(base, 252)) * _z(base, 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfisqrt_42d_base_v072_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 42)
    result = np.sign(base) * base.abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_tpsqrt_63d_base_v073_signal(high, low, closeadj, volume):
    base = _z(_f042_typical_price(high, low, closeadj), 63)
    result = np.sign(base) * base.abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfsqrt_63d_base_v074_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 63)
    result = np.sign(_z(base, 252)) * _z(base, 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f042mfi_f042_money_flow_index_mfisqrt_63d_base_v075_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 63)
    result = np.sign(base) * base.abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f042mfi_f042_money_flow_index_tpraw_5d_base_v001_signal,
    f042mfi_f042_money_flow_index_mfraw_5d_base_v002_signal,
    f042mfi_f042_money_flow_index_mfiraw_5d_base_v003_signal,
    f042mfi_f042_money_flow_index_tpraw_10d_base_v004_signal,
    f042mfi_f042_money_flow_index_mfraw_10d_base_v005_signal,
    f042mfi_f042_money_flow_index_mfiraw_10d_base_v006_signal,
    f042mfi_f042_money_flow_index_tpraw_21d_base_v007_signal,
    f042mfi_f042_money_flow_index_mfraw_21d_base_v008_signal,
    f042mfi_f042_money_flow_index_mfiraw_21d_base_v009_signal,
    f042mfi_f042_money_flow_index_tpraw_42d_base_v010_signal,
    f042mfi_f042_money_flow_index_mfraw_42d_base_v011_signal,
    f042mfi_f042_money_flow_index_mfiraw_42d_base_v012_signal,
    f042mfi_f042_money_flow_index_tpraw_63d_base_v013_signal,
    f042mfi_f042_money_flow_index_mfraw_63d_base_v014_signal,
    f042mfi_f042_money_flow_index_mfiraw_63d_base_v015_signal,
    f042mfi_f042_money_flow_index_tpraw_126d_base_v016_signal,
    f042mfi_f042_money_flow_index_mfraw_126d_base_v017_signal,
    f042mfi_f042_money_flow_index_mfiraw_126d_base_v018_signal,
    f042mfi_f042_money_flow_index_tpraw_189d_base_v019_signal,
    f042mfi_f042_money_flow_index_mfraw_189d_base_v020_signal,
    f042mfi_f042_money_flow_index_mfiraw_189d_base_v021_signal,
    f042mfi_f042_money_flow_index_tpraw_252d_base_v022_signal,
    f042mfi_f042_money_flow_index_mfraw_252d_base_v023_signal,
    f042mfi_f042_money_flow_index_mfiraw_252d_base_v024_signal,
    f042mfi_f042_money_flow_index_tpraw_378d_base_v025_signal,
    f042mfi_f042_money_flow_index_mfraw_378d_base_v026_signal,
    f042mfi_f042_money_flow_index_mfiraw_378d_base_v027_signal,
    f042mfi_f042_money_flow_index_tpraw_504d_base_v028_signal,
    f042mfi_f042_money_flow_index_mfraw_504d_base_v029_signal,
    f042mfi_f042_money_flow_index_mfiraw_504d_base_v030_signal,
    f042mfi_f042_money_flow_index_tpabs_5d_base_v031_signal,
    f042mfi_f042_money_flow_index_mfabs_5d_base_v032_signal,
    f042mfi_f042_money_flow_index_mfiabs_5d_base_v033_signal,
    f042mfi_f042_money_flow_index_tpabs_10d_base_v034_signal,
    f042mfi_f042_money_flow_index_mfabs_10d_base_v035_signal,
    f042mfi_f042_money_flow_index_mfiabs_10d_base_v036_signal,
    f042mfi_f042_money_flow_index_tpabs_21d_base_v037_signal,
    f042mfi_f042_money_flow_index_mfabs_21d_base_v038_signal,
    f042mfi_f042_money_flow_index_mfiabs_21d_base_v039_signal,
    f042mfi_f042_money_flow_index_tpabs_42d_base_v040_signal,
    f042mfi_f042_money_flow_index_mfabs_42d_base_v041_signal,
    f042mfi_f042_money_flow_index_mfiabs_42d_base_v042_signal,
    f042mfi_f042_money_flow_index_tpabs_63d_base_v043_signal,
    f042mfi_f042_money_flow_index_mfabs_63d_base_v044_signal,
    f042mfi_f042_money_flow_index_mfiabs_63d_base_v045_signal,
    f042mfi_f042_money_flow_index_tpabs_126d_base_v046_signal,
    f042mfi_f042_money_flow_index_mfabs_126d_base_v047_signal,
    f042mfi_f042_money_flow_index_mfiabs_126d_base_v048_signal,
    f042mfi_f042_money_flow_index_tpabs_189d_base_v049_signal,
    f042mfi_f042_money_flow_index_mfabs_189d_base_v050_signal,
    f042mfi_f042_money_flow_index_mfiabs_189d_base_v051_signal,
    f042mfi_f042_money_flow_index_tpabs_252d_base_v052_signal,
    f042mfi_f042_money_flow_index_mfabs_252d_base_v053_signal,
    f042mfi_f042_money_flow_index_mfiabs_252d_base_v054_signal,
    f042mfi_f042_money_flow_index_tpabs_378d_base_v055_signal,
    f042mfi_f042_money_flow_index_mfabs_378d_base_v056_signal,
    f042mfi_f042_money_flow_index_mfiabs_378d_base_v057_signal,
    f042mfi_f042_money_flow_index_tpabs_504d_base_v058_signal,
    f042mfi_f042_money_flow_index_mfabs_504d_base_v059_signal,
    f042mfi_f042_money_flow_index_mfiabs_504d_base_v060_signal,
    f042mfi_f042_money_flow_index_tpsqrt_5d_base_v061_signal,
    f042mfi_f042_money_flow_index_mfsqrt_5d_base_v062_signal,
    f042mfi_f042_money_flow_index_mfisqrt_5d_base_v063_signal,
    f042mfi_f042_money_flow_index_tpsqrt_10d_base_v064_signal,
    f042mfi_f042_money_flow_index_mfsqrt_10d_base_v065_signal,
    f042mfi_f042_money_flow_index_mfisqrt_10d_base_v066_signal,
    f042mfi_f042_money_flow_index_tpsqrt_21d_base_v067_signal,
    f042mfi_f042_money_flow_index_mfsqrt_21d_base_v068_signal,
    f042mfi_f042_money_flow_index_mfisqrt_21d_base_v069_signal,
    f042mfi_f042_money_flow_index_tpsqrt_42d_base_v070_signal,
    f042mfi_f042_money_flow_index_mfsqrt_42d_base_v071_signal,
    f042mfi_f042_money_flow_index_mfisqrt_42d_base_v072_signal,
    f042mfi_f042_money_flow_index_tpsqrt_63d_base_v073_signal,
    f042mfi_f042_money_flow_index_mfsqrt_63d_base_v074_signal,
    f042mfi_f042_money_flow_index_mfisqrt_63d_base_v075_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F042_MONEY_FLOW_INDEX_REGISTRY_001_075 = REGISTRY



if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = pd.Series((100.0 * np.exp(np.cumsum(rets))) * (1.0 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series((100.0 * np.exp(np.cumsum(rets))) * (1.0 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"high": high, "low": low, "closeadj": closeadj, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f042_typical_price", "_f042_money_flow", "_f042_mfi")
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
