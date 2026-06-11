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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====

def _f020_bandwidth(closeadj, w):
    m = _mean(closeadj, w)
    sd = _std(closeadj, w)
    upper = m + 2 * sd
    lower = m - 2 * sd
    return (upper - lower) / m.replace(0, np.nan).abs()


def _f020_bb_squeeze(closeadj, w):
    bw = _f020_bandwidth(closeadj, w)
    bw_min = bw.rolling(w * 4, min_periods=max(1, w * 2)).min()
    return bw / bw_min.replace(0, np.nan)


def _f020_squeeze_intensity(closeadj, w):
    bw = _f020_bandwidth(closeadj, w)
    z = _z(bw, w * 2)
    return -z



# ===== features =====
def f020bbw_f020_bollinger_bandwidth_p3_sma63_closesma21_sd63_5d_slope_v001_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 5)
    inter = (_mean(base, 63)) * _mean(closeadj, 21)
    result = _slope_diff_norm(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_z63_closesma63_sp10_126d_slope_v002_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 126)
    inter = (_z(base, 63)) * _mean(closeadj, 63)
    result = _slope_pct(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_raw_closesq_sp42_504d_slope_v003_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 504)
    inter = (base) * closeadj * closeadj
    result = _slope_pct(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_diff63_close_sd63_10d_slope_v004_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 10)
    inter = ((base).diff(63)) * closeadj
    result = _slope_diff_norm(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_diff63_closesma63_sd21_42d_slope_v005_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 42)
    inter = ((base).diff(63)) * _mean(closeadj, 63)
    result = _slope_diff_norm(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_std63_closesq_sp42_189d_slope_v006_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 189)
    inter = (_std(base, 63)) * closeadj * closeadj
    result = _slope_pct(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_z21_closesq_sd42_42d_slope_v007_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 42)
    inter = (_z(base, 21)) * closeadj * closeadj
    result = _slope_diff_norm(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_z126_close_sd21_189d_slope_v008_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 189)
    inter = (_z(base, 126)) * closeadj
    result = _slope_diff_norm(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_z63_close_sd63_21d_slope_v009_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 21)
    inter = (_z(base, 63)) * closeadj
    result = _slope_diff_norm(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_sma21_closesma63_sp63_10d_slope_v010_signal(closeadj):
    base = _f020_bandwidth(closeadj, 10)
    inter = (_mean(base, 21)) * _mean(closeadj, 63)
    result = _slope_pct(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_z126_closesma21_sp63_126d_slope_v011_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 126)
    inter = (_z(base, 126)) * _mean(closeadj, 21)
    result = _slope_pct(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_std21_closesq_sd126_42d_slope_v012_signal(closeadj):
    base = _f020_bandwidth(closeadj, 42)
    inter = (_std(base, 21)) * closeadj * closeadj
    result = _slope_diff_norm(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_diff21_closesma63_sp21_126d_slope_v013_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 126)
    inter = ((base).diff(21)) * _mean(closeadj, 63)
    result = _slope_pct(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_std63_closesma63_sp126_10d_slope_v014_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 10)
    inter = (_std(base, 63)) * _mean(closeadj, 63)
    result = _slope_pct(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_z252_close_sd21_21d_slope_v015_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 21)
    inter = (_z(base, 252)) * closeadj
    result = _slope_diff_norm(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_diff21_closesma21_sd63_189d_slope_v016_signal(closeadj):
    base = _f020_bandwidth(closeadj, 189)
    inter = ((base).diff(21)) * _mean(closeadj, 21)
    result = _slope_diff_norm(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_std21_closesq_sd21_42d_slope_v017_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 42)
    inter = (_std(base, 21)) * closeadj * closeadj
    result = _slope_diff_norm(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_sma21_close_sd10_252d_slope_v018_signal(closeadj):
    base = _f020_bandwidth(closeadj, 252)
    inter = (_mean(base, 21)) * closeadj
    result = _slope_diff_norm(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_diff21_closesma63_sd42_63d_slope_v019_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 63)
    inter = ((base).diff(21)) * _mean(closeadj, 63)
    result = _slope_diff_norm(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_std63_close_sp10_42d_slope_v020_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 42)
    inter = (_std(base, 63)) * closeadj
    result = _slope_pct(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_z126_close_sp42_126d_slope_v021_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 126)
    inter = (_z(base, 126)) * closeadj
    result = _slope_pct(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_diff63_closesma21_sd10_252d_slope_v022_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 252)
    inter = ((base).diff(63)) * _mean(closeadj, 21)
    result = _slope_diff_norm(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_z63_closesma63_sd10_21d_slope_v023_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 21)
    inter = (_z(base, 63)) * _mean(closeadj, 63)
    result = _slope_diff_norm(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_std21_closesma63_sp5_189d_slope_v024_signal(closeadj):
    base = _f020_bandwidth(closeadj, 189)
    inter = (_std(base, 21)) * _mean(closeadj, 63)
    result = _slope_pct(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_z21_closesma21_sp21_252d_slope_v025_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 252)
    inter = (_z(base, 21)) * _mean(closeadj, 21)
    result = _slope_pct(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_z126_closesq_sd42_42d_slope_v026_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 42)
    inter = (_z(base, 126)) * closeadj * closeadj
    result = _slope_diff_norm(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_diff63_close_sp21_252d_slope_v027_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 252)
    inter = ((base).diff(63)) * closeadj
    result = _slope_pct(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_sma21_closesma63_sd10_189d_slope_v028_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 189)
    inter = (_mean(base, 21)) * _mean(closeadj, 63)
    result = _slope_diff_norm(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_std63_close_sp63_10d_slope_v029_signal(closeadj):
    base = _f020_bandwidth(closeadj, 10)
    inter = (_std(base, 63)) * closeadj
    result = _slope_pct(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_sma126_closesma21_sp5_21d_slope_v030_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 21)
    inter = (_mean(base, 126)) * _mean(closeadj, 21)
    result = _slope_pct(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_raw_close_sp5_189d_slope_v031_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 189)
    inter = (base) * closeadj
    result = _slope_pct(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_z63_close_sp42_10d_slope_v032_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 10)
    inter = (_z(base, 63)) * closeadj
    result = _slope_pct(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_std126_closesq_sp126_189d_slope_v033_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 189)
    inter = (_std(base, 126)) * closeadj * closeadj
    result = _slope_pct(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_std21_closesma21_sd63_378d_slope_v034_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 378)
    inter = (_std(base, 21)) * _mean(closeadj, 21)
    result = _slope_diff_norm(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_std63_closesma63_sp63_21d_slope_v035_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 21)
    inter = (_std(base, 63)) * _mean(closeadj, 63)
    result = _slope_pct(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_std63_close_sp126_5d_slope_v036_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 5)
    inter = (_std(base, 63)) * closeadj
    result = _slope_pct(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_diff21_closesma21_sp21_5d_slope_v037_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 5)
    inter = ((base).diff(21)) * _mean(closeadj, 21)
    result = _slope_pct(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_std21_close_sd5_5d_slope_v038_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 5)
    inter = (_std(base, 21)) * closeadj
    result = _slope_diff_norm(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_std63_closesq_sp21_63d_slope_v039_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 63)
    inter = (_std(base, 63)) * closeadj * closeadj
    result = _slope_pct(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_sma63_closesma63_sd63_252d_slope_v040_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 252)
    inter = (_mean(base, 63)) * _mean(closeadj, 63)
    result = _slope_diff_norm(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_diff21_closesq_sp21_5d_slope_v041_signal(closeadj):
    base = _f020_bandwidth(closeadj, 5)
    inter = ((base).diff(21)) * closeadj * closeadj
    result = _slope_pct(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_sma63_closesma21_sd42_10d_slope_v042_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 10)
    inter = (_mean(base, 63)) * _mean(closeadj, 21)
    result = _slope_diff_norm(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_diff21_closesma21_sp63_63d_slope_v043_signal(closeadj):
    base = _f020_bandwidth(closeadj, 63)
    inter = ((base).diff(21)) * _mean(closeadj, 21)
    result = _slope_pct(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_std21_closesma63_sd5_504d_slope_v044_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 504)
    inter = (_std(base, 21)) * _mean(closeadj, 63)
    result = _slope_diff_norm(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_z21_closesq_sp21_189d_slope_v045_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 189)
    inter = (_z(base, 21)) * closeadj * closeadj
    result = _slope_pct(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_z21_closesq_sp5_42d_slope_v046_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 42)
    inter = (_z(base, 21)) * closeadj * closeadj
    result = _slope_pct(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_diff63_closesma21_sd126_5d_slope_v047_signal(closeadj):
    base = _f020_bandwidth(closeadj, 5)
    inter = ((base).diff(63)) * _mean(closeadj, 21)
    result = _slope_diff_norm(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_z63_closesma21_sd63_378d_slope_v048_signal(closeadj):
    base = _f020_bandwidth(closeadj, 378)
    inter = (_z(base, 63)) * _mean(closeadj, 21)
    result = _slope_diff_norm(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_std21_closesma63_sp42_21d_slope_v049_signal(closeadj):
    base = _f020_bandwidth(closeadj, 21)
    inter = (_std(base, 21)) * _mean(closeadj, 63)
    result = _slope_pct(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_sma63_closesma63_sp42_252d_slope_v050_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 252)
    inter = (_mean(base, 63)) * _mean(closeadj, 63)
    result = _slope_pct(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_diff21_closesq_sp42_42d_slope_v051_signal(closeadj):
    base = _f020_bandwidth(closeadj, 42)
    inter = ((base).diff(21)) * closeadj * closeadj
    result = _slope_pct(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_std126_closesma63_sd42_252d_slope_v052_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 252)
    inter = (_std(base, 126)) * _mean(closeadj, 63)
    result = _slope_diff_norm(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_diff63_closesq_sd126_63d_slope_v053_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 63)
    inter = ((base).diff(63)) * closeadj * closeadj
    result = _slope_diff_norm(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_sma126_closesq_sp126_10d_slope_v054_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 10)
    inter = (_mean(base, 126)) * closeadj * closeadj
    result = _slope_pct(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_z252_closesma21_sd5_252d_slope_v055_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 252)
    inter = (_z(base, 252)) * _mean(closeadj, 21)
    result = _slope_diff_norm(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_diff5_closesma21_sd42_21d_slope_v056_signal(closeadj):
    base = _f020_bandwidth(closeadj, 21)
    inter = ((base).diff(5)) * _mean(closeadj, 21)
    result = _slope_diff_norm(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_sma126_close_sp5_21d_slope_v057_signal(closeadj):
    base = _f020_bandwidth(closeadj, 21)
    inter = (_mean(base, 126)) * closeadj
    result = _slope_pct(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_sma21_closesma63_sp10_252d_slope_v058_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 252)
    inter = (_mean(base, 21)) * _mean(closeadj, 63)
    result = _slope_pct(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_sma63_closesma21_sd126_252d_slope_v059_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 252)
    inter = (_mean(base, 63)) * _mean(closeadj, 21)
    result = _slope_diff_norm(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_sma21_close_sp42_63d_slope_v060_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 63)
    inter = (_mean(base, 21)) * closeadj
    result = _slope_pct(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_raw_closesma21_sp21_189d_slope_v061_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 189)
    inter = (base) * _mean(closeadj, 21)
    result = _slope_pct(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_z63_closesma63_sp5_5d_slope_v062_signal(closeadj):
    base = _f020_bandwidth(closeadj, 5)
    inter = (_z(base, 63)) * _mean(closeadj, 63)
    result = _slope_pct(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_raw_closesq_sd5_378d_slope_v063_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 378)
    inter = (base) * closeadj * closeadj
    result = _slope_diff_norm(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_z21_close_sp10_63d_slope_v064_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 63)
    inter = (_z(base, 21)) * closeadj
    result = _slope_pct(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_std126_close_sd5_126d_slope_v065_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 126)
    inter = (_std(base, 126)) * closeadj
    result = _slope_diff_norm(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_sma21_closesq_sd5_63d_slope_v066_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 63)
    inter = (_mean(base, 21)) * closeadj * closeadj
    result = _slope_diff_norm(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_z21_closesma63_sd42_126d_slope_v067_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 126)
    inter = (_z(base, 21)) * _mean(closeadj, 63)
    result = _slope_diff_norm(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_diff21_closesq_sd5_10d_slope_v068_signal(closeadj):
    base = _f020_bandwidth(closeadj, 10)
    inter = ((base).diff(21)) * closeadj * closeadj
    result = _slope_diff_norm(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_diff63_closesma63_sd21_126d_slope_v069_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 126)
    inter = ((base).diff(63)) * _mean(closeadj, 63)
    result = _slope_diff_norm(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_z252_closesq_sd10_504d_slope_v070_signal(closeadj):
    base = _f020_bandwidth(closeadj, 504)
    inter = (_z(base, 252)) * closeadj * closeadj
    result = _slope_diff_norm(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_diff21_closesma63_sp5_63d_slope_v071_signal(closeadj):
    base = _f020_bandwidth(closeadj, 63)
    inter = ((base).diff(21)) * _mean(closeadj, 63)
    result = _slope_pct(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_diff5_closesq_sp63_42d_slope_v072_signal(closeadj):
    base = _f020_bandwidth(closeadj, 42)
    inter = ((base).diff(5)) * closeadj * closeadj
    result = _slope_pct(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_sma21_closesq_sd10_378d_slope_v073_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 378)
    inter = (_mean(base, 21)) * closeadj * closeadj
    result = _slope_diff_norm(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_z21_close_sd10_10d_slope_v074_signal(closeadj):
    base = _f020_bandwidth(closeadj, 10)
    inter = (_z(base, 21)) * closeadj
    result = _slope_diff_norm(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_sma21_closesq_sd21_378d_slope_v075_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 378)
    inter = (_mean(base, 21)) * closeadj * closeadj
    result = _slope_diff_norm(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_raw_closesma21_sp126_42d_slope_v076_signal(closeadj):
    base = _f020_bandwidth(closeadj, 42)
    inter = (base) * _mean(closeadj, 21)
    result = _slope_pct(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_z63_closesma63_sp10_5d_slope_v077_signal(closeadj):
    base = _f020_bandwidth(closeadj, 5)
    inter = (_z(base, 63)) * _mean(closeadj, 63)
    result = _slope_pct(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_z252_closesq_sd42_378d_slope_v078_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 378)
    inter = (_z(base, 252)) * closeadj * closeadj
    result = _slope_diff_norm(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_std63_closesq_sd5_63d_slope_v079_signal(closeadj):
    base = _f020_bandwidth(closeadj, 63)
    inter = (_std(base, 63)) * closeadj * closeadj
    result = _slope_diff_norm(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_diff5_closesma63_sd126_126d_slope_v080_signal(closeadj):
    base = _f020_bandwidth(closeadj, 126)
    inter = ((base).diff(5)) * _mean(closeadj, 63)
    result = _slope_diff_norm(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_raw_closesma63_sd5_504d_slope_v081_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 504)
    inter = (base) * _mean(closeadj, 63)
    result = _slope_diff_norm(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_std63_closesma21_sd126_378d_slope_v082_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 378)
    inter = (_std(base, 63)) * _mean(closeadj, 21)
    result = _slope_diff_norm(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_z63_closesma21_sp63_42d_slope_v083_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 42)
    inter = (_z(base, 63)) * _mean(closeadj, 21)
    result = _slope_pct(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_sma126_closesq_sd42_378d_slope_v084_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 378)
    inter = (_mean(base, 126)) * closeadj * closeadj
    result = _slope_diff_norm(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_z252_close_sp10_126d_slope_v085_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 126)
    inter = (_z(base, 252)) * closeadj
    result = _slope_pct(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_raw_close_sp42_378d_slope_v086_signal(closeadj):
    base = _f020_bandwidth(closeadj, 378)
    inter = (base) * closeadj
    result = _slope_pct(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_sma21_close_sd10_5d_slope_v087_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 5)
    inter = (_mean(base, 21)) * closeadj
    result = _slope_diff_norm(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_z126_closesma21_sd5_189d_slope_v088_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 189)
    inter = (_z(base, 126)) * _mean(closeadj, 21)
    result = _slope_diff_norm(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_sma126_closesq_sd21_5d_slope_v089_signal(closeadj):
    base = _f020_bandwidth(closeadj, 5)
    inter = (_mean(base, 126)) * closeadj * closeadj
    result = _slope_diff_norm(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_diff21_closesma63_sp21_189d_slope_v090_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 189)
    inter = ((base).diff(21)) * _mean(closeadj, 63)
    result = _slope_pct(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_std126_closesq_sp42_10d_slope_v091_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 10)
    inter = (_std(base, 126)) * closeadj * closeadj
    result = _slope_pct(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_sma21_closesma21_sd10_126d_slope_v092_signal(closeadj):
    base = _f020_bandwidth(closeadj, 126)
    inter = (_mean(base, 21)) * _mean(closeadj, 21)
    result = _slope_diff_norm(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_diff21_closesq_sd21_189d_slope_v093_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 189)
    inter = ((base).diff(21)) * closeadj * closeadj
    result = _slope_diff_norm(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_diff21_closesq_sp63_126d_slope_v094_signal(closeadj):
    base = _f020_bandwidth(closeadj, 126)
    inter = ((base).diff(21)) * closeadj * closeadj
    result = _slope_pct(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_sma63_closesma63_sp10_10d_slope_v095_signal(closeadj):
    base = _f020_bandwidth(closeadj, 10)
    inter = (_mean(base, 63)) * _mean(closeadj, 63)
    result = _slope_pct(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_sma126_close_sd42_378d_slope_v096_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 378)
    inter = (_mean(base, 126)) * closeadj
    result = _slope_diff_norm(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_diff5_closesma63_sd10_504d_slope_v097_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 504)
    inter = ((base).diff(5)) * _mean(closeadj, 63)
    result = _slope_diff_norm(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_z126_closesq_sp42_5d_slope_v098_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 5)
    inter = (_z(base, 126)) * closeadj * closeadj
    result = _slope_pct(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_z21_closesq_sp126_5d_slope_v099_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 5)
    inter = (_z(base, 21)) * closeadj * closeadj
    result = _slope_pct(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_sma21_close_sd42_42d_slope_v100_signal(closeadj):
    base = _f020_bandwidth(closeadj, 42)
    inter = (_mean(base, 21)) * closeadj
    result = _slope_diff_norm(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_z21_closesma21_sp21_63d_slope_v101_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 63)
    inter = (_z(base, 21)) * _mean(closeadj, 21)
    result = _slope_pct(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_sma63_closesma63_sd21_189d_slope_v102_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 189)
    inter = (_mean(base, 63)) * _mean(closeadj, 63)
    result = _slope_diff_norm(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_diff63_close_sp42_5d_slope_v103_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 5)
    inter = ((base).diff(63)) * closeadj
    result = _slope_pct(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_std63_closesq_sp5_504d_slope_v104_signal(closeadj):
    base = _f020_bandwidth(closeadj, 504)
    inter = (_std(base, 63)) * closeadj * closeadj
    result = _slope_pct(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_sma21_closesma21_sp42_10d_slope_v105_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 10)
    inter = (_mean(base, 21)) * _mean(closeadj, 21)
    result = _slope_pct(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_sma21_closesma21_sp63_42d_slope_v106_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 42)
    inter = (_mean(base, 21)) * _mean(closeadj, 21)
    result = _slope_pct(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_raw_closesma21_sp42_5d_slope_v107_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 5)
    inter = (base) * _mean(closeadj, 21)
    result = _slope_pct(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_z252_closesq_sd126_252d_slope_v108_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 252)
    inter = (_z(base, 252)) * closeadj * closeadj
    result = _slope_diff_norm(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_z252_closesma21_sp126_42d_slope_v109_signal(closeadj):
    base = _f020_bandwidth(closeadj, 42)
    inter = (_z(base, 252)) * _mean(closeadj, 21)
    result = _slope_pct(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_std126_closesma21_sp10_63d_slope_v110_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 63)
    inter = (_std(base, 126)) * _mean(closeadj, 21)
    result = _slope_pct(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_z126_closesma63_sd5_42d_slope_v111_signal(closeadj):
    base = _f020_bandwidth(closeadj, 42)
    inter = (_z(base, 126)) * _mean(closeadj, 63)
    result = _slope_diff_norm(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_sma63_closesma21_sd5_42d_slope_v112_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 42)
    inter = (_mean(base, 63)) * _mean(closeadj, 21)
    result = _slope_diff_norm(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_std126_closesq_sd10_42d_slope_v113_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 42)
    inter = (_std(base, 126)) * closeadj * closeadj
    result = _slope_diff_norm(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_std63_close_sd21_126d_slope_v114_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 126)
    inter = (_std(base, 63)) * closeadj
    result = _slope_diff_norm(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_z21_closesma21_sd21_42d_slope_v115_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 42)
    inter = (_z(base, 21)) * _mean(closeadj, 21)
    result = _slope_diff_norm(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_diff63_closesq_sp21_63d_slope_v116_signal(closeadj):
    base = _f020_bandwidth(closeadj, 63)
    inter = ((base).diff(63)) * closeadj * closeadj
    result = _slope_pct(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_diff5_close_sp5_378d_slope_v117_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 378)
    inter = ((base).diff(5)) * closeadj
    result = _slope_pct(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_diff21_closesq_sd5_252d_slope_v118_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 252)
    inter = ((base).diff(21)) * closeadj * closeadj
    result = _slope_diff_norm(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_sma21_close_sd21_5d_slope_v119_signal(closeadj):
    base = _f020_bandwidth(closeadj, 5)
    inter = (_mean(base, 21)) * closeadj
    result = _slope_diff_norm(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_z126_closesma21_sp5_126d_slope_v120_signal(closeadj):
    base = _f020_bandwidth(closeadj, 126)
    inter = (_z(base, 126)) * _mean(closeadj, 21)
    result = _slope_pct(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_diff5_closesma21_sd63_21d_slope_v121_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 21)
    inter = ((base).diff(5)) * _mean(closeadj, 21)
    result = _slope_diff_norm(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_sma63_closesma21_sd5_126d_slope_v122_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 126)
    inter = (_mean(base, 63)) * _mean(closeadj, 21)
    result = _slope_diff_norm(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_diff63_closesma63_sp10_378d_slope_v123_signal(closeadj):
    base = _f020_bandwidth(closeadj, 378)
    inter = ((base).diff(63)) * _mean(closeadj, 63)
    result = _slope_pct(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_z126_closesma21_sd5_63d_slope_v124_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 63)
    inter = (_z(base, 126)) * _mean(closeadj, 21)
    result = _slope_diff_norm(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_z63_closesma21_sp126_126d_slope_v125_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 126)
    inter = (_z(base, 63)) * _mean(closeadj, 21)
    result = _slope_pct(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_diff21_closesma63_sp126_63d_slope_v126_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 63)
    inter = ((base).diff(21)) * _mean(closeadj, 63)
    result = _slope_pct(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_sma63_close_sp10_126d_slope_v127_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 126)
    inter = (_mean(base, 63)) * closeadj
    result = _slope_pct(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_z21_closesma63_sp10_252d_slope_v128_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 252)
    inter = (_z(base, 21)) * _mean(closeadj, 63)
    result = _slope_pct(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_z252_closesq_sd5_21d_slope_v129_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 21)
    inter = (_z(base, 252)) * closeadj * closeadj
    result = _slope_diff_norm(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_z21_closesq_sp10_10d_slope_v130_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 10)
    inter = (_z(base, 21)) * closeadj * closeadj
    result = _slope_pct(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_sma63_closesq_sp63_5d_slope_v131_signal(closeadj):
    base = _f020_bandwidth(closeadj, 5)
    inter = (_mean(base, 63)) * closeadj * closeadj
    result = _slope_pct(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_raw_closesma63_sd10_189d_slope_v132_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 189)
    inter = (base) * _mean(closeadj, 63)
    result = _slope_diff_norm(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_z21_closesma63_sd21_126d_slope_v133_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 126)
    inter = (_z(base, 21)) * _mean(closeadj, 63)
    result = _slope_diff_norm(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_raw_closesma21_sp21_5d_slope_v134_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 5)
    inter = (base) * _mean(closeadj, 21)
    result = _slope_pct(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_diff21_closesq_sd63_252d_slope_v135_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 252)
    inter = ((base).diff(21)) * closeadj * closeadj
    result = _slope_diff_norm(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_diff63_closesma63_sd5_63d_slope_v136_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 63)
    inter = ((base).diff(63)) * _mean(closeadj, 63)
    result = _slope_diff_norm(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_diff5_closesq_sd21_252d_slope_v137_signal(closeadj):
    base = _f020_bandwidth(closeadj, 252)
    inter = ((base).diff(5)) * closeadj * closeadj
    result = _slope_diff_norm(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_z126_close_sd42_63d_slope_v138_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 63)
    inter = (_z(base, 126)) * closeadj
    result = _slope_diff_norm(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_z126_closesma63_sp63_21d_slope_v139_signal(closeadj):
    base = _f020_bandwidth(closeadj, 21)
    inter = (_z(base, 126)) * _mean(closeadj, 63)
    result = _slope_pct(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_diff63_closesma21_sd5_126d_slope_v140_signal(closeadj):
    base = _f020_bandwidth(closeadj, 126)
    inter = ((base).diff(63)) * _mean(closeadj, 21)
    result = _slope_diff_norm(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_diff5_close_sp63_10d_slope_v141_signal(closeadj):
    base = _f020_bandwidth(closeadj, 10)
    inter = ((base).diff(5)) * closeadj
    result = _slope_pct(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_sma63_closesma21_sd5_504d_slope_v142_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 504)
    inter = (_mean(base, 63)) * _mean(closeadj, 21)
    result = _slope_diff_norm(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_std126_closesma21_sd42_378d_slope_v143_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 378)
    inter = (_std(base, 126)) * _mean(closeadj, 21)
    result = _slope_diff_norm(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_z126_closesq_sp21_126d_slope_v144_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 126)
    inter = (_z(base, 126)) * closeadj * closeadj
    result = _slope_pct(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_sma63_closesq_sd21_63d_slope_v145_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 63)
    inter = (_mean(base, 63)) * closeadj * closeadj
    result = _slope_diff_norm(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p1_z63_closesq_sp10_5d_slope_v146_signal(closeadj):
    base = _f020_bandwidth(closeadj, 5)
    inter = (_z(base, 63)) * closeadj * closeadj
    result = _slope_pct(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_diff5_closesma21_sd63_252d_slope_v147_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 252)
    inter = ((base).diff(5)) * _mean(closeadj, 21)
    result = _slope_diff_norm(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_z126_closesma21_sd10_10d_slope_v148_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 10)
    inter = (_z(base, 126)) * _mean(closeadj, 21)
    result = _slope_diff_norm(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p2_sma21_close_sp63_42d_slope_v149_signal(closeadj):
    base = _f020_bb_squeeze(closeadj, 42)
    inter = (_mean(base, 21)) * closeadj
    result = _slope_pct(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f020bbw_f020_bollinger_bandwidth_p3_std63_closesma21_sd126_5d_slope_v150_signal(closeadj):
    base = _f020_squeeze_intensity(closeadj, 5)
    inter = (_std(base, 63)) * _mean(closeadj, 21)
    result = _slope_diff_norm(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f020bbw_f020_bollinger_bandwidth_p3_sma63_closesma21_sd63_5d_slope_v001_signal,
    f020bbw_f020_bollinger_bandwidth_p3_z63_closesma63_sp10_126d_slope_v002_signal,
    f020bbw_f020_bollinger_bandwidth_p3_raw_closesq_sp42_504d_slope_v003_signal,
    f020bbw_f020_bollinger_bandwidth_p3_diff63_close_sd63_10d_slope_v004_signal,
    f020bbw_f020_bollinger_bandwidth_p3_diff63_closesma63_sd21_42d_slope_v005_signal,
    f020bbw_f020_bollinger_bandwidth_p3_std63_closesq_sp42_189d_slope_v006_signal,
    f020bbw_f020_bollinger_bandwidth_p2_z21_closesq_sd42_42d_slope_v007_signal,
    f020bbw_f020_bollinger_bandwidth_p3_z126_close_sd21_189d_slope_v008_signal,
    f020bbw_f020_bollinger_bandwidth_p3_z63_close_sd63_21d_slope_v009_signal,
    f020bbw_f020_bollinger_bandwidth_p1_sma21_closesma63_sp63_10d_slope_v010_signal,
    f020bbw_f020_bollinger_bandwidth_p2_z126_closesma21_sp63_126d_slope_v011_signal,
    f020bbw_f020_bollinger_bandwidth_p1_std21_closesq_sd126_42d_slope_v012_signal,
    f020bbw_f020_bollinger_bandwidth_p3_diff21_closesma63_sp21_126d_slope_v013_signal,
    f020bbw_f020_bollinger_bandwidth_p3_std63_closesma63_sp126_10d_slope_v014_signal,
    f020bbw_f020_bollinger_bandwidth_p2_z252_close_sd21_21d_slope_v015_signal,
    f020bbw_f020_bollinger_bandwidth_p1_diff21_closesma21_sd63_189d_slope_v016_signal,
    f020bbw_f020_bollinger_bandwidth_p2_std21_closesq_sd21_42d_slope_v017_signal,
    f020bbw_f020_bollinger_bandwidth_p1_sma21_close_sd10_252d_slope_v018_signal,
    f020bbw_f020_bollinger_bandwidth_p3_diff21_closesma63_sd42_63d_slope_v019_signal,
    f020bbw_f020_bollinger_bandwidth_p3_std63_close_sp10_42d_slope_v020_signal,
    f020bbw_f020_bollinger_bandwidth_p3_z126_close_sp42_126d_slope_v021_signal,
    f020bbw_f020_bollinger_bandwidth_p3_diff63_closesma21_sd10_252d_slope_v022_signal,
    f020bbw_f020_bollinger_bandwidth_p2_z63_closesma63_sd10_21d_slope_v023_signal,
    f020bbw_f020_bollinger_bandwidth_p1_std21_closesma63_sp5_189d_slope_v024_signal,
    f020bbw_f020_bollinger_bandwidth_p2_z21_closesma21_sp21_252d_slope_v025_signal,
    f020bbw_f020_bollinger_bandwidth_p2_z126_closesq_sd42_42d_slope_v026_signal,
    f020bbw_f020_bollinger_bandwidth_p3_diff63_close_sp21_252d_slope_v027_signal,
    f020bbw_f020_bollinger_bandwidth_p3_sma21_closesma63_sd10_189d_slope_v028_signal,
    f020bbw_f020_bollinger_bandwidth_p1_std63_close_sp63_10d_slope_v029_signal,
    f020bbw_f020_bollinger_bandwidth_p2_sma126_closesma21_sp5_21d_slope_v030_signal,
    f020bbw_f020_bollinger_bandwidth_p3_raw_close_sp5_189d_slope_v031_signal,
    f020bbw_f020_bollinger_bandwidth_p2_z63_close_sp42_10d_slope_v032_signal,
    f020bbw_f020_bollinger_bandwidth_p3_std126_closesq_sp126_189d_slope_v033_signal,
    f020bbw_f020_bollinger_bandwidth_p3_std21_closesma21_sd63_378d_slope_v034_signal,
    f020bbw_f020_bollinger_bandwidth_p2_std63_closesma63_sp63_21d_slope_v035_signal,
    f020bbw_f020_bollinger_bandwidth_p2_std63_close_sp126_5d_slope_v036_signal,
    f020bbw_f020_bollinger_bandwidth_p3_diff21_closesma21_sp21_5d_slope_v037_signal,
    f020bbw_f020_bollinger_bandwidth_p3_std21_close_sd5_5d_slope_v038_signal,
    f020bbw_f020_bollinger_bandwidth_p3_std63_closesq_sp21_63d_slope_v039_signal,
    f020bbw_f020_bollinger_bandwidth_p3_sma63_closesma63_sd63_252d_slope_v040_signal,
    f020bbw_f020_bollinger_bandwidth_p1_diff21_closesq_sp21_5d_slope_v041_signal,
    f020bbw_f020_bollinger_bandwidth_p2_sma63_closesma21_sd42_10d_slope_v042_signal,
    f020bbw_f020_bollinger_bandwidth_p1_diff21_closesma21_sp63_63d_slope_v043_signal,
    f020bbw_f020_bollinger_bandwidth_p3_std21_closesma63_sd5_504d_slope_v044_signal,
    f020bbw_f020_bollinger_bandwidth_p2_z21_closesq_sp21_189d_slope_v045_signal,
    f020bbw_f020_bollinger_bandwidth_p3_z21_closesq_sp5_42d_slope_v046_signal,
    f020bbw_f020_bollinger_bandwidth_p1_diff63_closesma21_sd126_5d_slope_v047_signal,
    f020bbw_f020_bollinger_bandwidth_p1_z63_closesma21_sd63_378d_slope_v048_signal,
    f020bbw_f020_bollinger_bandwidth_p1_std21_closesma63_sp42_21d_slope_v049_signal,
    f020bbw_f020_bollinger_bandwidth_p2_sma63_closesma63_sp42_252d_slope_v050_signal,
    f020bbw_f020_bollinger_bandwidth_p1_diff21_closesq_sp42_42d_slope_v051_signal,
    f020bbw_f020_bollinger_bandwidth_p3_std126_closesma63_sd42_252d_slope_v052_signal,
    f020bbw_f020_bollinger_bandwidth_p2_diff63_closesq_sd126_63d_slope_v053_signal,
    f020bbw_f020_bollinger_bandwidth_p3_sma126_closesq_sp126_10d_slope_v054_signal,
    f020bbw_f020_bollinger_bandwidth_p2_z252_closesma21_sd5_252d_slope_v055_signal,
    f020bbw_f020_bollinger_bandwidth_p1_diff5_closesma21_sd42_21d_slope_v056_signal,
    f020bbw_f020_bollinger_bandwidth_p1_sma126_close_sp5_21d_slope_v057_signal,
    f020bbw_f020_bollinger_bandwidth_p2_sma21_closesma63_sp10_252d_slope_v058_signal,
    f020bbw_f020_bollinger_bandwidth_p3_sma63_closesma21_sd126_252d_slope_v059_signal,
    f020bbw_f020_bollinger_bandwidth_p3_sma21_close_sp42_63d_slope_v060_signal,
    f020bbw_f020_bollinger_bandwidth_p2_raw_closesma21_sp21_189d_slope_v061_signal,
    f020bbw_f020_bollinger_bandwidth_p1_z63_closesma63_sp5_5d_slope_v062_signal,
    f020bbw_f020_bollinger_bandwidth_p3_raw_closesq_sd5_378d_slope_v063_signal,
    f020bbw_f020_bollinger_bandwidth_p3_z21_close_sp10_63d_slope_v064_signal,
    f020bbw_f020_bollinger_bandwidth_p3_std126_close_sd5_126d_slope_v065_signal,
    f020bbw_f020_bollinger_bandwidth_p3_sma21_closesq_sd5_63d_slope_v066_signal,
    f020bbw_f020_bollinger_bandwidth_p3_z21_closesma63_sd42_126d_slope_v067_signal,
    f020bbw_f020_bollinger_bandwidth_p1_diff21_closesq_sd5_10d_slope_v068_signal,
    f020bbw_f020_bollinger_bandwidth_p2_diff63_closesma63_sd21_126d_slope_v069_signal,
    f020bbw_f020_bollinger_bandwidth_p1_z252_closesq_sd10_504d_slope_v070_signal,
    f020bbw_f020_bollinger_bandwidth_p1_diff21_closesma63_sp5_63d_slope_v071_signal,
    f020bbw_f020_bollinger_bandwidth_p1_diff5_closesq_sp63_42d_slope_v072_signal,
    f020bbw_f020_bollinger_bandwidth_p2_sma21_closesq_sd10_378d_slope_v073_signal,
    f020bbw_f020_bollinger_bandwidth_p1_z21_close_sd10_10d_slope_v074_signal,
    f020bbw_f020_bollinger_bandwidth_p3_sma21_closesq_sd21_378d_slope_v075_signal,
    f020bbw_f020_bollinger_bandwidth_p1_raw_closesma21_sp126_42d_slope_v076_signal,
    f020bbw_f020_bollinger_bandwidth_p1_z63_closesma63_sp10_5d_slope_v077_signal,
    f020bbw_f020_bollinger_bandwidth_p3_z252_closesq_sd42_378d_slope_v078_signal,
    f020bbw_f020_bollinger_bandwidth_p1_std63_closesq_sd5_63d_slope_v079_signal,
    f020bbw_f020_bollinger_bandwidth_p1_diff5_closesma63_sd126_126d_slope_v080_signal,
    f020bbw_f020_bollinger_bandwidth_p3_raw_closesma63_sd5_504d_slope_v081_signal,
    f020bbw_f020_bollinger_bandwidth_p3_std63_closesma21_sd126_378d_slope_v082_signal,
    f020bbw_f020_bollinger_bandwidth_p2_z63_closesma21_sp63_42d_slope_v083_signal,
    f020bbw_f020_bollinger_bandwidth_p3_sma126_closesq_sd42_378d_slope_v084_signal,
    f020bbw_f020_bollinger_bandwidth_p3_z252_close_sp10_126d_slope_v085_signal,
    f020bbw_f020_bollinger_bandwidth_p1_raw_close_sp42_378d_slope_v086_signal,
    f020bbw_f020_bollinger_bandwidth_p3_sma21_close_sd10_5d_slope_v087_signal,
    f020bbw_f020_bollinger_bandwidth_p2_z126_closesma21_sd5_189d_slope_v088_signal,
    f020bbw_f020_bollinger_bandwidth_p1_sma126_closesq_sd21_5d_slope_v089_signal,
    f020bbw_f020_bollinger_bandwidth_p3_diff21_closesma63_sp21_189d_slope_v090_signal,
    f020bbw_f020_bollinger_bandwidth_p3_std126_closesq_sp42_10d_slope_v091_signal,
    f020bbw_f020_bollinger_bandwidth_p1_sma21_closesma21_sd10_126d_slope_v092_signal,
    f020bbw_f020_bollinger_bandwidth_p2_diff21_closesq_sd21_189d_slope_v093_signal,
    f020bbw_f020_bollinger_bandwidth_p1_diff21_closesq_sp63_126d_slope_v094_signal,
    f020bbw_f020_bollinger_bandwidth_p1_sma63_closesma63_sp10_10d_slope_v095_signal,
    f020bbw_f020_bollinger_bandwidth_p3_sma126_close_sd42_378d_slope_v096_signal,
    f020bbw_f020_bollinger_bandwidth_p3_diff5_closesma63_sd10_504d_slope_v097_signal,
    f020bbw_f020_bollinger_bandwidth_p2_z126_closesq_sp42_5d_slope_v098_signal,
    f020bbw_f020_bollinger_bandwidth_p2_z21_closesq_sp126_5d_slope_v099_signal,
    f020bbw_f020_bollinger_bandwidth_p1_sma21_close_sd42_42d_slope_v100_signal,
    f020bbw_f020_bollinger_bandwidth_p3_z21_closesma21_sp21_63d_slope_v101_signal,
    f020bbw_f020_bollinger_bandwidth_p3_sma63_closesma63_sd21_189d_slope_v102_signal,
    f020bbw_f020_bollinger_bandwidth_p3_diff63_close_sp42_5d_slope_v103_signal,
    f020bbw_f020_bollinger_bandwidth_p1_std63_closesq_sp5_504d_slope_v104_signal,
    f020bbw_f020_bollinger_bandwidth_p3_sma21_closesma21_sp42_10d_slope_v105_signal,
    f020bbw_f020_bollinger_bandwidth_p2_sma21_closesma21_sp63_42d_slope_v106_signal,
    f020bbw_f020_bollinger_bandwidth_p2_raw_closesma21_sp42_5d_slope_v107_signal,
    f020bbw_f020_bollinger_bandwidth_p2_z252_closesq_sd126_252d_slope_v108_signal,
    f020bbw_f020_bollinger_bandwidth_p1_z252_closesma21_sp126_42d_slope_v109_signal,
    f020bbw_f020_bollinger_bandwidth_p3_std126_closesma21_sp10_63d_slope_v110_signal,
    f020bbw_f020_bollinger_bandwidth_p1_z126_closesma63_sd5_42d_slope_v111_signal,
    f020bbw_f020_bollinger_bandwidth_p2_sma63_closesma21_sd5_42d_slope_v112_signal,
    f020bbw_f020_bollinger_bandwidth_p2_std126_closesq_sd10_42d_slope_v113_signal,
    f020bbw_f020_bollinger_bandwidth_p3_std63_close_sd21_126d_slope_v114_signal,
    f020bbw_f020_bollinger_bandwidth_p2_z21_closesma21_sd21_42d_slope_v115_signal,
    f020bbw_f020_bollinger_bandwidth_p1_diff63_closesq_sp21_63d_slope_v116_signal,
    f020bbw_f020_bollinger_bandwidth_p3_diff5_close_sp5_378d_slope_v117_signal,
    f020bbw_f020_bollinger_bandwidth_p3_diff21_closesq_sd5_252d_slope_v118_signal,
    f020bbw_f020_bollinger_bandwidth_p1_sma21_close_sd21_5d_slope_v119_signal,
    f020bbw_f020_bollinger_bandwidth_p1_z126_closesma21_sp5_126d_slope_v120_signal,
    f020bbw_f020_bollinger_bandwidth_p2_diff5_closesma21_sd63_21d_slope_v121_signal,
    f020bbw_f020_bollinger_bandwidth_p2_sma63_closesma21_sd5_126d_slope_v122_signal,
    f020bbw_f020_bollinger_bandwidth_p1_diff63_closesma63_sp10_378d_slope_v123_signal,
    f020bbw_f020_bollinger_bandwidth_p2_z126_closesma21_sd5_63d_slope_v124_signal,
    f020bbw_f020_bollinger_bandwidth_p3_z63_closesma21_sp126_126d_slope_v125_signal,
    f020bbw_f020_bollinger_bandwidth_p3_diff21_closesma63_sp126_63d_slope_v126_signal,
    f020bbw_f020_bollinger_bandwidth_p3_sma63_close_sp10_126d_slope_v127_signal,
    f020bbw_f020_bollinger_bandwidth_p2_z21_closesma63_sp10_252d_slope_v128_signal,
    f020bbw_f020_bollinger_bandwidth_p3_z252_closesq_sd5_21d_slope_v129_signal,
    f020bbw_f020_bollinger_bandwidth_p2_z21_closesq_sp10_10d_slope_v130_signal,
    f020bbw_f020_bollinger_bandwidth_p1_sma63_closesq_sp63_5d_slope_v131_signal,
    f020bbw_f020_bollinger_bandwidth_p3_raw_closesma63_sd10_189d_slope_v132_signal,
    f020bbw_f020_bollinger_bandwidth_p3_z21_closesma63_sd21_126d_slope_v133_signal,
    f020bbw_f020_bollinger_bandwidth_p2_raw_closesma21_sp21_5d_slope_v134_signal,
    f020bbw_f020_bollinger_bandwidth_p2_diff21_closesq_sd63_252d_slope_v135_signal,
    f020bbw_f020_bollinger_bandwidth_p2_diff63_closesma63_sd5_63d_slope_v136_signal,
    f020bbw_f020_bollinger_bandwidth_p1_diff5_closesq_sd21_252d_slope_v137_signal,
    f020bbw_f020_bollinger_bandwidth_p3_z126_close_sd42_63d_slope_v138_signal,
    f020bbw_f020_bollinger_bandwidth_p1_z126_closesma63_sp63_21d_slope_v139_signal,
    f020bbw_f020_bollinger_bandwidth_p1_diff63_closesma21_sd5_126d_slope_v140_signal,
    f020bbw_f020_bollinger_bandwidth_p1_diff5_close_sp63_10d_slope_v141_signal,
    f020bbw_f020_bollinger_bandwidth_p3_sma63_closesma21_sd5_504d_slope_v142_signal,
    f020bbw_f020_bollinger_bandwidth_p3_std126_closesma21_sd42_378d_slope_v143_signal,
    f020bbw_f020_bollinger_bandwidth_p2_z126_closesq_sp21_126d_slope_v144_signal,
    f020bbw_f020_bollinger_bandwidth_p2_sma63_closesq_sd21_63d_slope_v145_signal,
    f020bbw_f020_bollinger_bandwidth_p1_z63_closesq_sp10_5d_slope_v146_signal,
    f020bbw_f020_bollinger_bandwidth_p3_diff5_closesma21_sd63_252d_slope_v147_signal,
    f020bbw_f020_bollinger_bandwidth_p2_z126_closesma21_sd10_10d_slope_v148_signal,
    f020bbw_f020_bollinger_bandwidth_p2_sma21_close_sp63_42d_slope_v149_signal,
    f020bbw_f020_bollinger_bandwidth_p3_std63_closesma21_sd126_5d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F020_BOLLINGER_BANDWIDTH_REGISTRY_SLOPE_001_150 = REGISTRY


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
    domain_primitives = ('_f020_bandwidth', '_f020_bb_squeeze', '_f020_squeeze_intensity')
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
    print(f"OK f020_bollinger_bandwidth_2nd_derivatives_001_150_claude: {n_features} features pass")
