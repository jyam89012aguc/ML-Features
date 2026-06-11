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

def _f018_round_distance(closeadj, w):
    # nearest round number at order-of-magnitude scale
    mag = 10.0 ** (np.floor(np.log10(closeadj.abs().replace(0, np.nan))) - 1.0)
    nearest = (closeadj / mag).round() * mag
    return (closeadj - nearest) / closeadj.replace(0, np.nan).abs()


def _f018_round_proximity(closeadj, w):
    dist = _f018_round_distance(closeadj, w).abs()
    sm = dist.rolling(w, min_periods=max(1, w // 2)).mean()
    return 1.0 / (1.0 + sm)


def _f018_magnet_score(closeadj, w):
    prox = _f018_round_proximity(closeadj, w)
    vol = closeadj.rolling(w, min_periods=max(1, w // 2)).std()
    return prox * vol



# ===== features =====
def f018drn_f018_distance_to_round_number_p2_z63_close_jk63_42d_jerk_v001_signal(closeadj):
    base = _f018_round_proximity(closeadj, 42)
    inter = (_z(base, 63)) * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_z63_closesq_jk42_42d_jerk_v002_signal(closeadj):
    base = _f018_round_proximity(closeadj, 42)
    inter = (_z(base, 63)) * closeadj * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_std126_closesma63_jk63_63d_jerk_v003_signal(closeadj):
    base = _f018_round_proximity(closeadj, 63)
    inter = (_std(base, 126)) * _mean(closeadj, 63)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_diff5_closesma63_jk42_378d_jerk_v004_signal(closeadj):
    base = _f018_round_distance(closeadj, 378)
    inter = ((base).diff(5)) * _mean(closeadj, 63)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_z252_closesq_jk63_189d_jerk_v005_signal(closeadj):
    base = _f018_magnet_score(closeadj, 189)
    inter = (_z(base, 252)) * closeadj * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_diff21_close_jk42_252d_jerk_v006_signal(closeadj):
    base = _f018_round_proximity(closeadj, 252)
    inter = ((base).diff(21)) * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_diff63_closesq_jk21_5d_jerk_v007_signal(closeadj):
    base = _f018_round_proximity(closeadj, 5)
    inter = ((base).diff(63)) * closeadj * closeadj
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_diff63_closesma21_jk5_252d_jerk_v008_signal(closeadj):
    base = _f018_round_proximity(closeadj, 252)
    inter = ((base).diff(63)) * _mean(closeadj, 21)
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_sma21_close_jk126_5d_jerk_v009_signal(closeadj):
    base = _f018_magnet_score(closeadj, 5)
    inter = (_mean(base, 21)) * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_z63_closesma63_jk21_63d_jerk_v010_signal(closeadj):
    base = _f018_round_distance(closeadj, 63)
    inter = (_z(base, 63)) * _mean(closeadj, 63)
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_std126_close_jk5_504d_jerk_v011_signal(closeadj):
    base = _f018_round_distance(closeadj, 504)
    inter = (_std(base, 126)) * closeadj
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_raw_closesma63_jk21_126d_jerk_v012_signal(closeadj):
    base = _f018_round_proximity(closeadj, 126)
    inter = (base) * _mean(closeadj, 63)
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_sma21_closesq_jk42_504d_jerk_v013_signal(closeadj):
    base = _f018_round_distance(closeadj, 504)
    inter = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_z21_close_jk63_63d_jerk_v014_signal(closeadj):
    base = _f018_magnet_score(closeadj, 63)
    inter = (_z(base, 21)) * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_std21_closesma63_jk126_10d_jerk_v015_signal(closeadj):
    base = _f018_round_distance(closeadj, 10)
    inter = (_std(base, 21)) * _mean(closeadj, 63)
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_diff63_close_jk21_42d_jerk_v016_signal(closeadj):
    base = _f018_magnet_score(closeadj, 42)
    inter = ((base).diff(63)) * closeadj
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_diff63_close_jk21_10d_jerk_v017_signal(closeadj):
    base = _f018_magnet_score(closeadj, 10)
    inter = ((base).diff(63)) * closeadj
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_raw_closesq_jk5_504d_jerk_v018_signal(closeadj):
    base = _f018_magnet_score(closeadj, 504)
    inter = (base) * closeadj * closeadj
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_sma126_closesma21_jk63_42d_jerk_v019_signal(closeadj):
    base = _f018_magnet_score(closeadj, 42)
    inter = (_mean(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_z126_closesma21_jk42_189d_jerk_v020_signal(closeadj):
    base = _f018_magnet_score(closeadj, 189)
    inter = (_z(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_z21_closesma63_jk63_5d_jerk_v021_signal(closeadj):
    base = _f018_round_distance(closeadj, 5)
    inter = (_z(base, 21)) * _mean(closeadj, 63)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_std63_close_jk63_5d_jerk_v022_signal(closeadj):
    base = _f018_magnet_score(closeadj, 5)
    inter = (_std(base, 63)) * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_std126_closesma21_jk42_10d_jerk_v023_signal(closeadj):
    base = _f018_magnet_score(closeadj, 10)
    inter = (_std(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_sma126_closesma21_jk10_42d_jerk_v024_signal(closeadj):
    base = _f018_round_proximity(closeadj, 42)
    inter = (_mean(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_sma126_closesma21_jk21_378d_jerk_v025_signal(closeadj):
    base = _f018_magnet_score(closeadj, 378)
    inter = (_mean(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_diff63_closesma63_jk126_126d_jerk_v026_signal(closeadj):
    base = _f018_round_distance(closeadj, 126)
    inter = ((base).diff(63)) * _mean(closeadj, 63)
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_std126_closesma21_jk5_10d_jerk_v027_signal(closeadj):
    base = _f018_magnet_score(closeadj, 10)
    inter = (_std(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_diff5_closesma21_jk42_21d_jerk_v028_signal(closeadj):
    base = _f018_round_proximity(closeadj, 21)
    inter = ((base).diff(5)) * _mean(closeadj, 21)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_std21_close_jk21_126d_jerk_v029_signal(closeadj):
    base = _f018_round_distance(closeadj, 126)
    inter = (_std(base, 21)) * closeadj
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_sma126_closesma21_jk63_21d_jerk_v030_signal(closeadj):
    base = _f018_round_distance(closeadj, 21)
    inter = (_mean(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_z126_close_jk42_42d_jerk_v031_signal(closeadj):
    base = _f018_round_proximity(closeadj, 42)
    inter = (_z(base, 126)) * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_z63_closesq_jk42_10d_jerk_v032_signal(closeadj):
    base = _f018_magnet_score(closeadj, 10)
    inter = (_z(base, 63)) * closeadj * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_diff5_closesq_jk21_378d_jerk_v033_signal(closeadj):
    base = _f018_round_distance(closeadj, 378)
    inter = ((base).diff(5)) * closeadj * closeadj
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_std126_closesma63_jk10_63d_jerk_v034_signal(closeadj):
    base = _f018_round_proximity(closeadj, 63)
    inter = (_std(base, 126)) * _mean(closeadj, 63)
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_sma126_closesma63_jk42_252d_jerk_v035_signal(closeadj):
    base = _f018_magnet_score(closeadj, 252)
    inter = (_mean(base, 126)) * _mean(closeadj, 63)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_raw_closesma21_jk42_189d_jerk_v036_signal(closeadj):
    base = _f018_round_distance(closeadj, 189)
    inter = (base) * _mean(closeadj, 21)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_z63_closesma21_jk21_63d_jerk_v037_signal(closeadj):
    base = _f018_magnet_score(closeadj, 63)
    inter = (_z(base, 63)) * _mean(closeadj, 21)
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_diff63_closesq_jk63_63d_jerk_v038_signal(closeadj):
    base = _f018_round_proximity(closeadj, 63)
    inter = ((base).diff(63)) * closeadj * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_sma63_closesma21_jk5_5d_jerk_v039_signal(closeadj):
    base = _f018_round_proximity(closeadj, 5)
    inter = (_mean(base, 63)) * _mean(closeadj, 21)
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_sma126_closesq_jk5_42d_jerk_v040_signal(closeadj):
    base = _f018_round_distance(closeadj, 42)
    inter = (_mean(base, 126)) * closeadj * closeadj
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_sma63_closesma63_jk42_504d_jerk_v041_signal(closeadj):
    base = _f018_round_proximity(closeadj, 504)
    inter = (_mean(base, 63)) * _mean(closeadj, 63)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_sma21_closesma21_jk63_5d_jerk_v042_signal(closeadj):
    base = _f018_round_proximity(closeadj, 5)
    inter = (_mean(base, 21)) * _mean(closeadj, 21)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_diff63_close_jk126_189d_jerk_v043_signal(closeadj):
    base = _f018_magnet_score(closeadj, 189)
    inter = ((base).diff(63)) * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_z126_closesma63_jk5_189d_jerk_v044_signal(closeadj):
    base = _f018_round_proximity(closeadj, 189)
    inter = (_z(base, 126)) * _mean(closeadj, 63)
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_std63_closesma21_jk10_63d_jerk_v045_signal(closeadj):
    base = _f018_round_proximity(closeadj, 63)
    inter = (_std(base, 63)) * _mean(closeadj, 21)
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_sma63_closesq_jk5_126d_jerk_v046_signal(closeadj):
    base = _f018_magnet_score(closeadj, 126)
    inter = (_mean(base, 63)) * closeadj * closeadj
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_diff21_close_jk5_378d_jerk_v047_signal(closeadj):
    base = _f018_round_distance(closeadj, 378)
    inter = ((base).diff(21)) * closeadj
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_std63_closesma21_jk63_10d_jerk_v048_signal(closeadj):
    base = _f018_round_distance(closeadj, 10)
    inter = (_std(base, 63)) * _mean(closeadj, 21)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_raw_closesq_jk10_42d_jerk_v049_signal(closeadj):
    base = _f018_round_distance(closeadj, 42)
    inter = (base) * closeadj * closeadj
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_diff21_close_jk10_10d_jerk_v050_signal(closeadj):
    base = _f018_magnet_score(closeadj, 10)
    inter = ((base).diff(21)) * closeadj
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_std21_closesma63_jk126_5d_jerk_v051_signal(closeadj):
    base = _f018_round_proximity(closeadj, 5)
    inter = (_std(base, 21)) * _mean(closeadj, 63)
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_std63_closesma63_jk63_63d_jerk_v052_signal(closeadj):
    base = _f018_round_distance(closeadj, 63)
    inter = (_std(base, 63)) * _mean(closeadj, 63)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_std63_closesma63_jk126_189d_jerk_v053_signal(closeadj):
    base = _f018_magnet_score(closeadj, 189)
    inter = (_std(base, 63)) * _mean(closeadj, 63)
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_diff5_closesma63_jk21_5d_jerk_v054_signal(closeadj):
    base = _f018_magnet_score(closeadj, 5)
    inter = ((base).diff(5)) * _mean(closeadj, 63)
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_std63_closesma63_jk10_126d_jerk_v055_signal(closeadj):
    base = _f018_magnet_score(closeadj, 126)
    inter = (_std(base, 63)) * _mean(closeadj, 63)
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_std63_closesma63_jk63_10d_jerk_v056_signal(closeadj):
    base = _f018_magnet_score(closeadj, 10)
    inter = (_std(base, 63)) * _mean(closeadj, 63)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_std21_close_jk10_189d_jerk_v057_signal(closeadj):
    base = _f018_round_distance(closeadj, 189)
    inter = (_std(base, 21)) * closeadj
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_z126_closesma21_jk10_252d_jerk_v058_signal(closeadj):
    base = _f018_magnet_score(closeadj, 252)
    inter = (_z(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_sma21_closesq_jk126_252d_jerk_v059_signal(closeadj):
    base = _f018_round_distance(closeadj, 252)
    inter = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_z126_closesma21_jk63_126d_jerk_v060_signal(closeadj):
    base = _f018_round_distance(closeadj, 126)
    inter = (_z(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_diff5_close_jk126_63d_jerk_v061_signal(closeadj):
    base = _f018_round_distance(closeadj, 63)
    inter = ((base).diff(5)) * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_diff21_closesma63_jk126_126d_jerk_v062_signal(closeadj):
    base = _f018_round_distance(closeadj, 126)
    inter = ((base).diff(21)) * _mean(closeadj, 63)
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_std21_close_jk63_42d_jerk_v063_signal(closeadj):
    base = _f018_round_proximity(closeadj, 42)
    inter = (_std(base, 21)) * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_sma63_closesma63_jk21_10d_jerk_v064_signal(closeadj):
    base = _f018_round_proximity(closeadj, 10)
    inter = (_mean(base, 63)) * _mean(closeadj, 63)
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_z21_closesq_jk63_63d_jerk_v065_signal(closeadj):
    base = _f018_round_distance(closeadj, 63)
    inter = (_z(base, 21)) * closeadj * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_z21_close_jk63_252d_jerk_v066_signal(closeadj):
    base = _f018_round_distance(closeadj, 252)
    inter = (_z(base, 21)) * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_diff5_closesma21_jk42_5d_jerk_v067_signal(closeadj):
    base = _f018_round_distance(closeadj, 5)
    inter = ((base).diff(5)) * _mean(closeadj, 21)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_diff21_closesma21_jk126_126d_jerk_v068_signal(closeadj):
    base = _f018_round_proximity(closeadj, 126)
    inter = ((base).diff(21)) * _mean(closeadj, 21)
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_sma63_close_jk21_252d_jerk_v069_signal(closeadj):
    base = _f018_round_proximity(closeadj, 252)
    inter = (_mean(base, 63)) * closeadj
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_diff21_closesma21_jk42_378d_jerk_v070_signal(closeadj):
    base = _f018_magnet_score(closeadj, 378)
    inter = ((base).diff(21)) * _mean(closeadj, 21)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_z21_closesma63_jk10_63d_jerk_v071_signal(closeadj):
    base = _f018_magnet_score(closeadj, 63)
    inter = (_z(base, 21)) * _mean(closeadj, 63)
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_diff5_closesq_jk10_378d_jerk_v072_signal(closeadj):
    base = _f018_magnet_score(closeadj, 378)
    inter = ((base).diff(5)) * closeadj * closeadj
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_z21_close_jk42_378d_jerk_v073_signal(closeadj):
    base = _f018_round_proximity(closeadj, 378)
    inter = (_z(base, 21)) * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_z63_closesq_jk126_5d_jerk_v074_signal(closeadj):
    base = _f018_magnet_score(closeadj, 5)
    inter = (_z(base, 63)) * closeadj * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_z252_close_jk10_42d_jerk_v075_signal(closeadj):
    base = _f018_magnet_score(closeadj, 42)
    inter = (_z(base, 252)) * closeadj
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_z252_closesma21_jk63_189d_jerk_v076_signal(closeadj):
    base = _f018_round_distance(closeadj, 189)
    inter = (_z(base, 252)) * _mean(closeadj, 21)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_z126_closesq_jk63_126d_jerk_v077_signal(closeadj):
    base = _f018_magnet_score(closeadj, 126)
    inter = (_z(base, 126)) * closeadj * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_std21_closesma63_jk126_21d_jerk_v078_signal(closeadj):
    base = _f018_round_distance(closeadj, 21)
    inter = (_std(base, 21)) * _mean(closeadj, 63)
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_raw_close_jk5_21d_jerk_v079_signal(closeadj):
    base = _f018_round_distance(closeadj, 21)
    inter = (base) * closeadj
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_std126_closesma21_jk63_21d_jerk_v080_signal(closeadj):
    base = _f018_magnet_score(closeadj, 21)
    inter = (_std(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_raw_close_jk10_42d_jerk_v081_signal(closeadj):
    base = _f018_round_proximity(closeadj, 42)
    inter = (base) * closeadj
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_std63_closesq_jk126_504d_jerk_v082_signal(closeadj):
    base = _f018_round_distance(closeadj, 504)
    inter = (_std(base, 63)) * closeadj * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_std21_closesma21_jk10_378d_jerk_v083_signal(closeadj):
    base = _f018_magnet_score(closeadj, 378)
    inter = (_std(base, 21)) * _mean(closeadj, 21)
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_sma63_close_jk42_252d_jerk_v084_signal(closeadj):
    base = _f018_round_proximity(closeadj, 252)
    inter = (_mean(base, 63)) * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_diff21_closesma21_jk42_126d_jerk_v085_signal(closeadj):
    base = _f018_magnet_score(closeadj, 126)
    inter = ((base).diff(21)) * _mean(closeadj, 21)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_sma126_close_jk42_42d_jerk_v086_signal(closeadj):
    base = _f018_round_proximity(closeadj, 42)
    inter = (_mean(base, 126)) * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_sma126_closesq_jk63_10d_jerk_v087_signal(closeadj):
    base = _f018_round_distance(closeadj, 10)
    inter = (_mean(base, 126)) * closeadj * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_z21_closesma63_jk63_63d_jerk_v088_signal(closeadj):
    base = _f018_round_distance(closeadj, 63)
    inter = (_z(base, 21)) * _mean(closeadj, 63)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_diff21_closesma63_jk21_42d_jerk_v089_signal(closeadj):
    base = _f018_round_proximity(closeadj, 42)
    inter = ((base).diff(21)) * _mean(closeadj, 63)
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_sma21_closesq_jk21_504d_jerk_v090_signal(closeadj):
    base = _f018_round_distance(closeadj, 504)
    inter = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_sma63_closesma21_jk42_252d_jerk_v091_signal(closeadj):
    base = _f018_round_proximity(closeadj, 252)
    inter = (_mean(base, 63)) * _mean(closeadj, 21)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_z21_close_jk10_126d_jerk_v092_signal(closeadj):
    base = _f018_round_distance(closeadj, 126)
    inter = (_z(base, 21)) * closeadj
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_z21_closesma21_jk42_504d_jerk_v093_signal(closeadj):
    base = _f018_magnet_score(closeadj, 504)
    inter = (_z(base, 21)) * _mean(closeadj, 21)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_sma126_closesma21_jk5_42d_jerk_v094_signal(closeadj):
    base = _f018_round_proximity(closeadj, 42)
    inter = (_mean(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_z21_closesma21_jk42_126d_jerk_v095_signal(closeadj):
    base = _f018_round_proximity(closeadj, 126)
    inter = (_z(base, 21)) * _mean(closeadj, 21)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_sma21_close_jk42_10d_jerk_v096_signal(closeadj):
    base = _f018_round_distance(closeadj, 10)
    inter = (_mean(base, 21)) * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_diff63_closesq_jk63_42d_jerk_v097_signal(closeadj):
    base = _f018_round_proximity(closeadj, 42)
    inter = ((base).diff(63)) * closeadj * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_z126_close_jk63_126d_jerk_v098_signal(closeadj):
    base = _f018_magnet_score(closeadj, 126)
    inter = (_z(base, 126)) * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_diff21_closesq_jk21_21d_jerk_v099_signal(closeadj):
    base = _f018_round_distance(closeadj, 21)
    inter = ((base).diff(21)) * closeadj * closeadj
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_raw_closesma21_jk126_5d_jerk_v100_signal(closeadj):
    base = _f018_magnet_score(closeadj, 5)
    inter = (base) * _mean(closeadj, 21)
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_diff63_closesma63_jk63_189d_jerk_v101_signal(closeadj):
    base = _f018_round_distance(closeadj, 189)
    inter = ((base).diff(63)) * _mean(closeadj, 63)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_diff5_closesma21_jk21_10d_jerk_v102_signal(closeadj):
    base = _f018_magnet_score(closeadj, 10)
    inter = ((base).diff(5)) * _mean(closeadj, 21)
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_sma126_closesma21_jk126_189d_jerk_v103_signal(closeadj):
    base = _f018_round_distance(closeadj, 189)
    inter = (_mean(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_diff5_closesma63_jk42_189d_jerk_v104_signal(closeadj):
    base = _f018_round_proximity(closeadj, 189)
    inter = ((base).diff(5)) * _mean(closeadj, 63)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_z21_closesma21_jk42_5d_jerk_v105_signal(closeadj):
    base = _f018_magnet_score(closeadj, 5)
    inter = (_z(base, 21)) * _mean(closeadj, 21)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_std21_close_jk126_10d_jerk_v106_signal(closeadj):
    base = _f018_round_proximity(closeadj, 10)
    inter = (_std(base, 21)) * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_sma126_close_jk126_378d_jerk_v107_signal(closeadj):
    base = _f018_round_proximity(closeadj, 378)
    inter = (_mean(base, 126)) * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_sma126_closesma21_jk10_63d_jerk_v108_signal(closeadj):
    base = _f018_round_distance(closeadj, 63)
    inter = (_mean(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_diff5_closesma63_jk63_126d_jerk_v109_signal(closeadj):
    base = _f018_magnet_score(closeadj, 126)
    inter = ((base).diff(5)) * _mean(closeadj, 63)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_z252_close_jk42_252d_jerk_v110_signal(closeadj):
    base = _f018_magnet_score(closeadj, 252)
    inter = (_z(base, 252)) * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_raw_closesma21_jk126_126d_jerk_v111_signal(closeadj):
    base = _f018_round_proximity(closeadj, 126)
    inter = (base) * _mean(closeadj, 21)
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_z252_closesma63_jk21_42d_jerk_v112_signal(closeadj):
    base = _f018_round_proximity(closeadj, 42)
    inter = (_z(base, 252)) * _mean(closeadj, 63)
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_z252_closesma63_jk5_63d_jerk_v113_signal(closeadj):
    base = _f018_round_proximity(closeadj, 63)
    inter = (_z(base, 252)) * _mean(closeadj, 63)
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_std63_closesq_jk63_504d_jerk_v114_signal(closeadj):
    base = _f018_magnet_score(closeadj, 504)
    inter = (_std(base, 63)) * closeadj * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_z252_closesq_jk42_5d_jerk_v115_signal(closeadj):
    base = _f018_magnet_score(closeadj, 5)
    inter = (_z(base, 252)) * closeadj * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_z126_close_jk42_126d_jerk_v116_signal(closeadj):
    base = _f018_magnet_score(closeadj, 126)
    inter = (_z(base, 126)) * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_diff21_closesma21_jk21_378d_jerk_v117_signal(closeadj):
    base = _f018_round_proximity(closeadj, 378)
    inter = ((base).diff(21)) * _mean(closeadj, 21)
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_diff5_closesma63_jk42_42d_jerk_v118_signal(closeadj):
    base = _f018_magnet_score(closeadj, 42)
    inter = ((base).diff(5)) * _mean(closeadj, 63)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_z21_closesq_jk10_189d_jerk_v119_signal(closeadj):
    base = _f018_round_proximity(closeadj, 189)
    inter = (_z(base, 21)) * closeadj * closeadj
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_std126_closesma63_jk63_10d_jerk_v120_signal(closeadj):
    base = _f018_round_distance(closeadj, 10)
    inter = (_std(base, 126)) * _mean(closeadj, 63)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_z21_close_jk21_126d_jerk_v121_signal(closeadj):
    base = _f018_magnet_score(closeadj, 126)
    inter = (_z(base, 21)) * closeadj
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_diff21_closesq_jk42_63d_jerk_v122_signal(closeadj):
    base = _f018_magnet_score(closeadj, 63)
    inter = ((base).diff(21)) * closeadj * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_sma21_closesq_jk42_126d_jerk_v123_signal(closeadj):
    base = _f018_round_distance(closeadj, 126)
    inter = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_z126_closesma21_jk63_21d_jerk_v124_signal(closeadj):
    base = _f018_magnet_score(closeadj, 21)
    inter = (_z(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_z252_closesq_jk10_252d_jerk_v125_signal(closeadj):
    base = _f018_round_distance(closeadj, 252)
    inter = (_z(base, 252)) * closeadj * closeadj
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_std126_closesma63_jk126_189d_jerk_v126_signal(closeadj):
    base = _f018_round_distance(closeadj, 189)
    inter = (_std(base, 126)) * _mean(closeadj, 63)
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_sma63_closesq_jk21_378d_jerk_v127_signal(closeadj):
    base = _f018_round_distance(closeadj, 378)
    inter = (_mean(base, 63)) * closeadj * closeadj
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_z63_closesma63_jk5_21d_jerk_v128_signal(closeadj):
    base = _f018_round_proximity(closeadj, 21)
    inter = (_z(base, 63)) * _mean(closeadj, 63)
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_diff21_closesq_jk21_189d_jerk_v129_signal(closeadj):
    base = _f018_round_proximity(closeadj, 189)
    inter = ((base).diff(21)) * closeadj * closeadj
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_z126_closesma21_jk5_189d_jerk_v130_signal(closeadj):
    base = _f018_magnet_score(closeadj, 189)
    inter = (_z(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_z63_closesq_jk126_252d_jerk_v131_signal(closeadj):
    base = _f018_magnet_score(closeadj, 252)
    inter = (_z(base, 63)) * closeadj * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_z63_closesma21_jk126_42d_jerk_v132_signal(closeadj):
    base = _f018_round_proximity(closeadj, 42)
    inter = (_z(base, 63)) * _mean(closeadj, 21)
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_diff63_closesma21_jk126_42d_jerk_v133_signal(closeadj):
    base = _f018_round_distance(closeadj, 42)
    inter = ((base).diff(63)) * _mean(closeadj, 21)
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_std63_close_jk126_189d_jerk_v134_signal(closeadj):
    base = _f018_round_distance(closeadj, 189)
    inter = (_std(base, 63)) * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_diff5_close_jk126_5d_jerk_v135_signal(closeadj):
    base = _f018_round_distance(closeadj, 5)
    inter = ((base).diff(5)) * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_std21_closesma63_jk21_378d_jerk_v136_signal(closeadj):
    base = _f018_round_distance(closeadj, 378)
    inter = (_std(base, 21)) * _mean(closeadj, 63)
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_diff63_closesma63_jk42_378d_jerk_v137_signal(closeadj):
    base = _f018_round_proximity(closeadj, 378)
    inter = ((base).diff(63)) * _mean(closeadj, 63)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_z126_closesma21_jk42_5d_jerk_v138_signal(closeadj):
    base = _f018_round_distance(closeadj, 5)
    inter = (_z(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_z63_closesma21_jk63_378d_jerk_v139_signal(closeadj):
    base = _f018_magnet_score(closeadj, 378)
    inter = (_z(base, 63)) * _mean(closeadj, 21)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_z252_closesma63_jk42_252d_jerk_v140_signal(closeadj):
    base = _f018_round_distance(closeadj, 252)
    inter = (_z(base, 252)) * _mean(closeadj, 63)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_std21_closesq_jk126_5d_jerk_v141_signal(closeadj):
    base = _f018_round_proximity(closeadj, 5)
    inter = (_std(base, 21)) * closeadj * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_z63_close_jk126_10d_jerk_v142_signal(closeadj):
    base = _f018_round_distance(closeadj, 10)
    inter = (_z(base, 63)) * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_z63_closesq_jk21_63d_jerk_v143_signal(closeadj):
    base = _f018_round_proximity(closeadj, 63)
    inter = (_z(base, 63)) * closeadj * closeadj
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_sma21_close_jk42_21d_jerk_v144_signal(closeadj):
    base = _f018_round_proximity(closeadj, 21)
    inter = (_mean(base, 21)) * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p3_std63_closesma21_jk5_504d_jerk_v145_signal(closeadj):
    base = _f018_magnet_score(closeadj, 504)
    inter = (_std(base, 63)) * _mean(closeadj, 21)
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_z126_closesq_jk10_42d_jerk_v146_signal(closeadj):
    base = _f018_round_proximity(closeadj, 42)
    inter = (_z(base, 126)) * closeadj * closeadj
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_z63_closesma21_jk21_10d_jerk_v147_signal(closeadj):
    base = _f018_round_proximity(closeadj, 10)
    inter = (_z(base, 63)) * _mean(closeadj, 21)
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p1_sma21_closesq_jk63_10d_jerk_v148_signal(closeadj):
    base = _f018_round_distance(closeadj, 10)
    inter = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_std21_closesma63_jk5_252d_jerk_v149_signal(closeadj):
    base = _f018_round_proximity(closeadj, 252)
    inter = (_std(base, 21)) * _mean(closeadj, 63)
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f018drn_f018_distance_to_round_number_p2_z21_closesma63_jk63_504d_jerk_v150_signal(closeadj):
    base = _f018_round_proximity(closeadj, 504)
    inter = (_z(base, 21)) * _mean(closeadj, 63)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f018drn_f018_distance_to_round_number_p2_z63_close_jk63_42d_jerk_v001_signal,
    f018drn_f018_distance_to_round_number_p2_z63_closesq_jk42_42d_jerk_v002_signal,
    f018drn_f018_distance_to_round_number_p2_std126_closesma63_jk63_63d_jerk_v003_signal,
    f018drn_f018_distance_to_round_number_p1_diff5_closesma63_jk42_378d_jerk_v004_signal,
    f018drn_f018_distance_to_round_number_p3_z252_closesq_jk63_189d_jerk_v005_signal,
    f018drn_f018_distance_to_round_number_p2_diff21_close_jk42_252d_jerk_v006_signal,
    f018drn_f018_distance_to_round_number_p2_diff63_closesq_jk21_5d_jerk_v007_signal,
    f018drn_f018_distance_to_round_number_p2_diff63_closesma21_jk5_252d_jerk_v008_signal,
    f018drn_f018_distance_to_round_number_p3_sma21_close_jk126_5d_jerk_v009_signal,
    f018drn_f018_distance_to_round_number_p1_z63_closesma63_jk21_63d_jerk_v010_signal,
    f018drn_f018_distance_to_round_number_p1_std126_close_jk5_504d_jerk_v011_signal,
    f018drn_f018_distance_to_round_number_p2_raw_closesma63_jk21_126d_jerk_v012_signal,
    f018drn_f018_distance_to_round_number_p1_sma21_closesq_jk42_504d_jerk_v013_signal,
    f018drn_f018_distance_to_round_number_p3_z21_close_jk63_63d_jerk_v014_signal,
    f018drn_f018_distance_to_round_number_p1_std21_closesma63_jk126_10d_jerk_v015_signal,
    f018drn_f018_distance_to_round_number_p3_diff63_close_jk21_42d_jerk_v016_signal,
    f018drn_f018_distance_to_round_number_p3_diff63_close_jk21_10d_jerk_v017_signal,
    f018drn_f018_distance_to_round_number_p3_raw_closesq_jk5_504d_jerk_v018_signal,
    f018drn_f018_distance_to_round_number_p3_sma126_closesma21_jk63_42d_jerk_v019_signal,
    f018drn_f018_distance_to_round_number_p3_z126_closesma21_jk42_189d_jerk_v020_signal,
    f018drn_f018_distance_to_round_number_p1_z21_closesma63_jk63_5d_jerk_v021_signal,
    f018drn_f018_distance_to_round_number_p3_std63_close_jk63_5d_jerk_v022_signal,
    f018drn_f018_distance_to_round_number_p3_std126_closesma21_jk42_10d_jerk_v023_signal,
    f018drn_f018_distance_to_round_number_p2_sma126_closesma21_jk10_42d_jerk_v024_signal,
    f018drn_f018_distance_to_round_number_p3_sma126_closesma21_jk21_378d_jerk_v025_signal,
    f018drn_f018_distance_to_round_number_p1_diff63_closesma63_jk126_126d_jerk_v026_signal,
    f018drn_f018_distance_to_round_number_p3_std126_closesma21_jk5_10d_jerk_v027_signal,
    f018drn_f018_distance_to_round_number_p2_diff5_closesma21_jk42_21d_jerk_v028_signal,
    f018drn_f018_distance_to_round_number_p1_std21_close_jk21_126d_jerk_v029_signal,
    f018drn_f018_distance_to_round_number_p1_sma126_closesma21_jk63_21d_jerk_v030_signal,
    f018drn_f018_distance_to_round_number_p2_z126_close_jk42_42d_jerk_v031_signal,
    f018drn_f018_distance_to_round_number_p3_z63_closesq_jk42_10d_jerk_v032_signal,
    f018drn_f018_distance_to_round_number_p1_diff5_closesq_jk21_378d_jerk_v033_signal,
    f018drn_f018_distance_to_round_number_p2_std126_closesma63_jk10_63d_jerk_v034_signal,
    f018drn_f018_distance_to_round_number_p3_sma126_closesma63_jk42_252d_jerk_v035_signal,
    f018drn_f018_distance_to_round_number_p1_raw_closesma21_jk42_189d_jerk_v036_signal,
    f018drn_f018_distance_to_round_number_p3_z63_closesma21_jk21_63d_jerk_v037_signal,
    f018drn_f018_distance_to_round_number_p2_diff63_closesq_jk63_63d_jerk_v038_signal,
    f018drn_f018_distance_to_round_number_p2_sma63_closesma21_jk5_5d_jerk_v039_signal,
    f018drn_f018_distance_to_round_number_p1_sma126_closesq_jk5_42d_jerk_v040_signal,
    f018drn_f018_distance_to_round_number_p2_sma63_closesma63_jk42_504d_jerk_v041_signal,
    f018drn_f018_distance_to_round_number_p2_sma21_closesma21_jk63_5d_jerk_v042_signal,
    f018drn_f018_distance_to_round_number_p3_diff63_close_jk126_189d_jerk_v043_signal,
    f018drn_f018_distance_to_round_number_p2_z126_closesma63_jk5_189d_jerk_v044_signal,
    f018drn_f018_distance_to_round_number_p2_std63_closesma21_jk10_63d_jerk_v045_signal,
    f018drn_f018_distance_to_round_number_p3_sma63_closesq_jk5_126d_jerk_v046_signal,
    f018drn_f018_distance_to_round_number_p1_diff21_close_jk5_378d_jerk_v047_signal,
    f018drn_f018_distance_to_round_number_p1_std63_closesma21_jk63_10d_jerk_v048_signal,
    f018drn_f018_distance_to_round_number_p1_raw_closesq_jk10_42d_jerk_v049_signal,
    f018drn_f018_distance_to_round_number_p3_diff21_close_jk10_10d_jerk_v050_signal,
    f018drn_f018_distance_to_round_number_p2_std21_closesma63_jk126_5d_jerk_v051_signal,
    f018drn_f018_distance_to_round_number_p1_std63_closesma63_jk63_63d_jerk_v052_signal,
    f018drn_f018_distance_to_round_number_p3_std63_closesma63_jk126_189d_jerk_v053_signal,
    f018drn_f018_distance_to_round_number_p3_diff5_closesma63_jk21_5d_jerk_v054_signal,
    f018drn_f018_distance_to_round_number_p3_std63_closesma63_jk10_126d_jerk_v055_signal,
    f018drn_f018_distance_to_round_number_p3_std63_closesma63_jk63_10d_jerk_v056_signal,
    f018drn_f018_distance_to_round_number_p1_std21_close_jk10_189d_jerk_v057_signal,
    f018drn_f018_distance_to_round_number_p3_z126_closesma21_jk10_252d_jerk_v058_signal,
    f018drn_f018_distance_to_round_number_p1_sma21_closesq_jk126_252d_jerk_v059_signal,
    f018drn_f018_distance_to_round_number_p1_z126_closesma21_jk63_126d_jerk_v060_signal,
    f018drn_f018_distance_to_round_number_p1_diff5_close_jk126_63d_jerk_v061_signal,
    f018drn_f018_distance_to_round_number_p1_diff21_closesma63_jk126_126d_jerk_v062_signal,
    f018drn_f018_distance_to_round_number_p2_std21_close_jk63_42d_jerk_v063_signal,
    f018drn_f018_distance_to_round_number_p2_sma63_closesma63_jk21_10d_jerk_v064_signal,
    f018drn_f018_distance_to_round_number_p1_z21_closesq_jk63_63d_jerk_v065_signal,
    f018drn_f018_distance_to_round_number_p1_z21_close_jk63_252d_jerk_v066_signal,
    f018drn_f018_distance_to_round_number_p1_diff5_closesma21_jk42_5d_jerk_v067_signal,
    f018drn_f018_distance_to_round_number_p2_diff21_closesma21_jk126_126d_jerk_v068_signal,
    f018drn_f018_distance_to_round_number_p2_sma63_close_jk21_252d_jerk_v069_signal,
    f018drn_f018_distance_to_round_number_p3_diff21_closesma21_jk42_378d_jerk_v070_signal,
    f018drn_f018_distance_to_round_number_p3_z21_closesma63_jk10_63d_jerk_v071_signal,
    f018drn_f018_distance_to_round_number_p3_diff5_closesq_jk10_378d_jerk_v072_signal,
    f018drn_f018_distance_to_round_number_p2_z21_close_jk42_378d_jerk_v073_signal,
    f018drn_f018_distance_to_round_number_p3_z63_closesq_jk126_5d_jerk_v074_signal,
    f018drn_f018_distance_to_round_number_p3_z252_close_jk10_42d_jerk_v075_signal,
    f018drn_f018_distance_to_round_number_p1_z252_closesma21_jk63_189d_jerk_v076_signal,
    f018drn_f018_distance_to_round_number_p3_z126_closesq_jk63_126d_jerk_v077_signal,
    f018drn_f018_distance_to_round_number_p1_std21_closesma63_jk126_21d_jerk_v078_signal,
    f018drn_f018_distance_to_round_number_p1_raw_close_jk5_21d_jerk_v079_signal,
    f018drn_f018_distance_to_round_number_p3_std126_closesma21_jk63_21d_jerk_v080_signal,
    f018drn_f018_distance_to_round_number_p2_raw_close_jk10_42d_jerk_v081_signal,
    f018drn_f018_distance_to_round_number_p1_std63_closesq_jk126_504d_jerk_v082_signal,
    f018drn_f018_distance_to_round_number_p3_std21_closesma21_jk10_378d_jerk_v083_signal,
    f018drn_f018_distance_to_round_number_p2_sma63_close_jk42_252d_jerk_v084_signal,
    f018drn_f018_distance_to_round_number_p3_diff21_closesma21_jk42_126d_jerk_v085_signal,
    f018drn_f018_distance_to_round_number_p2_sma126_close_jk42_42d_jerk_v086_signal,
    f018drn_f018_distance_to_round_number_p1_sma126_closesq_jk63_10d_jerk_v087_signal,
    f018drn_f018_distance_to_round_number_p1_z21_closesma63_jk63_63d_jerk_v088_signal,
    f018drn_f018_distance_to_round_number_p2_diff21_closesma63_jk21_42d_jerk_v089_signal,
    f018drn_f018_distance_to_round_number_p1_sma21_closesq_jk21_504d_jerk_v090_signal,
    f018drn_f018_distance_to_round_number_p2_sma63_closesma21_jk42_252d_jerk_v091_signal,
    f018drn_f018_distance_to_round_number_p1_z21_close_jk10_126d_jerk_v092_signal,
    f018drn_f018_distance_to_round_number_p3_z21_closesma21_jk42_504d_jerk_v093_signal,
    f018drn_f018_distance_to_round_number_p2_sma126_closesma21_jk5_42d_jerk_v094_signal,
    f018drn_f018_distance_to_round_number_p2_z21_closesma21_jk42_126d_jerk_v095_signal,
    f018drn_f018_distance_to_round_number_p1_sma21_close_jk42_10d_jerk_v096_signal,
    f018drn_f018_distance_to_round_number_p2_diff63_closesq_jk63_42d_jerk_v097_signal,
    f018drn_f018_distance_to_round_number_p3_z126_close_jk63_126d_jerk_v098_signal,
    f018drn_f018_distance_to_round_number_p1_diff21_closesq_jk21_21d_jerk_v099_signal,
    f018drn_f018_distance_to_round_number_p3_raw_closesma21_jk126_5d_jerk_v100_signal,
    f018drn_f018_distance_to_round_number_p1_diff63_closesma63_jk63_189d_jerk_v101_signal,
    f018drn_f018_distance_to_round_number_p3_diff5_closesma21_jk21_10d_jerk_v102_signal,
    f018drn_f018_distance_to_round_number_p1_sma126_closesma21_jk126_189d_jerk_v103_signal,
    f018drn_f018_distance_to_round_number_p2_diff5_closesma63_jk42_189d_jerk_v104_signal,
    f018drn_f018_distance_to_round_number_p3_z21_closesma21_jk42_5d_jerk_v105_signal,
    f018drn_f018_distance_to_round_number_p2_std21_close_jk126_10d_jerk_v106_signal,
    f018drn_f018_distance_to_round_number_p2_sma126_close_jk126_378d_jerk_v107_signal,
    f018drn_f018_distance_to_round_number_p1_sma126_closesma21_jk10_63d_jerk_v108_signal,
    f018drn_f018_distance_to_round_number_p3_diff5_closesma63_jk63_126d_jerk_v109_signal,
    f018drn_f018_distance_to_round_number_p3_z252_close_jk42_252d_jerk_v110_signal,
    f018drn_f018_distance_to_round_number_p2_raw_closesma21_jk126_126d_jerk_v111_signal,
    f018drn_f018_distance_to_round_number_p2_z252_closesma63_jk21_42d_jerk_v112_signal,
    f018drn_f018_distance_to_round_number_p2_z252_closesma63_jk5_63d_jerk_v113_signal,
    f018drn_f018_distance_to_round_number_p3_std63_closesq_jk63_504d_jerk_v114_signal,
    f018drn_f018_distance_to_round_number_p3_z252_closesq_jk42_5d_jerk_v115_signal,
    f018drn_f018_distance_to_round_number_p3_z126_close_jk42_126d_jerk_v116_signal,
    f018drn_f018_distance_to_round_number_p2_diff21_closesma21_jk21_378d_jerk_v117_signal,
    f018drn_f018_distance_to_round_number_p3_diff5_closesma63_jk42_42d_jerk_v118_signal,
    f018drn_f018_distance_to_round_number_p2_z21_closesq_jk10_189d_jerk_v119_signal,
    f018drn_f018_distance_to_round_number_p1_std126_closesma63_jk63_10d_jerk_v120_signal,
    f018drn_f018_distance_to_round_number_p3_z21_close_jk21_126d_jerk_v121_signal,
    f018drn_f018_distance_to_round_number_p3_diff21_closesq_jk42_63d_jerk_v122_signal,
    f018drn_f018_distance_to_round_number_p1_sma21_closesq_jk42_126d_jerk_v123_signal,
    f018drn_f018_distance_to_round_number_p3_z126_closesma21_jk63_21d_jerk_v124_signal,
    f018drn_f018_distance_to_round_number_p1_z252_closesq_jk10_252d_jerk_v125_signal,
    f018drn_f018_distance_to_round_number_p1_std126_closesma63_jk126_189d_jerk_v126_signal,
    f018drn_f018_distance_to_round_number_p1_sma63_closesq_jk21_378d_jerk_v127_signal,
    f018drn_f018_distance_to_round_number_p2_z63_closesma63_jk5_21d_jerk_v128_signal,
    f018drn_f018_distance_to_round_number_p2_diff21_closesq_jk21_189d_jerk_v129_signal,
    f018drn_f018_distance_to_round_number_p3_z126_closesma21_jk5_189d_jerk_v130_signal,
    f018drn_f018_distance_to_round_number_p3_z63_closesq_jk126_252d_jerk_v131_signal,
    f018drn_f018_distance_to_round_number_p2_z63_closesma21_jk126_42d_jerk_v132_signal,
    f018drn_f018_distance_to_round_number_p1_diff63_closesma21_jk126_42d_jerk_v133_signal,
    f018drn_f018_distance_to_round_number_p1_std63_close_jk126_189d_jerk_v134_signal,
    f018drn_f018_distance_to_round_number_p1_diff5_close_jk126_5d_jerk_v135_signal,
    f018drn_f018_distance_to_round_number_p1_std21_closesma63_jk21_378d_jerk_v136_signal,
    f018drn_f018_distance_to_round_number_p2_diff63_closesma63_jk42_378d_jerk_v137_signal,
    f018drn_f018_distance_to_round_number_p1_z126_closesma21_jk42_5d_jerk_v138_signal,
    f018drn_f018_distance_to_round_number_p3_z63_closesma21_jk63_378d_jerk_v139_signal,
    f018drn_f018_distance_to_round_number_p1_z252_closesma63_jk42_252d_jerk_v140_signal,
    f018drn_f018_distance_to_round_number_p2_std21_closesq_jk126_5d_jerk_v141_signal,
    f018drn_f018_distance_to_round_number_p1_z63_close_jk126_10d_jerk_v142_signal,
    f018drn_f018_distance_to_round_number_p2_z63_closesq_jk21_63d_jerk_v143_signal,
    f018drn_f018_distance_to_round_number_p2_sma21_close_jk42_21d_jerk_v144_signal,
    f018drn_f018_distance_to_round_number_p3_std63_closesma21_jk5_504d_jerk_v145_signal,
    f018drn_f018_distance_to_round_number_p2_z126_closesq_jk10_42d_jerk_v146_signal,
    f018drn_f018_distance_to_round_number_p2_z63_closesma21_jk21_10d_jerk_v147_signal,
    f018drn_f018_distance_to_round_number_p1_sma21_closesq_jk63_10d_jerk_v148_signal,
    f018drn_f018_distance_to_round_number_p2_std21_closesma63_jk5_252d_jerk_v149_signal,
    f018drn_f018_distance_to_round_number_p2_z21_closesma63_jk63_504d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F018_DISTANCE_TO_ROUND_NUMBER_REGISTRY_JERK_001_150 = REGISTRY


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
    domain_primitives = ('_f018_round_distance', '_f018_round_proximity', '_f018_magnet_score')
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
    print(f"OK f018_distance_to_round_number_3rd_derivatives_001_150_claude: {n_features} features pass")
