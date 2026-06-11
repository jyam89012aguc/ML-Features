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


def f042mfi_f042_money_flow_index_tp21x_5d_jerk_v001_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj) * closeadj.rolling(21, min_periods=5).mean()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tp21x_10d_jerk_v002_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj) * closeadj.rolling(21, min_periods=5).mean()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tp21x_21d_jerk_v003_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj) * closeadj.rolling(21, min_periods=5).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tp21x_42d_jerk_v004_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj) * closeadj.rolling(21, min_periods=5).mean()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tp21x_63d_jerk_v005_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj) * closeadj.rolling(21, min_periods=5).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tp21x_126d_jerk_v006_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj) * closeadj.rolling(21, min_periods=5).mean()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tp63x_5d_jerk_v007_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tp63x_10d_jerk_v008_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tp63x_21d_jerk_v009_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tp63x_42d_jerk_v010_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tp63x_63d_jerk_v011_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tp63x_126d_jerk_v012_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tp126x_5d_jerk_v013_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj) * closeadj.rolling(126, min_periods=21).mean()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tp126x_10d_jerk_v014_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj) * closeadj.rolling(126, min_periods=21).mean()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tp126x_21d_jerk_v015_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj) * closeadj.rolling(126, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tp126x_42d_jerk_v016_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj) * closeadj.rolling(126, min_periods=21).mean()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tp126x_63d_jerk_v017_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj) * closeadj.rolling(126, min_periods=21).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tp126x_126d_jerk_v018_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj) * closeadj.rolling(126, min_periods=21).mean()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tp252x_5d_jerk_v019_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj) * closeadj.rolling(252, min_periods=63).mean()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tp252x_10d_jerk_v020_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj) * closeadj.rolling(252, min_periods=63).mean()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tp252x_21d_jerk_v021_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj) * closeadj.rolling(252, min_periods=63).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tp252x_42d_jerk_v022_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj) * closeadj.rolling(252, min_periods=63).mean()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tp252x_63d_jerk_v023_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj) * closeadj.rolling(252, min_periods=63).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tp252x_126d_jerk_v024_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj) * closeadj.rolling(252, min_periods=63).mean()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mf21_5d_jerk_v025_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mf21_10d_jerk_v026_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mf21_21d_jerk_v027_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mf21_42d_jerk_v028_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mf21_63d_jerk_v029_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mf21_126d_jerk_v030_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mf63_5d_jerk_v031_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mf63_10d_jerk_v032_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mf63_21d_jerk_v033_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mf63_42d_jerk_v034_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mf63_63d_jerk_v035_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mf63_126d_jerk_v036_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mf126_5d_jerk_v037_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mf126_10d_jerk_v038_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mf126_21d_jerk_v039_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mf126_42d_jerk_v040_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 126)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mf126_63d_jerk_v041_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mf126_126d_jerk_v042_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 126)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mf252_5d_jerk_v043_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mf252_10d_jerk_v044_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mf252_21d_jerk_v045_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mf252_42d_jerk_v046_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mf252_63d_jerk_v047_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mf252_126d_jerk_v048_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfi21x_5d_jerk_v049_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfi21x_10d_jerk_v050_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfi21x_21d_jerk_v051_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfi21x_42d_jerk_v052_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfi21x_63d_jerk_v053_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfi21x_126d_jerk_v054_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfi63x_5d_jerk_v055_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfi63x_10d_jerk_v056_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfi63x_21d_jerk_v057_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfi63x_42d_jerk_v058_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfi63x_63d_jerk_v059_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfi63x_126d_jerk_v060_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfi126x_5d_jerk_v061_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfi126x_10d_jerk_v062_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 126) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfi126x_21d_jerk_v063_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfi126x_42d_jerk_v064_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 126) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfi126x_63d_jerk_v065_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfi126x_126d_jerk_v066_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfi252x_5d_jerk_v067_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfi252x_10d_jerk_v068_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfi252x_21d_jerk_v069_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfi252x_42d_jerk_v070_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfi252x_63d_jerk_v071_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfi252x_126d_jerk_v072_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfidev21_5d_jerk_v073_signal(high, low, closeadj, volume):
    base = (_f042_mfi(high, low, closeadj, volume, 21) - 50.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfidev21_10d_jerk_v074_signal(high, low, closeadj, volume):
    base = (_f042_mfi(high, low, closeadj, volume, 21) - 50.0) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfidev21_21d_jerk_v075_signal(high, low, closeadj, volume):
    base = (_f042_mfi(high, low, closeadj, volume, 21) - 50.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfidev21_42d_jerk_v076_signal(high, low, closeadj, volume):
    base = (_f042_mfi(high, low, closeadj, volume, 21) - 50.0) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfidev21_63d_jerk_v077_signal(high, low, closeadj, volume):
    base = (_f042_mfi(high, low, closeadj, volume, 21) - 50.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfidev21_126d_jerk_v078_signal(high, low, closeadj, volume):
    base = (_f042_mfi(high, low, closeadj, volume, 21) - 50.0) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfidev63_5d_jerk_v079_signal(high, low, closeadj, volume):
    base = (_f042_mfi(high, low, closeadj, volume, 63) - 50.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfidev63_10d_jerk_v080_signal(high, low, closeadj, volume):
    base = (_f042_mfi(high, low, closeadj, volume, 63) - 50.0) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfidev63_21d_jerk_v081_signal(high, low, closeadj, volume):
    base = (_f042_mfi(high, low, closeadj, volume, 63) - 50.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfidev63_42d_jerk_v082_signal(high, low, closeadj, volume):
    base = (_f042_mfi(high, low, closeadj, volume, 63) - 50.0) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfidev63_63d_jerk_v083_signal(high, low, closeadj, volume):
    base = (_f042_mfi(high, low, closeadj, volume, 63) - 50.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfidev63_126d_jerk_v084_signal(high, low, closeadj, volume):
    base = (_f042_mfi(high, low, closeadj, volume, 63) - 50.0) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfidev252_5d_jerk_v085_signal(high, low, closeadj, volume):
    base = (_f042_mfi(high, low, closeadj, volume, 252) - 50.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfidev252_10d_jerk_v086_signal(high, low, closeadj, volume):
    base = (_f042_mfi(high, low, closeadj, volume, 252) - 50.0) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfidev252_21d_jerk_v087_signal(high, low, closeadj, volume):
    base = (_f042_mfi(high, low, closeadj, volume, 252) - 50.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfidev252_42d_jerk_v088_signal(high, low, closeadj, volume):
    base = (_f042_mfi(high, low, closeadj, volume, 252) - 50.0) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfidev252_63d_jerk_v089_signal(high, low, closeadj, volume):
    base = (_f042_mfi(high, low, closeadj, volume, 252) - 50.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfidev252_126d_jerk_v090_signal(high, low, closeadj, volume):
    base = (_f042_mfi(high, low, closeadj, volume, 252) - 50.0) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfxvol21_5d_jerk_v091_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 21) / volume.rolling(21, min_periods=5).mean().replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfxvol21_10d_jerk_v092_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 21) / volume.rolling(21, min_periods=5).mean().replace(0, np.nan)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfxvol21_21d_jerk_v093_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 21) / volume.rolling(21, min_periods=5).mean().replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfxvol21_42d_jerk_v094_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 21) / volume.rolling(21, min_periods=5).mean().replace(0, np.nan)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfxvol21_63d_jerk_v095_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 21) / volume.rolling(21, min_periods=5).mean().replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfxvol21_126d_jerk_v096_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 21) / volume.rolling(21, min_periods=5).mean().replace(0, np.nan)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfxvol63_5d_jerk_v097_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 63) / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfxvol63_10d_jerk_v098_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 63) / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfxvol63_21d_jerk_v099_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 63) / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfxvol63_42d_jerk_v100_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 63) / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfxvol63_63d_jerk_v101_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 63) / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfxvol63_126d_jerk_v102_signal(high, low, closeadj, volume):
    base = _f042_money_flow(high, low, closeadj, volume, 63) / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_logmf21_5d_jerk_v103_signal(high, low, closeadj, volume):
    base = np.log1p(_f042_money_flow(high, low, closeadj, volume, 21).abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_logmf21_10d_jerk_v104_signal(high, low, closeadj, volume):
    base = np.log1p(_f042_money_flow(high, low, closeadj, volume, 21).abs())
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_logmf21_21d_jerk_v105_signal(high, low, closeadj, volume):
    base = np.log1p(_f042_money_flow(high, low, closeadj, volume, 21).abs())
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_logmf21_42d_jerk_v106_signal(high, low, closeadj, volume):
    base = np.log1p(_f042_money_flow(high, low, closeadj, volume, 21).abs())
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_logmf21_63d_jerk_v107_signal(high, low, closeadj, volume):
    base = np.log1p(_f042_money_flow(high, low, closeadj, volume, 21).abs())
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_logmf21_126d_jerk_v108_signal(high, low, closeadj, volume):
    base = np.log1p(_f042_money_flow(high, low, closeadj, volume, 21).abs())
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_logmf63_5d_jerk_v109_signal(high, low, closeadj, volume):
    base = np.log1p(_f042_money_flow(high, low, closeadj, volume, 63).abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_logmf63_10d_jerk_v110_signal(high, low, closeadj, volume):
    base = np.log1p(_f042_money_flow(high, low, closeadj, volume, 63).abs())
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_logmf63_21d_jerk_v111_signal(high, low, closeadj, volume):
    base = np.log1p(_f042_money_flow(high, low, closeadj, volume, 63).abs())
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_logmf63_42d_jerk_v112_signal(high, low, closeadj, volume):
    base = np.log1p(_f042_money_flow(high, low, closeadj, volume, 63).abs())
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_logmf63_63d_jerk_v113_signal(high, low, closeadj, volume):
    base = np.log1p(_f042_money_flow(high, low, closeadj, volume, 63).abs())
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_logmf63_126d_jerk_v114_signal(high, low, closeadj, volume):
    base = np.log1p(_f042_money_flow(high, low, closeadj, volume, 63).abs())
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_logmf252_5d_jerk_v115_signal(high, low, closeadj, volume):
    base = np.log1p(_f042_money_flow(high, low, closeadj, volume, 252).abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_logmf252_10d_jerk_v116_signal(high, low, closeadj, volume):
    base = np.log1p(_f042_money_flow(high, low, closeadj, volume, 252).abs())
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_logmf252_21d_jerk_v117_signal(high, low, closeadj, volume):
    base = np.log1p(_f042_money_flow(high, low, closeadj, volume, 252).abs())
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_logmf252_42d_jerk_v118_signal(high, low, closeadj, volume):
    base = np.log1p(_f042_money_flow(high, low, closeadj, volume, 252).abs())
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_logmf252_63d_jerk_v119_signal(high, low, closeadj, volume):
    base = np.log1p(_f042_money_flow(high, low, closeadj, volume, 252).abs())
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_logmf252_126d_jerk_v120_signal(high, low, closeadj, volume):
    base = np.log1p(_f042_money_flow(high, low, closeadj, volume, 252).abs())
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfizscr21_5d_jerk_v121_signal(high, low, closeadj, volume):
    base = _z(_f042_mfi(high, low, closeadj, volume, 21), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfizscr21_10d_jerk_v122_signal(high, low, closeadj, volume):
    base = _z(_f042_mfi(high, low, closeadj, volume, 21), 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfizscr21_21d_jerk_v123_signal(high, low, closeadj, volume):
    base = _z(_f042_mfi(high, low, closeadj, volume, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfizscr21_42d_jerk_v124_signal(high, low, closeadj, volume):
    base = _z(_f042_mfi(high, low, closeadj, volume, 21), 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfizscr21_63d_jerk_v125_signal(high, low, closeadj, volume):
    base = _z(_f042_mfi(high, low, closeadj, volume, 21), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfizscr21_126d_jerk_v126_signal(high, low, closeadj, volume):
    base = _z(_f042_mfi(high, low, closeadj, volume, 21), 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfizscr63_5d_jerk_v127_signal(high, low, closeadj, volume):
    base = _z(_f042_mfi(high, low, closeadj, volume, 63), 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfizscr63_10d_jerk_v128_signal(high, low, closeadj, volume):
    base = _z(_f042_mfi(high, low, closeadj, volume, 63), 126) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfizscr63_21d_jerk_v129_signal(high, low, closeadj, volume):
    base = _z(_f042_mfi(high, low, closeadj, volume, 63), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfizscr63_42d_jerk_v130_signal(high, low, closeadj, volume):
    base = _z(_f042_mfi(high, low, closeadj, volume, 63), 126) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfizscr63_63d_jerk_v131_signal(high, low, closeadj, volume):
    base = _z(_f042_mfi(high, low, closeadj, volume, 63), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfizscr63_126d_jerk_v132_signal(high, low, closeadj, volume):
    base = _z(_f042_mfi(high, low, closeadj, volume, 63), 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfiemavg21_5d_jerk_v133_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfiemavg21_10d_jerk_v134_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfiemavg21_21d_jerk_v135_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfiemavg21_42d_jerk_v136_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfiemavg21_63d_jerk_v137_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfiemavg21_126d_jerk_v138_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfiemavg63_5d_jerk_v139_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfiemavg63_10d_jerk_v140_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfiemavg63_21d_jerk_v141_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfiemavg63_42d_jerk_v142_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfiemavg63_63d_jerk_v143_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_mfiemavg63_126d_jerk_v144_signal(high, low, closeadj, volume):
    base = _f042_mfi(high, low, closeadj, volume, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tpdiff21_5d_jerk_v145_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj).diff(21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tpdiff21_10d_jerk_v146_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj).diff(21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tpdiff21_21d_jerk_v147_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj).diff(21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tpdiff21_42d_jerk_v148_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj).diff(21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tpdiff21_63d_jerk_v149_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj).diff(21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f042mfi_f042_money_flow_index_tpdiff21_126d_jerk_v150_signal(high, low, closeadj):
    base = _f042_typical_price(high, low, closeadj).diff(21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f042mfi_f042_money_flow_index_tp21x_5d_jerk_v001_signal,
    f042mfi_f042_money_flow_index_tp21x_10d_jerk_v002_signal,
    f042mfi_f042_money_flow_index_tp21x_21d_jerk_v003_signal,
    f042mfi_f042_money_flow_index_tp21x_42d_jerk_v004_signal,
    f042mfi_f042_money_flow_index_tp21x_63d_jerk_v005_signal,
    f042mfi_f042_money_flow_index_tp21x_126d_jerk_v006_signal,
    f042mfi_f042_money_flow_index_tp63x_5d_jerk_v007_signal,
    f042mfi_f042_money_flow_index_tp63x_10d_jerk_v008_signal,
    f042mfi_f042_money_flow_index_tp63x_21d_jerk_v009_signal,
    f042mfi_f042_money_flow_index_tp63x_42d_jerk_v010_signal,
    f042mfi_f042_money_flow_index_tp63x_63d_jerk_v011_signal,
    f042mfi_f042_money_flow_index_tp63x_126d_jerk_v012_signal,
    f042mfi_f042_money_flow_index_tp126x_5d_jerk_v013_signal,
    f042mfi_f042_money_flow_index_tp126x_10d_jerk_v014_signal,
    f042mfi_f042_money_flow_index_tp126x_21d_jerk_v015_signal,
    f042mfi_f042_money_flow_index_tp126x_42d_jerk_v016_signal,
    f042mfi_f042_money_flow_index_tp126x_63d_jerk_v017_signal,
    f042mfi_f042_money_flow_index_tp126x_126d_jerk_v018_signal,
    f042mfi_f042_money_flow_index_tp252x_5d_jerk_v019_signal,
    f042mfi_f042_money_flow_index_tp252x_10d_jerk_v020_signal,
    f042mfi_f042_money_flow_index_tp252x_21d_jerk_v021_signal,
    f042mfi_f042_money_flow_index_tp252x_42d_jerk_v022_signal,
    f042mfi_f042_money_flow_index_tp252x_63d_jerk_v023_signal,
    f042mfi_f042_money_flow_index_tp252x_126d_jerk_v024_signal,
    f042mfi_f042_money_flow_index_mf21_5d_jerk_v025_signal,
    f042mfi_f042_money_flow_index_mf21_10d_jerk_v026_signal,
    f042mfi_f042_money_flow_index_mf21_21d_jerk_v027_signal,
    f042mfi_f042_money_flow_index_mf21_42d_jerk_v028_signal,
    f042mfi_f042_money_flow_index_mf21_63d_jerk_v029_signal,
    f042mfi_f042_money_flow_index_mf21_126d_jerk_v030_signal,
    f042mfi_f042_money_flow_index_mf63_5d_jerk_v031_signal,
    f042mfi_f042_money_flow_index_mf63_10d_jerk_v032_signal,
    f042mfi_f042_money_flow_index_mf63_21d_jerk_v033_signal,
    f042mfi_f042_money_flow_index_mf63_42d_jerk_v034_signal,
    f042mfi_f042_money_flow_index_mf63_63d_jerk_v035_signal,
    f042mfi_f042_money_flow_index_mf63_126d_jerk_v036_signal,
    f042mfi_f042_money_flow_index_mf126_5d_jerk_v037_signal,
    f042mfi_f042_money_flow_index_mf126_10d_jerk_v038_signal,
    f042mfi_f042_money_flow_index_mf126_21d_jerk_v039_signal,
    f042mfi_f042_money_flow_index_mf126_42d_jerk_v040_signal,
    f042mfi_f042_money_flow_index_mf126_63d_jerk_v041_signal,
    f042mfi_f042_money_flow_index_mf126_126d_jerk_v042_signal,
    f042mfi_f042_money_flow_index_mf252_5d_jerk_v043_signal,
    f042mfi_f042_money_flow_index_mf252_10d_jerk_v044_signal,
    f042mfi_f042_money_flow_index_mf252_21d_jerk_v045_signal,
    f042mfi_f042_money_flow_index_mf252_42d_jerk_v046_signal,
    f042mfi_f042_money_flow_index_mf252_63d_jerk_v047_signal,
    f042mfi_f042_money_flow_index_mf252_126d_jerk_v048_signal,
    f042mfi_f042_money_flow_index_mfi21x_5d_jerk_v049_signal,
    f042mfi_f042_money_flow_index_mfi21x_10d_jerk_v050_signal,
    f042mfi_f042_money_flow_index_mfi21x_21d_jerk_v051_signal,
    f042mfi_f042_money_flow_index_mfi21x_42d_jerk_v052_signal,
    f042mfi_f042_money_flow_index_mfi21x_63d_jerk_v053_signal,
    f042mfi_f042_money_flow_index_mfi21x_126d_jerk_v054_signal,
    f042mfi_f042_money_flow_index_mfi63x_5d_jerk_v055_signal,
    f042mfi_f042_money_flow_index_mfi63x_10d_jerk_v056_signal,
    f042mfi_f042_money_flow_index_mfi63x_21d_jerk_v057_signal,
    f042mfi_f042_money_flow_index_mfi63x_42d_jerk_v058_signal,
    f042mfi_f042_money_flow_index_mfi63x_63d_jerk_v059_signal,
    f042mfi_f042_money_flow_index_mfi63x_126d_jerk_v060_signal,
    f042mfi_f042_money_flow_index_mfi126x_5d_jerk_v061_signal,
    f042mfi_f042_money_flow_index_mfi126x_10d_jerk_v062_signal,
    f042mfi_f042_money_flow_index_mfi126x_21d_jerk_v063_signal,
    f042mfi_f042_money_flow_index_mfi126x_42d_jerk_v064_signal,
    f042mfi_f042_money_flow_index_mfi126x_63d_jerk_v065_signal,
    f042mfi_f042_money_flow_index_mfi126x_126d_jerk_v066_signal,
    f042mfi_f042_money_flow_index_mfi252x_5d_jerk_v067_signal,
    f042mfi_f042_money_flow_index_mfi252x_10d_jerk_v068_signal,
    f042mfi_f042_money_flow_index_mfi252x_21d_jerk_v069_signal,
    f042mfi_f042_money_flow_index_mfi252x_42d_jerk_v070_signal,
    f042mfi_f042_money_flow_index_mfi252x_63d_jerk_v071_signal,
    f042mfi_f042_money_flow_index_mfi252x_126d_jerk_v072_signal,
    f042mfi_f042_money_flow_index_mfidev21_5d_jerk_v073_signal,
    f042mfi_f042_money_flow_index_mfidev21_10d_jerk_v074_signal,
    f042mfi_f042_money_flow_index_mfidev21_21d_jerk_v075_signal,
    f042mfi_f042_money_flow_index_mfidev21_42d_jerk_v076_signal,
    f042mfi_f042_money_flow_index_mfidev21_63d_jerk_v077_signal,
    f042mfi_f042_money_flow_index_mfidev21_126d_jerk_v078_signal,
    f042mfi_f042_money_flow_index_mfidev63_5d_jerk_v079_signal,
    f042mfi_f042_money_flow_index_mfidev63_10d_jerk_v080_signal,
    f042mfi_f042_money_flow_index_mfidev63_21d_jerk_v081_signal,
    f042mfi_f042_money_flow_index_mfidev63_42d_jerk_v082_signal,
    f042mfi_f042_money_flow_index_mfidev63_63d_jerk_v083_signal,
    f042mfi_f042_money_flow_index_mfidev63_126d_jerk_v084_signal,
    f042mfi_f042_money_flow_index_mfidev252_5d_jerk_v085_signal,
    f042mfi_f042_money_flow_index_mfidev252_10d_jerk_v086_signal,
    f042mfi_f042_money_flow_index_mfidev252_21d_jerk_v087_signal,
    f042mfi_f042_money_flow_index_mfidev252_42d_jerk_v088_signal,
    f042mfi_f042_money_flow_index_mfidev252_63d_jerk_v089_signal,
    f042mfi_f042_money_flow_index_mfidev252_126d_jerk_v090_signal,
    f042mfi_f042_money_flow_index_mfxvol21_5d_jerk_v091_signal,
    f042mfi_f042_money_flow_index_mfxvol21_10d_jerk_v092_signal,
    f042mfi_f042_money_flow_index_mfxvol21_21d_jerk_v093_signal,
    f042mfi_f042_money_flow_index_mfxvol21_42d_jerk_v094_signal,
    f042mfi_f042_money_flow_index_mfxvol21_63d_jerk_v095_signal,
    f042mfi_f042_money_flow_index_mfxvol21_126d_jerk_v096_signal,
    f042mfi_f042_money_flow_index_mfxvol63_5d_jerk_v097_signal,
    f042mfi_f042_money_flow_index_mfxvol63_10d_jerk_v098_signal,
    f042mfi_f042_money_flow_index_mfxvol63_21d_jerk_v099_signal,
    f042mfi_f042_money_flow_index_mfxvol63_42d_jerk_v100_signal,
    f042mfi_f042_money_flow_index_mfxvol63_63d_jerk_v101_signal,
    f042mfi_f042_money_flow_index_mfxvol63_126d_jerk_v102_signal,
    f042mfi_f042_money_flow_index_logmf21_5d_jerk_v103_signal,
    f042mfi_f042_money_flow_index_logmf21_10d_jerk_v104_signal,
    f042mfi_f042_money_flow_index_logmf21_21d_jerk_v105_signal,
    f042mfi_f042_money_flow_index_logmf21_42d_jerk_v106_signal,
    f042mfi_f042_money_flow_index_logmf21_63d_jerk_v107_signal,
    f042mfi_f042_money_flow_index_logmf21_126d_jerk_v108_signal,
    f042mfi_f042_money_flow_index_logmf63_5d_jerk_v109_signal,
    f042mfi_f042_money_flow_index_logmf63_10d_jerk_v110_signal,
    f042mfi_f042_money_flow_index_logmf63_21d_jerk_v111_signal,
    f042mfi_f042_money_flow_index_logmf63_42d_jerk_v112_signal,
    f042mfi_f042_money_flow_index_logmf63_63d_jerk_v113_signal,
    f042mfi_f042_money_flow_index_logmf63_126d_jerk_v114_signal,
    f042mfi_f042_money_flow_index_logmf252_5d_jerk_v115_signal,
    f042mfi_f042_money_flow_index_logmf252_10d_jerk_v116_signal,
    f042mfi_f042_money_flow_index_logmf252_21d_jerk_v117_signal,
    f042mfi_f042_money_flow_index_logmf252_42d_jerk_v118_signal,
    f042mfi_f042_money_flow_index_logmf252_63d_jerk_v119_signal,
    f042mfi_f042_money_flow_index_logmf252_126d_jerk_v120_signal,
    f042mfi_f042_money_flow_index_mfizscr21_5d_jerk_v121_signal,
    f042mfi_f042_money_flow_index_mfizscr21_10d_jerk_v122_signal,
    f042mfi_f042_money_flow_index_mfizscr21_21d_jerk_v123_signal,
    f042mfi_f042_money_flow_index_mfizscr21_42d_jerk_v124_signal,
    f042mfi_f042_money_flow_index_mfizscr21_63d_jerk_v125_signal,
    f042mfi_f042_money_flow_index_mfizscr21_126d_jerk_v126_signal,
    f042mfi_f042_money_flow_index_mfizscr63_5d_jerk_v127_signal,
    f042mfi_f042_money_flow_index_mfizscr63_10d_jerk_v128_signal,
    f042mfi_f042_money_flow_index_mfizscr63_21d_jerk_v129_signal,
    f042mfi_f042_money_flow_index_mfizscr63_42d_jerk_v130_signal,
    f042mfi_f042_money_flow_index_mfizscr63_63d_jerk_v131_signal,
    f042mfi_f042_money_flow_index_mfizscr63_126d_jerk_v132_signal,
    f042mfi_f042_money_flow_index_mfiemavg21_5d_jerk_v133_signal,
    f042mfi_f042_money_flow_index_mfiemavg21_10d_jerk_v134_signal,
    f042mfi_f042_money_flow_index_mfiemavg21_21d_jerk_v135_signal,
    f042mfi_f042_money_flow_index_mfiemavg21_42d_jerk_v136_signal,
    f042mfi_f042_money_flow_index_mfiemavg21_63d_jerk_v137_signal,
    f042mfi_f042_money_flow_index_mfiemavg21_126d_jerk_v138_signal,
    f042mfi_f042_money_flow_index_mfiemavg63_5d_jerk_v139_signal,
    f042mfi_f042_money_flow_index_mfiemavg63_10d_jerk_v140_signal,
    f042mfi_f042_money_flow_index_mfiemavg63_21d_jerk_v141_signal,
    f042mfi_f042_money_flow_index_mfiemavg63_42d_jerk_v142_signal,
    f042mfi_f042_money_flow_index_mfiemavg63_63d_jerk_v143_signal,
    f042mfi_f042_money_flow_index_mfiemavg63_126d_jerk_v144_signal,
    f042mfi_f042_money_flow_index_tpdiff21_5d_jerk_v145_signal,
    f042mfi_f042_money_flow_index_tpdiff21_10d_jerk_v146_signal,
    f042mfi_f042_money_flow_index_tpdiff21_21d_jerk_v147_signal,
    f042mfi_f042_money_flow_index_tpdiff21_42d_jerk_v148_signal,
    f042mfi_f042_money_flow_index_tpdiff21_63d_jerk_v149_signal,
    f042mfi_f042_money_flow_index_tpdiff21_126d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F042_MONEY_FLOW_INDEX_REGISTRY_JERK_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK {__file__}: {n_features} features pass")
