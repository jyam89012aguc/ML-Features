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
def _f045_self_return(closeadj, w):
    return closeadj.pct_change(periods=w)


def _f045_smoothed_return(closeadj, w):
    return closeadj.pct_change(periods=w).rolling(w, min_periods=max(1, w // 2)).mean()


def _f045_rs_score(closeadj, w):
    r = closeadj.pct_change(periods=w)
    rm = r.rolling(252, min_periods=63).mean()
    rs = r.rolling(252, min_periods=63).std()
    return ((r - rm) / rs.replace(0, np.nan)) * closeadj


def f045rsm_f045_relative_strength_market_sret21x_5d_jerk_v001_signal(closeadj):
    base = _f045_self_return(closeadj, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_sret21x_10d_jerk_v002_signal(closeadj):
    base = _f045_self_return(closeadj, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_sret21x_21d_jerk_v003_signal(closeadj):
    base = _f045_self_return(closeadj, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_sret21x_42d_jerk_v004_signal(closeadj):
    base = _f045_self_return(closeadj, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_sret21x_63d_jerk_v005_signal(closeadj):
    base = _f045_self_return(closeadj, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_sret21x_126d_jerk_v006_signal(closeadj):
    base = _f045_self_return(closeadj, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_sret63x_5d_jerk_v007_signal(closeadj):
    base = _f045_self_return(closeadj, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_sret63x_10d_jerk_v008_signal(closeadj):
    base = _f045_self_return(closeadj, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_sret63x_21d_jerk_v009_signal(closeadj):
    base = _f045_self_return(closeadj, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_sret63x_42d_jerk_v010_signal(closeadj):
    base = _f045_self_return(closeadj, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_sret63x_63d_jerk_v011_signal(closeadj):
    base = _f045_self_return(closeadj, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_sret63x_126d_jerk_v012_signal(closeadj):
    base = _f045_self_return(closeadj, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_sret126x_5d_jerk_v013_signal(closeadj):
    base = _f045_self_return(closeadj, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_sret126x_10d_jerk_v014_signal(closeadj):
    base = _f045_self_return(closeadj, 126) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_sret126x_21d_jerk_v015_signal(closeadj):
    base = _f045_self_return(closeadj, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_sret126x_42d_jerk_v016_signal(closeadj):
    base = _f045_self_return(closeadj, 126) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_sret126x_63d_jerk_v017_signal(closeadj):
    base = _f045_self_return(closeadj, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_sret126x_126d_jerk_v018_signal(closeadj):
    base = _f045_self_return(closeadj, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_sret252x_5d_jerk_v019_signal(closeadj):
    base = _f045_self_return(closeadj, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_sret252x_10d_jerk_v020_signal(closeadj):
    base = _f045_self_return(closeadj, 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_sret252x_21d_jerk_v021_signal(closeadj):
    base = _f045_self_return(closeadj, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_sret252x_42d_jerk_v022_signal(closeadj):
    base = _f045_self_return(closeadj, 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_sret252x_63d_jerk_v023_signal(closeadj):
    base = _f045_self_return(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_sret252x_126d_jerk_v024_signal(closeadj):
    base = _f045_self_return(closeadj, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smret21x_5d_jerk_v025_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smret21x_10d_jerk_v026_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smret21x_21d_jerk_v027_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smret21x_42d_jerk_v028_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smret21x_63d_jerk_v029_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smret21x_126d_jerk_v030_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smret63x_5d_jerk_v031_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smret63x_10d_jerk_v032_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smret63x_21d_jerk_v033_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smret63x_42d_jerk_v034_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smret63x_63d_jerk_v035_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smret63x_126d_jerk_v036_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smret126x_5d_jerk_v037_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smret126x_10d_jerk_v038_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 126) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smret126x_21d_jerk_v039_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smret126x_42d_jerk_v040_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 126) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smret126x_63d_jerk_v041_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smret126x_126d_jerk_v042_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smret252x_5d_jerk_v043_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smret252x_10d_jerk_v044_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smret252x_21d_jerk_v045_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smret252x_42d_jerk_v046_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smret252x_63d_jerk_v047_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smret252x_126d_jerk_v048_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs21_5d_jerk_v049_signal(closeadj):
    base = _f045_rs_score(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs21_10d_jerk_v050_signal(closeadj):
    base = _f045_rs_score(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs21_21d_jerk_v051_signal(closeadj):
    base = _f045_rs_score(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs21_42d_jerk_v052_signal(closeadj):
    base = _f045_rs_score(closeadj, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs21_63d_jerk_v053_signal(closeadj):
    base = _f045_rs_score(closeadj, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs21_126d_jerk_v054_signal(closeadj):
    base = _f045_rs_score(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs63_5d_jerk_v055_signal(closeadj):
    base = _f045_rs_score(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs63_10d_jerk_v056_signal(closeadj):
    base = _f045_rs_score(closeadj, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs63_21d_jerk_v057_signal(closeadj):
    base = _f045_rs_score(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs63_42d_jerk_v058_signal(closeadj):
    base = _f045_rs_score(closeadj, 63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs63_63d_jerk_v059_signal(closeadj):
    base = _f045_rs_score(closeadj, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs63_126d_jerk_v060_signal(closeadj):
    base = _f045_rs_score(closeadj, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs126_5d_jerk_v061_signal(closeadj):
    base = _f045_rs_score(closeadj, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs126_10d_jerk_v062_signal(closeadj):
    base = _f045_rs_score(closeadj, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs126_21d_jerk_v063_signal(closeadj):
    base = _f045_rs_score(closeadj, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs126_42d_jerk_v064_signal(closeadj):
    base = _f045_rs_score(closeadj, 126)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs126_63d_jerk_v065_signal(closeadj):
    base = _f045_rs_score(closeadj, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs126_126d_jerk_v066_signal(closeadj):
    base = _f045_rs_score(closeadj, 126)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs252_5d_jerk_v067_signal(closeadj):
    base = _f045_rs_score(closeadj, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs252_10d_jerk_v068_signal(closeadj):
    base = _f045_rs_score(closeadj, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs252_21d_jerk_v069_signal(closeadj):
    base = _f045_rs_score(closeadj, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs252_42d_jerk_v070_signal(closeadj):
    base = _f045_rs_score(closeadj, 252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs252_63d_jerk_v071_signal(closeadj):
    base = _f045_rs_score(closeadj, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs252_126d_jerk_v072_signal(closeadj):
    base = _f045_rs_score(closeadj, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_absret21x_5d_jerk_v073_signal(closeadj):
    base = _f045_self_return(closeadj, 21).abs() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_absret21x_10d_jerk_v074_signal(closeadj):
    base = _f045_self_return(closeadj, 21).abs() * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_absret21x_21d_jerk_v075_signal(closeadj):
    base = _f045_self_return(closeadj, 21).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_absret21x_42d_jerk_v076_signal(closeadj):
    base = _f045_self_return(closeadj, 21).abs() * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_absret21x_63d_jerk_v077_signal(closeadj):
    base = _f045_self_return(closeadj, 21).abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_absret21x_126d_jerk_v078_signal(closeadj):
    base = _f045_self_return(closeadj, 21).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_absret63x_5d_jerk_v079_signal(closeadj):
    base = _f045_self_return(closeadj, 63).abs() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_absret63x_10d_jerk_v080_signal(closeadj):
    base = _f045_self_return(closeadj, 63).abs() * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_absret63x_21d_jerk_v081_signal(closeadj):
    base = _f045_self_return(closeadj, 63).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_absret63x_42d_jerk_v082_signal(closeadj):
    base = _f045_self_return(closeadj, 63).abs() * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_absret63x_63d_jerk_v083_signal(closeadj):
    base = _f045_self_return(closeadj, 63).abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_absret63x_126d_jerk_v084_signal(closeadj):
    base = _f045_self_return(closeadj, 63).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_absret126x_5d_jerk_v085_signal(closeadj):
    base = _f045_self_return(closeadj, 126).abs() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_absret126x_10d_jerk_v086_signal(closeadj):
    base = _f045_self_return(closeadj, 126).abs() * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_absret126x_21d_jerk_v087_signal(closeadj):
    base = _f045_self_return(closeadj, 126).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_absret126x_42d_jerk_v088_signal(closeadj):
    base = _f045_self_return(closeadj, 126).abs() * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_absret126x_63d_jerk_v089_signal(closeadj):
    base = _f045_self_return(closeadj, 126).abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_absret126x_126d_jerk_v090_signal(closeadj):
    base = _f045_self_return(closeadj, 126).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_absret252x_5d_jerk_v091_signal(closeadj):
    base = _f045_self_return(closeadj, 252).abs() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_absret252x_10d_jerk_v092_signal(closeadj):
    base = _f045_self_return(closeadj, 252).abs() * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_absret252x_21d_jerk_v093_signal(closeadj):
    base = _f045_self_return(closeadj, 252).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_absret252x_42d_jerk_v094_signal(closeadj):
    base = _f045_self_return(closeadj, 252).abs() * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_absret252x_63d_jerk_v095_signal(closeadj):
    base = _f045_self_return(closeadj, 252).abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_absret252x_126d_jerk_v096_signal(closeadj):
    base = _f045_self_return(closeadj, 252).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_signret21x_5d_jerk_v097_signal(closeadj):
    base = np.sign(_f045_self_return(closeadj, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_signret21x_10d_jerk_v098_signal(closeadj):
    base = np.sign(_f045_self_return(closeadj, 21)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_signret21x_21d_jerk_v099_signal(closeadj):
    base = np.sign(_f045_self_return(closeadj, 21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_signret21x_42d_jerk_v100_signal(closeadj):
    base = np.sign(_f045_self_return(closeadj, 21)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_signret21x_63d_jerk_v101_signal(closeadj):
    base = np.sign(_f045_self_return(closeadj, 21)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_signret21x_126d_jerk_v102_signal(closeadj):
    base = np.sign(_f045_self_return(closeadj, 21)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_signret63x_5d_jerk_v103_signal(closeadj):
    base = np.sign(_f045_self_return(closeadj, 63)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_signret63x_10d_jerk_v104_signal(closeadj):
    base = np.sign(_f045_self_return(closeadj, 63)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_signret63x_21d_jerk_v105_signal(closeadj):
    base = np.sign(_f045_self_return(closeadj, 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_signret63x_42d_jerk_v106_signal(closeadj):
    base = np.sign(_f045_self_return(closeadj, 63)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_signret63x_63d_jerk_v107_signal(closeadj):
    base = np.sign(_f045_self_return(closeadj, 63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_signret63x_126d_jerk_v108_signal(closeadj):
    base = np.sign(_f045_self_return(closeadj, 63)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_signret252x_5d_jerk_v109_signal(closeadj):
    base = np.sign(_f045_self_return(closeadj, 252)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_signret252x_10d_jerk_v110_signal(closeadj):
    base = np.sign(_f045_self_return(closeadj, 252)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_signret252x_21d_jerk_v111_signal(closeadj):
    base = np.sign(_f045_self_return(closeadj, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_signret252x_42d_jerk_v112_signal(closeadj):
    base = np.sign(_f045_self_return(closeadj, 252)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_signret252x_63d_jerk_v113_signal(closeadj):
    base = np.sign(_f045_self_return(closeadj, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_signret252x_126d_jerk_v114_signal(closeadj):
    base = np.sign(_f045_self_return(closeadj, 252)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs21x_5d_jerk_v115_signal(closeadj):
    base = _f045_rs_score(closeadj, 21) * closeadj / 100.0
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs21x_10d_jerk_v116_signal(closeadj):
    base = _f045_rs_score(closeadj, 21) * closeadj / 100.0
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs21x_21d_jerk_v117_signal(closeadj):
    base = _f045_rs_score(closeadj, 21) * closeadj / 100.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs21x_42d_jerk_v118_signal(closeadj):
    base = _f045_rs_score(closeadj, 21) * closeadj / 100.0
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs21x_63d_jerk_v119_signal(closeadj):
    base = _f045_rs_score(closeadj, 21) * closeadj / 100.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs21x_126d_jerk_v120_signal(closeadj):
    base = _f045_rs_score(closeadj, 21) * closeadj / 100.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs63x_5d_jerk_v121_signal(closeadj):
    base = _f045_rs_score(closeadj, 63) * closeadj / 100.0
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs63x_10d_jerk_v122_signal(closeadj):
    base = _f045_rs_score(closeadj, 63) * closeadj / 100.0
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs63x_21d_jerk_v123_signal(closeadj):
    base = _f045_rs_score(closeadj, 63) * closeadj / 100.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs63x_42d_jerk_v124_signal(closeadj):
    base = _f045_rs_score(closeadj, 63) * closeadj / 100.0
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs63x_63d_jerk_v125_signal(closeadj):
    base = _f045_rs_score(closeadj, 63) * closeadj / 100.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs63x_126d_jerk_v126_signal(closeadj):
    base = _f045_rs_score(closeadj, 63) * closeadj / 100.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs126x_5d_jerk_v127_signal(closeadj):
    base = _f045_rs_score(closeadj, 126) * closeadj / 100.0
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs126x_10d_jerk_v128_signal(closeadj):
    base = _f045_rs_score(closeadj, 126) * closeadj / 100.0
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs126x_21d_jerk_v129_signal(closeadj):
    base = _f045_rs_score(closeadj, 126) * closeadj / 100.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs126x_42d_jerk_v130_signal(closeadj):
    base = _f045_rs_score(closeadj, 126) * closeadj / 100.0
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs126x_63d_jerk_v131_signal(closeadj):
    base = _f045_rs_score(closeadj, 126) * closeadj / 100.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs126x_126d_jerk_v132_signal(closeadj):
    base = _f045_rs_score(closeadj, 126) * closeadj / 100.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs252x_5d_jerk_v133_signal(closeadj):
    base = _f045_rs_score(closeadj, 252) * closeadj / 100.0
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs252x_10d_jerk_v134_signal(closeadj):
    base = _f045_rs_score(closeadj, 252) * closeadj / 100.0
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs252x_21d_jerk_v135_signal(closeadj):
    base = _f045_rs_score(closeadj, 252) * closeadj / 100.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs252x_42d_jerk_v136_signal(closeadj):
    base = _f045_rs_score(closeadj, 252) * closeadj / 100.0
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs252x_63d_jerk_v137_signal(closeadj):
    base = _f045_rs_score(closeadj, 252) * closeadj / 100.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_rs252x_126d_jerk_v138_signal(closeadj):
    base = _f045_rs_score(closeadj, 252) * closeadj / 100.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smretrnk21_5d_jerk_v139_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 21).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smretrnk21_10d_jerk_v140_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 21).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smretrnk21_21d_jerk_v141_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 21).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smretrnk21_42d_jerk_v142_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 21).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smretrnk21_63d_jerk_v143_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 21).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smretrnk21_126d_jerk_v144_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 21).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smretrnk63_5d_jerk_v145_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 63).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smretrnk63_10d_jerk_v146_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 63).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smretrnk63_21d_jerk_v147_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 63).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smretrnk63_42d_jerk_v148_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 63).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smretrnk63_63d_jerk_v149_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 63).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f045rsm_f045_relative_strength_market_smretrnk63_126d_jerk_v150_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 63).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f045rsm_f045_relative_strength_market_sret21x_5d_jerk_v001_signal,
    f045rsm_f045_relative_strength_market_sret21x_10d_jerk_v002_signal,
    f045rsm_f045_relative_strength_market_sret21x_21d_jerk_v003_signal,
    f045rsm_f045_relative_strength_market_sret21x_42d_jerk_v004_signal,
    f045rsm_f045_relative_strength_market_sret21x_63d_jerk_v005_signal,
    f045rsm_f045_relative_strength_market_sret21x_126d_jerk_v006_signal,
    f045rsm_f045_relative_strength_market_sret63x_5d_jerk_v007_signal,
    f045rsm_f045_relative_strength_market_sret63x_10d_jerk_v008_signal,
    f045rsm_f045_relative_strength_market_sret63x_21d_jerk_v009_signal,
    f045rsm_f045_relative_strength_market_sret63x_42d_jerk_v010_signal,
    f045rsm_f045_relative_strength_market_sret63x_63d_jerk_v011_signal,
    f045rsm_f045_relative_strength_market_sret63x_126d_jerk_v012_signal,
    f045rsm_f045_relative_strength_market_sret126x_5d_jerk_v013_signal,
    f045rsm_f045_relative_strength_market_sret126x_10d_jerk_v014_signal,
    f045rsm_f045_relative_strength_market_sret126x_21d_jerk_v015_signal,
    f045rsm_f045_relative_strength_market_sret126x_42d_jerk_v016_signal,
    f045rsm_f045_relative_strength_market_sret126x_63d_jerk_v017_signal,
    f045rsm_f045_relative_strength_market_sret126x_126d_jerk_v018_signal,
    f045rsm_f045_relative_strength_market_sret252x_5d_jerk_v019_signal,
    f045rsm_f045_relative_strength_market_sret252x_10d_jerk_v020_signal,
    f045rsm_f045_relative_strength_market_sret252x_21d_jerk_v021_signal,
    f045rsm_f045_relative_strength_market_sret252x_42d_jerk_v022_signal,
    f045rsm_f045_relative_strength_market_sret252x_63d_jerk_v023_signal,
    f045rsm_f045_relative_strength_market_sret252x_126d_jerk_v024_signal,
    f045rsm_f045_relative_strength_market_smret21x_5d_jerk_v025_signal,
    f045rsm_f045_relative_strength_market_smret21x_10d_jerk_v026_signal,
    f045rsm_f045_relative_strength_market_smret21x_21d_jerk_v027_signal,
    f045rsm_f045_relative_strength_market_smret21x_42d_jerk_v028_signal,
    f045rsm_f045_relative_strength_market_smret21x_63d_jerk_v029_signal,
    f045rsm_f045_relative_strength_market_smret21x_126d_jerk_v030_signal,
    f045rsm_f045_relative_strength_market_smret63x_5d_jerk_v031_signal,
    f045rsm_f045_relative_strength_market_smret63x_10d_jerk_v032_signal,
    f045rsm_f045_relative_strength_market_smret63x_21d_jerk_v033_signal,
    f045rsm_f045_relative_strength_market_smret63x_42d_jerk_v034_signal,
    f045rsm_f045_relative_strength_market_smret63x_63d_jerk_v035_signal,
    f045rsm_f045_relative_strength_market_smret63x_126d_jerk_v036_signal,
    f045rsm_f045_relative_strength_market_smret126x_5d_jerk_v037_signal,
    f045rsm_f045_relative_strength_market_smret126x_10d_jerk_v038_signal,
    f045rsm_f045_relative_strength_market_smret126x_21d_jerk_v039_signal,
    f045rsm_f045_relative_strength_market_smret126x_42d_jerk_v040_signal,
    f045rsm_f045_relative_strength_market_smret126x_63d_jerk_v041_signal,
    f045rsm_f045_relative_strength_market_smret126x_126d_jerk_v042_signal,
    f045rsm_f045_relative_strength_market_smret252x_5d_jerk_v043_signal,
    f045rsm_f045_relative_strength_market_smret252x_10d_jerk_v044_signal,
    f045rsm_f045_relative_strength_market_smret252x_21d_jerk_v045_signal,
    f045rsm_f045_relative_strength_market_smret252x_42d_jerk_v046_signal,
    f045rsm_f045_relative_strength_market_smret252x_63d_jerk_v047_signal,
    f045rsm_f045_relative_strength_market_smret252x_126d_jerk_v048_signal,
    f045rsm_f045_relative_strength_market_rs21_5d_jerk_v049_signal,
    f045rsm_f045_relative_strength_market_rs21_10d_jerk_v050_signal,
    f045rsm_f045_relative_strength_market_rs21_21d_jerk_v051_signal,
    f045rsm_f045_relative_strength_market_rs21_42d_jerk_v052_signal,
    f045rsm_f045_relative_strength_market_rs21_63d_jerk_v053_signal,
    f045rsm_f045_relative_strength_market_rs21_126d_jerk_v054_signal,
    f045rsm_f045_relative_strength_market_rs63_5d_jerk_v055_signal,
    f045rsm_f045_relative_strength_market_rs63_10d_jerk_v056_signal,
    f045rsm_f045_relative_strength_market_rs63_21d_jerk_v057_signal,
    f045rsm_f045_relative_strength_market_rs63_42d_jerk_v058_signal,
    f045rsm_f045_relative_strength_market_rs63_63d_jerk_v059_signal,
    f045rsm_f045_relative_strength_market_rs63_126d_jerk_v060_signal,
    f045rsm_f045_relative_strength_market_rs126_5d_jerk_v061_signal,
    f045rsm_f045_relative_strength_market_rs126_10d_jerk_v062_signal,
    f045rsm_f045_relative_strength_market_rs126_21d_jerk_v063_signal,
    f045rsm_f045_relative_strength_market_rs126_42d_jerk_v064_signal,
    f045rsm_f045_relative_strength_market_rs126_63d_jerk_v065_signal,
    f045rsm_f045_relative_strength_market_rs126_126d_jerk_v066_signal,
    f045rsm_f045_relative_strength_market_rs252_5d_jerk_v067_signal,
    f045rsm_f045_relative_strength_market_rs252_10d_jerk_v068_signal,
    f045rsm_f045_relative_strength_market_rs252_21d_jerk_v069_signal,
    f045rsm_f045_relative_strength_market_rs252_42d_jerk_v070_signal,
    f045rsm_f045_relative_strength_market_rs252_63d_jerk_v071_signal,
    f045rsm_f045_relative_strength_market_rs252_126d_jerk_v072_signal,
    f045rsm_f045_relative_strength_market_absret21x_5d_jerk_v073_signal,
    f045rsm_f045_relative_strength_market_absret21x_10d_jerk_v074_signal,
    f045rsm_f045_relative_strength_market_absret21x_21d_jerk_v075_signal,
    f045rsm_f045_relative_strength_market_absret21x_42d_jerk_v076_signal,
    f045rsm_f045_relative_strength_market_absret21x_63d_jerk_v077_signal,
    f045rsm_f045_relative_strength_market_absret21x_126d_jerk_v078_signal,
    f045rsm_f045_relative_strength_market_absret63x_5d_jerk_v079_signal,
    f045rsm_f045_relative_strength_market_absret63x_10d_jerk_v080_signal,
    f045rsm_f045_relative_strength_market_absret63x_21d_jerk_v081_signal,
    f045rsm_f045_relative_strength_market_absret63x_42d_jerk_v082_signal,
    f045rsm_f045_relative_strength_market_absret63x_63d_jerk_v083_signal,
    f045rsm_f045_relative_strength_market_absret63x_126d_jerk_v084_signal,
    f045rsm_f045_relative_strength_market_absret126x_5d_jerk_v085_signal,
    f045rsm_f045_relative_strength_market_absret126x_10d_jerk_v086_signal,
    f045rsm_f045_relative_strength_market_absret126x_21d_jerk_v087_signal,
    f045rsm_f045_relative_strength_market_absret126x_42d_jerk_v088_signal,
    f045rsm_f045_relative_strength_market_absret126x_63d_jerk_v089_signal,
    f045rsm_f045_relative_strength_market_absret126x_126d_jerk_v090_signal,
    f045rsm_f045_relative_strength_market_absret252x_5d_jerk_v091_signal,
    f045rsm_f045_relative_strength_market_absret252x_10d_jerk_v092_signal,
    f045rsm_f045_relative_strength_market_absret252x_21d_jerk_v093_signal,
    f045rsm_f045_relative_strength_market_absret252x_42d_jerk_v094_signal,
    f045rsm_f045_relative_strength_market_absret252x_63d_jerk_v095_signal,
    f045rsm_f045_relative_strength_market_absret252x_126d_jerk_v096_signal,
    f045rsm_f045_relative_strength_market_signret21x_5d_jerk_v097_signal,
    f045rsm_f045_relative_strength_market_signret21x_10d_jerk_v098_signal,
    f045rsm_f045_relative_strength_market_signret21x_21d_jerk_v099_signal,
    f045rsm_f045_relative_strength_market_signret21x_42d_jerk_v100_signal,
    f045rsm_f045_relative_strength_market_signret21x_63d_jerk_v101_signal,
    f045rsm_f045_relative_strength_market_signret21x_126d_jerk_v102_signal,
    f045rsm_f045_relative_strength_market_signret63x_5d_jerk_v103_signal,
    f045rsm_f045_relative_strength_market_signret63x_10d_jerk_v104_signal,
    f045rsm_f045_relative_strength_market_signret63x_21d_jerk_v105_signal,
    f045rsm_f045_relative_strength_market_signret63x_42d_jerk_v106_signal,
    f045rsm_f045_relative_strength_market_signret63x_63d_jerk_v107_signal,
    f045rsm_f045_relative_strength_market_signret63x_126d_jerk_v108_signal,
    f045rsm_f045_relative_strength_market_signret252x_5d_jerk_v109_signal,
    f045rsm_f045_relative_strength_market_signret252x_10d_jerk_v110_signal,
    f045rsm_f045_relative_strength_market_signret252x_21d_jerk_v111_signal,
    f045rsm_f045_relative_strength_market_signret252x_42d_jerk_v112_signal,
    f045rsm_f045_relative_strength_market_signret252x_63d_jerk_v113_signal,
    f045rsm_f045_relative_strength_market_signret252x_126d_jerk_v114_signal,
    f045rsm_f045_relative_strength_market_rs21x_5d_jerk_v115_signal,
    f045rsm_f045_relative_strength_market_rs21x_10d_jerk_v116_signal,
    f045rsm_f045_relative_strength_market_rs21x_21d_jerk_v117_signal,
    f045rsm_f045_relative_strength_market_rs21x_42d_jerk_v118_signal,
    f045rsm_f045_relative_strength_market_rs21x_63d_jerk_v119_signal,
    f045rsm_f045_relative_strength_market_rs21x_126d_jerk_v120_signal,
    f045rsm_f045_relative_strength_market_rs63x_5d_jerk_v121_signal,
    f045rsm_f045_relative_strength_market_rs63x_10d_jerk_v122_signal,
    f045rsm_f045_relative_strength_market_rs63x_21d_jerk_v123_signal,
    f045rsm_f045_relative_strength_market_rs63x_42d_jerk_v124_signal,
    f045rsm_f045_relative_strength_market_rs63x_63d_jerk_v125_signal,
    f045rsm_f045_relative_strength_market_rs63x_126d_jerk_v126_signal,
    f045rsm_f045_relative_strength_market_rs126x_5d_jerk_v127_signal,
    f045rsm_f045_relative_strength_market_rs126x_10d_jerk_v128_signal,
    f045rsm_f045_relative_strength_market_rs126x_21d_jerk_v129_signal,
    f045rsm_f045_relative_strength_market_rs126x_42d_jerk_v130_signal,
    f045rsm_f045_relative_strength_market_rs126x_63d_jerk_v131_signal,
    f045rsm_f045_relative_strength_market_rs126x_126d_jerk_v132_signal,
    f045rsm_f045_relative_strength_market_rs252x_5d_jerk_v133_signal,
    f045rsm_f045_relative_strength_market_rs252x_10d_jerk_v134_signal,
    f045rsm_f045_relative_strength_market_rs252x_21d_jerk_v135_signal,
    f045rsm_f045_relative_strength_market_rs252x_42d_jerk_v136_signal,
    f045rsm_f045_relative_strength_market_rs252x_63d_jerk_v137_signal,
    f045rsm_f045_relative_strength_market_rs252x_126d_jerk_v138_signal,
    f045rsm_f045_relative_strength_market_smretrnk21_5d_jerk_v139_signal,
    f045rsm_f045_relative_strength_market_smretrnk21_10d_jerk_v140_signal,
    f045rsm_f045_relative_strength_market_smretrnk21_21d_jerk_v141_signal,
    f045rsm_f045_relative_strength_market_smretrnk21_42d_jerk_v142_signal,
    f045rsm_f045_relative_strength_market_smretrnk21_63d_jerk_v143_signal,
    f045rsm_f045_relative_strength_market_smretrnk21_126d_jerk_v144_signal,
    f045rsm_f045_relative_strength_market_smretrnk63_5d_jerk_v145_signal,
    f045rsm_f045_relative_strength_market_smretrnk63_10d_jerk_v146_signal,
    f045rsm_f045_relative_strength_market_smretrnk63_21d_jerk_v147_signal,
    f045rsm_f045_relative_strength_market_smretrnk63_42d_jerk_v148_signal,
    f045rsm_f045_relative_strength_market_smretrnk63_63d_jerk_v149_signal,
    f045rsm_f045_relative_strength_market_smretrnk63_126d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F045_RELATIVE_STRENGTH_MARKET_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")

    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f045_self_return", "_f045_smoothed_return", "_f045_rs_score")
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
