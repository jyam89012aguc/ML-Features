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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f060_up_streak(close, w):
    # Rolling fraction of up days (returns > 0)
    up = (close.diff() > 0).astype(float)
    return up.rolling(w, min_periods=max(1, w // 2)).mean()


def _f060_streak_length(close, w):
    # Current run length of same-sign returns scaled by w
    sgn = np.sign(close.diff()).fillna(0.0)
    grp = (sgn != sgn.shift(1)).astype(int).cumsum()
    run = sgn.groupby(grp).cumcount() + 1
    return run.astype(float) / float(w)


def _f060_streak_intensity(close, w):
    # Streak intensity: signed run length / w times magnitude of recent return
    sgn = np.sign(close.diff()).fillna(0.0)
    grp = (sgn != sgn.shift(1)).astype(int).cumsum()
    run = (sgn.groupby(grp).cumcount() + 1).astype(float)
    mag = close.pct_change().abs().rolling(w, min_periods=max(1, w // 2)).mean()
    return sgn * run * mag / float(w)



# ustk base_w=5 variant=xclose jerk_w=5
def f060stl_f060_streak_length_ustk_5d_xclose_jerk_v001_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xclose jerk_w=10
def f060stl_f060_streak_length_ustk_5d_xclose_jerk_v002_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xclose jerk_w=21
def f060stl_f060_streak_length_ustk_5d_xclose_jerk_v003_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xclose jerk_w=42
def f060stl_f060_streak_length_ustk_5d_xclose_jerk_v004_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xclose jerk_w=63
def f060stl_f060_streak_length_ustk_5d_xclose_jerk_v005_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xclose jerk_w=126
def f060stl_f060_streak_length_ustk_5d_xclose_jerk_v006_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xmean21 jerk_w=5
def f060stl_f060_streak_length_ustk_5d_xmean21_jerk_v007_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xmean21 jerk_w=10
def f060stl_f060_streak_length_ustk_5d_xmean21_jerk_v008_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * _mean(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xmean21 jerk_w=21
def f060stl_f060_streak_length_ustk_5d_xmean21_jerk_v009_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * _mean(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xmean21 jerk_w=42
def f060stl_f060_streak_length_ustk_5d_xmean21_jerk_v010_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * _mean(closeadj, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xmean21 jerk_w=63
def f060stl_f060_streak_length_ustk_5d_xmean21_jerk_v011_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * _mean(closeadj, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xmean21 jerk_w=126
def f060stl_f060_streak_length_ustk_5d_xmean21_jerk_v012_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * _mean(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xmean63 jerk_w=5
def f060stl_f060_streak_length_ustk_5d_xmean63_jerk_v013_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xmean63 jerk_w=10
def f060stl_f060_streak_length_ustk_5d_xmean63_jerk_v014_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * _mean(closeadj, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xmean63 jerk_w=21
def f060stl_f060_streak_length_ustk_5d_xmean63_jerk_v015_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * _mean(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xmean63 jerk_w=42
def f060stl_f060_streak_length_ustk_5d_xmean63_jerk_v016_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * _mean(closeadj, 63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xmean63 jerk_w=63
def f060stl_f060_streak_length_ustk_5d_xmean63_jerk_v017_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * _mean(closeadj, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xmean63 jerk_w=126
def f060stl_f060_streak_length_ustk_5d_xmean63_jerk_v018_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * _mean(closeadj, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xstd63 jerk_w=5
def f060stl_f060_streak_length_ustk_5d_xstd63_jerk_v019_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * _std(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xstd63 jerk_w=10
def f060stl_f060_streak_length_ustk_5d_xstd63_jerk_v020_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * _std(closeadj, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xstd63 jerk_w=21
def f060stl_f060_streak_length_ustk_5d_xstd63_jerk_v021_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * _std(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xstd63 jerk_w=42
def f060stl_f060_streak_length_ustk_5d_xstd63_jerk_v022_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * _std(closeadj, 63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xstd63 jerk_w=63
def f060stl_f060_streak_length_ustk_5d_xstd63_jerk_v023_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * _std(closeadj, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xstd63 jerk_w=126
def f060stl_f060_streak_length_ustk_5d_xstd63_jerk_v024_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * _std(closeadj, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xclosesq jerk_w=5
def f060stl_f060_streak_length_ustk_5d_xclosesq_jerk_v025_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * closeadj * closeadj / 100.0
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xclosesq jerk_w=10
def f060stl_f060_streak_length_ustk_5d_xclosesq_jerk_v026_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * closeadj * closeadj / 100.0
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xclosesq jerk_w=21
def f060stl_f060_streak_length_ustk_5d_xclosesq_jerk_v027_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * closeadj * closeadj / 100.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xclosesq jerk_w=42
def f060stl_f060_streak_length_ustk_5d_xclosesq_jerk_v028_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * closeadj * closeadj / 100.0
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xclosesq jerk_w=63
def f060stl_f060_streak_length_ustk_5d_xclosesq_jerk_v029_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * closeadj * closeadj / 100.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xclosesq jerk_w=126
def f060stl_f060_streak_length_ustk_5d_xclosesq_jerk_v030_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * closeadj * closeadj / 100.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xclose2 jerk_w=5
def f060stl_f060_streak_length_ustk_5d_xclose2_jerk_v031_signal(closeadj):
    base = (_f060_up_streak(closeadj, 5) + closeadj) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xclose2 jerk_w=10
def f060stl_f060_streak_length_ustk_5d_xclose2_jerk_v032_signal(closeadj):
    base = (_f060_up_streak(closeadj, 5) + closeadj) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xclose2 jerk_w=21
def f060stl_f060_streak_length_ustk_5d_xclose2_jerk_v033_signal(closeadj):
    base = (_f060_up_streak(closeadj, 5) + closeadj) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xclose2 jerk_w=42
def f060stl_f060_streak_length_ustk_5d_xclose2_jerk_v034_signal(closeadj):
    base = (_f060_up_streak(closeadj, 5) + closeadj) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xclose2 jerk_w=63
def f060stl_f060_streak_length_ustk_5d_xclose2_jerk_v035_signal(closeadj):
    base = (_f060_up_streak(closeadj, 5) + closeadj) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xclose2 jerk_w=126
def f060stl_f060_streak_length_ustk_5d_xclose2_jerk_v036_signal(closeadj):
    base = (_f060_up_streak(closeadj, 5) + closeadj) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xema21 jerk_w=5
def f060stl_f060_streak_length_ustk_5d_xema21_jerk_v037_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * closeadj.ewm(span=21, min_periods=10).mean()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xema21 jerk_w=10
def f060stl_f060_streak_length_ustk_5d_xema21_jerk_v038_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * closeadj.ewm(span=21, min_periods=10).mean()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xema21 jerk_w=21
def f060stl_f060_streak_length_ustk_5d_xema21_jerk_v039_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * closeadj.ewm(span=21, min_periods=10).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xema21 jerk_w=42
def f060stl_f060_streak_length_ustk_5d_xema21_jerk_v040_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * closeadj.ewm(span=21, min_periods=10).mean()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xema21 jerk_w=63
def f060stl_f060_streak_length_ustk_5d_xema21_jerk_v041_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * closeadj.ewm(span=21, min_periods=10).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xema21 jerk_w=126
def f060stl_f060_streak_length_ustk_5d_xema21_jerk_v042_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * closeadj.ewm(span=21, min_periods=10).mean()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xema63 jerk_w=5
def f060stl_f060_streak_length_ustk_5d_xema63_jerk_v043_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * closeadj.ewm(span=63, min_periods=21).mean()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xema63 jerk_w=10
def f060stl_f060_streak_length_ustk_5d_xema63_jerk_v044_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * closeadj.ewm(span=63, min_periods=21).mean()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xema63 jerk_w=21
def f060stl_f060_streak_length_ustk_5d_xema63_jerk_v045_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * closeadj.ewm(span=63, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xema63 jerk_w=42
def f060stl_f060_streak_length_ustk_5d_xema63_jerk_v046_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * closeadj.ewm(span=63, min_periods=21).mean()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xema63 jerk_w=63
def f060stl_f060_streak_length_ustk_5d_xema63_jerk_v047_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * closeadj.ewm(span=63, min_periods=21).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xema63 jerk_w=126
def f060stl_f060_streak_length_ustk_5d_xema63_jerk_v048_signal(closeadj):
    base = _f060_up_streak(closeadj, 5) * closeadj.ewm(span=63, min_periods=21).mean()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xmix jerk_w=5
def f060stl_f060_streak_length_ustk_5d_xmix_jerk_v049_signal(closeadj):
    base = (_f060_up_streak(closeadj, 5) * closeadj + _mean(closeadj, 63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xmix jerk_w=10
def f060stl_f060_streak_length_ustk_5d_xmix_jerk_v050_signal(closeadj):
    base = (_f060_up_streak(closeadj, 5) * closeadj + _mean(closeadj, 63))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xmix jerk_w=21
def f060stl_f060_streak_length_ustk_5d_xmix_jerk_v051_signal(closeadj):
    base = (_f060_up_streak(closeadj, 5) * closeadj + _mean(closeadj, 63))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xmix jerk_w=42
def f060stl_f060_streak_length_ustk_5d_xmix_jerk_v052_signal(closeadj):
    base = (_f060_up_streak(closeadj, 5) * closeadj + _mean(closeadj, 63))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xmix jerk_w=63
def f060stl_f060_streak_length_ustk_5d_xmix_jerk_v053_signal(closeadj):
    base = (_f060_up_streak(closeadj, 5) * closeadj + _mean(closeadj, 63))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xmix jerk_w=126
def f060stl_f060_streak_length_ustk_5d_xmix_jerk_v054_signal(closeadj):
    base = (_f060_up_streak(closeadj, 5) * closeadj + _mean(closeadj, 63))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xmix2 jerk_w=5
def f060stl_f060_streak_length_ustk_5d_xmix2_jerk_v055_signal(closeadj):
    base = (_f060_up_streak(closeadj, 5) * closeadj - _mean(closeadj, 126))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xmix2 jerk_w=10
def f060stl_f060_streak_length_ustk_5d_xmix2_jerk_v056_signal(closeadj):
    base = (_f060_up_streak(closeadj, 5) * closeadj - _mean(closeadj, 126))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xmix2 jerk_w=21
def f060stl_f060_streak_length_ustk_5d_xmix2_jerk_v057_signal(closeadj):
    base = (_f060_up_streak(closeadj, 5) * closeadj - _mean(closeadj, 126))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xmix2 jerk_w=42
def f060stl_f060_streak_length_ustk_5d_xmix2_jerk_v058_signal(closeadj):
    base = (_f060_up_streak(closeadj, 5) * closeadj - _mean(closeadj, 126))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xmix2 jerk_w=63
def f060stl_f060_streak_length_ustk_5d_xmix2_jerk_v059_signal(closeadj):
    base = (_f060_up_streak(closeadj, 5) * closeadj - _mean(closeadj, 126))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=5 variant=xmix2 jerk_w=126
def f060stl_f060_streak_length_ustk_5d_xmix2_jerk_v060_signal(closeadj):
    base = (_f060_up_streak(closeadj, 5) * closeadj - _mean(closeadj, 126))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xclose jerk_w=5
def f060stl_f060_streak_length_ustk_10d_xclose_jerk_v061_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xclose jerk_w=10
def f060stl_f060_streak_length_ustk_10d_xclose_jerk_v062_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xclose jerk_w=21
def f060stl_f060_streak_length_ustk_10d_xclose_jerk_v063_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xclose jerk_w=42
def f060stl_f060_streak_length_ustk_10d_xclose_jerk_v064_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xclose jerk_w=63
def f060stl_f060_streak_length_ustk_10d_xclose_jerk_v065_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xclose jerk_w=126
def f060stl_f060_streak_length_ustk_10d_xclose_jerk_v066_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xmean21 jerk_w=5
def f060stl_f060_streak_length_ustk_10d_xmean21_jerk_v067_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xmean21 jerk_w=10
def f060stl_f060_streak_length_ustk_10d_xmean21_jerk_v068_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * _mean(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xmean21 jerk_w=21
def f060stl_f060_streak_length_ustk_10d_xmean21_jerk_v069_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * _mean(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xmean21 jerk_w=42
def f060stl_f060_streak_length_ustk_10d_xmean21_jerk_v070_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * _mean(closeadj, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xmean21 jerk_w=63
def f060stl_f060_streak_length_ustk_10d_xmean21_jerk_v071_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * _mean(closeadj, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xmean21 jerk_w=126
def f060stl_f060_streak_length_ustk_10d_xmean21_jerk_v072_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * _mean(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xmean63 jerk_w=5
def f060stl_f060_streak_length_ustk_10d_xmean63_jerk_v073_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xmean63 jerk_w=10
def f060stl_f060_streak_length_ustk_10d_xmean63_jerk_v074_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * _mean(closeadj, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xmean63 jerk_w=21
def f060stl_f060_streak_length_ustk_10d_xmean63_jerk_v075_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * _mean(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xmean63 jerk_w=42
def f060stl_f060_streak_length_ustk_10d_xmean63_jerk_v076_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * _mean(closeadj, 63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xmean63 jerk_w=63
def f060stl_f060_streak_length_ustk_10d_xmean63_jerk_v077_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * _mean(closeadj, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xmean63 jerk_w=126
def f060stl_f060_streak_length_ustk_10d_xmean63_jerk_v078_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * _mean(closeadj, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xstd63 jerk_w=5
def f060stl_f060_streak_length_ustk_10d_xstd63_jerk_v079_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * _std(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xstd63 jerk_w=10
def f060stl_f060_streak_length_ustk_10d_xstd63_jerk_v080_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * _std(closeadj, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xstd63 jerk_w=21
def f060stl_f060_streak_length_ustk_10d_xstd63_jerk_v081_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * _std(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xstd63 jerk_w=42
def f060stl_f060_streak_length_ustk_10d_xstd63_jerk_v082_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * _std(closeadj, 63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xstd63 jerk_w=63
def f060stl_f060_streak_length_ustk_10d_xstd63_jerk_v083_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * _std(closeadj, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xstd63 jerk_w=126
def f060stl_f060_streak_length_ustk_10d_xstd63_jerk_v084_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * _std(closeadj, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xclosesq jerk_w=5
def f060stl_f060_streak_length_ustk_10d_xclosesq_jerk_v085_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * closeadj * closeadj / 100.0
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xclosesq jerk_w=10
def f060stl_f060_streak_length_ustk_10d_xclosesq_jerk_v086_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * closeadj * closeadj / 100.0
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xclosesq jerk_w=21
def f060stl_f060_streak_length_ustk_10d_xclosesq_jerk_v087_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * closeadj * closeadj / 100.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xclosesq jerk_w=42
def f060stl_f060_streak_length_ustk_10d_xclosesq_jerk_v088_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * closeadj * closeadj / 100.0
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xclosesq jerk_w=63
def f060stl_f060_streak_length_ustk_10d_xclosesq_jerk_v089_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * closeadj * closeadj / 100.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xclosesq jerk_w=126
def f060stl_f060_streak_length_ustk_10d_xclosesq_jerk_v090_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * closeadj * closeadj / 100.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xclose2 jerk_w=5
def f060stl_f060_streak_length_ustk_10d_xclose2_jerk_v091_signal(closeadj):
    base = (_f060_up_streak(closeadj, 10) + closeadj) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xclose2 jerk_w=10
def f060stl_f060_streak_length_ustk_10d_xclose2_jerk_v092_signal(closeadj):
    base = (_f060_up_streak(closeadj, 10) + closeadj) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xclose2 jerk_w=21
def f060stl_f060_streak_length_ustk_10d_xclose2_jerk_v093_signal(closeadj):
    base = (_f060_up_streak(closeadj, 10) + closeadj) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xclose2 jerk_w=42
def f060stl_f060_streak_length_ustk_10d_xclose2_jerk_v094_signal(closeadj):
    base = (_f060_up_streak(closeadj, 10) + closeadj) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xclose2 jerk_w=63
def f060stl_f060_streak_length_ustk_10d_xclose2_jerk_v095_signal(closeadj):
    base = (_f060_up_streak(closeadj, 10) + closeadj) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xclose2 jerk_w=126
def f060stl_f060_streak_length_ustk_10d_xclose2_jerk_v096_signal(closeadj):
    base = (_f060_up_streak(closeadj, 10) + closeadj) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xema21 jerk_w=5
def f060stl_f060_streak_length_ustk_10d_xema21_jerk_v097_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * closeadj.ewm(span=21, min_periods=10).mean()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xema21 jerk_w=10
def f060stl_f060_streak_length_ustk_10d_xema21_jerk_v098_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * closeadj.ewm(span=21, min_periods=10).mean()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xema21 jerk_w=21
def f060stl_f060_streak_length_ustk_10d_xema21_jerk_v099_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * closeadj.ewm(span=21, min_periods=10).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xema21 jerk_w=42
def f060stl_f060_streak_length_ustk_10d_xema21_jerk_v100_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * closeadj.ewm(span=21, min_periods=10).mean()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xema21 jerk_w=63
def f060stl_f060_streak_length_ustk_10d_xema21_jerk_v101_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * closeadj.ewm(span=21, min_periods=10).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xema21 jerk_w=126
def f060stl_f060_streak_length_ustk_10d_xema21_jerk_v102_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * closeadj.ewm(span=21, min_periods=10).mean()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xema63 jerk_w=5
def f060stl_f060_streak_length_ustk_10d_xema63_jerk_v103_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * closeadj.ewm(span=63, min_periods=21).mean()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xema63 jerk_w=10
def f060stl_f060_streak_length_ustk_10d_xema63_jerk_v104_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * closeadj.ewm(span=63, min_periods=21).mean()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xema63 jerk_w=21
def f060stl_f060_streak_length_ustk_10d_xema63_jerk_v105_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * closeadj.ewm(span=63, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xema63 jerk_w=42
def f060stl_f060_streak_length_ustk_10d_xema63_jerk_v106_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * closeadj.ewm(span=63, min_periods=21).mean()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xema63 jerk_w=63
def f060stl_f060_streak_length_ustk_10d_xema63_jerk_v107_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * closeadj.ewm(span=63, min_periods=21).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xema63 jerk_w=126
def f060stl_f060_streak_length_ustk_10d_xema63_jerk_v108_signal(closeadj):
    base = _f060_up_streak(closeadj, 10) * closeadj.ewm(span=63, min_periods=21).mean()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xmix jerk_w=5
def f060stl_f060_streak_length_ustk_10d_xmix_jerk_v109_signal(closeadj):
    base = (_f060_up_streak(closeadj, 10) * closeadj + _mean(closeadj, 63))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xmix jerk_w=10
def f060stl_f060_streak_length_ustk_10d_xmix_jerk_v110_signal(closeadj):
    base = (_f060_up_streak(closeadj, 10) * closeadj + _mean(closeadj, 63))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xmix jerk_w=21
def f060stl_f060_streak_length_ustk_10d_xmix_jerk_v111_signal(closeadj):
    base = (_f060_up_streak(closeadj, 10) * closeadj + _mean(closeadj, 63))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xmix jerk_w=42
def f060stl_f060_streak_length_ustk_10d_xmix_jerk_v112_signal(closeadj):
    base = (_f060_up_streak(closeadj, 10) * closeadj + _mean(closeadj, 63))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xmix jerk_w=63
def f060stl_f060_streak_length_ustk_10d_xmix_jerk_v113_signal(closeadj):
    base = (_f060_up_streak(closeadj, 10) * closeadj + _mean(closeadj, 63))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xmix jerk_w=126
def f060stl_f060_streak_length_ustk_10d_xmix_jerk_v114_signal(closeadj):
    base = (_f060_up_streak(closeadj, 10) * closeadj + _mean(closeadj, 63))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xmix2 jerk_w=5
def f060stl_f060_streak_length_ustk_10d_xmix2_jerk_v115_signal(closeadj):
    base = (_f060_up_streak(closeadj, 10) * closeadj - _mean(closeadj, 126))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xmix2 jerk_w=10
def f060stl_f060_streak_length_ustk_10d_xmix2_jerk_v116_signal(closeadj):
    base = (_f060_up_streak(closeadj, 10) * closeadj - _mean(closeadj, 126))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xmix2 jerk_w=21
def f060stl_f060_streak_length_ustk_10d_xmix2_jerk_v117_signal(closeadj):
    base = (_f060_up_streak(closeadj, 10) * closeadj - _mean(closeadj, 126))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xmix2 jerk_w=42
def f060stl_f060_streak_length_ustk_10d_xmix2_jerk_v118_signal(closeadj):
    base = (_f060_up_streak(closeadj, 10) * closeadj - _mean(closeadj, 126))
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xmix2 jerk_w=63
def f060stl_f060_streak_length_ustk_10d_xmix2_jerk_v119_signal(closeadj):
    base = (_f060_up_streak(closeadj, 10) * closeadj - _mean(closeadj, 126))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=10 variant=xmix2 jerk_w=126
def f060stl_f060_streak_length_ustk_10d_xmix2_jerk_v120_signal(closeadj):
    base = (_f060_up_streak(closeadj, 10) * closeadj - _mean(closeadj, 126))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xclose jerk_w=5
def f060stl_f060_streak_length_ustk_21d_xclose_jerk_v121_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xclose jerk_w=10
def f060stl_f060_streak_length_ustk_21d_xclose_jerk_v122_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xclose jerk_w=21
def f060stl_f060_streak_length_ustk_21d_xclose_jerk_v123_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xclose jerk_w=42
def f060stl_f060_streak_length_ustk_21d_xclose_jerk_v124_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xclose jerk_w=63
def f060stl_f060_streak_length_ustk_21d_xclose_jerk_v125_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xclose jerk_w=126
def f060stl_f060_streak_length_ustk_21d_xclose_jerk_v126_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xmean21 jerk_w=5
def f060stl_f060_streak_length_ustk_21d_xmean21_jerk_v127_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xmean21 jerk_w=10
def f060stl_f060_streak_length_ustk_21d_xmean21_jerk_v128_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * _mean(closeadj, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xmean21 jerk_w=21
def f060stl_f060_streak_length_ustk_21d_xmean21_jerk_v129_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * _mean(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xmean21 jerk_w=42
def f060stl_f060_streak_length_ustk_21d_xmean21_jerk_v130_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * _mean(closeadj, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xmean21 jerk_w=63
def f060stl_f060_streak_length_ustk_21d_xmean21_jerk_v131_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * _mean(closeadj, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xmean21 jerk_w=126
def f060stl_f060_streak_length_ustk_21d_xmean21_jerk_v132_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * _mean(closeadj, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xmean63 jerk_w=5
def f060stl_f060_streak_length_ustk_21d_xmean63_jerk_v133_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * _mean(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xmean63 jerk_w=10
def f060stl_f060_streak_length_ustk_21d_xmean63_jerk_v134_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * _mean(closeadj, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xmean63 jerk_w=21
def f060stl_f060_streak_length_ustk_21d_xmean63_jerk_v135_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * _mean(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xmean63 jerk_w=42
def f060stl_f060_streak_length_ustk_21d_xmean63_jerk_v136_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * _mean(closeadj, 63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xmean63 jerk_w=63
def f060stl_f060_streak_length_ustk_21d_xmean63_jerk_v137_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * _mean(closeadj, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xmean63 jerk_w=126
def f060stl_f060_streak_length_ustk_21d_xmean63_jerk_v138_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * _mean(closeadj, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xstd63 jerk_w=5
def f060stl_f060_streak_length_ustk_21d_xstd63_jerk_v139_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * _std(closeadj, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xstd63 jerk_w=10
def f060stl_f060_streak_length_ustk_21d_xstd63_jerk_v140_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * _std(closeadj, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xstd63 jerk_w=21
def f060stl_f060_streak_length_ustk_21d_xstd63_jerk_v141_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * _std(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xstd63 jerk_w=42
def f060stl_f060_streak_length_ustk_21d_xstd63_jerk_v142_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * _std(closeadj, 63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xstd63 jerk_w=63
def f060stl_f060_streak_length_ustk_21d_xstd63_jerk_v143_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * _std(closeadj, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xstd63 jerk_w=126
def f060stl_f060_streak_length_ustk_21d_xstd63_jerk_v144_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * _std(closeadj, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xclosesq jerk_w=5
def f060stl_f060_streak_length_ustk_21d_xclosesq_jerk_v145_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * closeadj * closeadj / 100.0
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xclosesq jerk_w=10
def f060stl_f060_streak_length_ustk_21d_xclosesq_jerk_v146_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * closeadj * closeadj / 100.0
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xclosesq jerk_w=21
def f060stl_f060_streak_length_ustk_21d_xclosesq_jerk_v147_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * closeadj * closeadj / 100.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xclosesq jerk_w=42
def f060stl_f060_streak_length_ustk_21d_xclosesq_jerk_v148_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * closeadj * closeadj / 100.0
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xclosesq jerk_w=63
def f060stl_f060_streak_length_ustk_21d_xclosesq_jerk_v149_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * closeadj * closeadj / 100.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ustk base_w=21 variant=xclosesq jerk_w=126
def f060stl_f060_streak_length_ustk_21d_xclosesq_jerk_v150_signal(closeadj):
    base = _f060_up_streak(closeadj, 21) * closeadj * closeadj / 100.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f060stl_f060_streak_length_ustk_5d_xclose_jerk_v001_signal,
    f060stl_f060_streak_length_ustk_5d_xclose_jerk_v002_signal,
    f060stl_f060_streak_length_ustk_5d_xclose_jerk_v003_signal,
    f060stl_f060_streak_length_ustk_5d_xclose_jerk_v004_signal,
    f060stl_f060_streak_length_ustk_5d_xclose_jerk_v005_signal,
    f060stl_f060_streak_length_ustk_5d_xclose_jerk_v006_signal,
    f060stl_f060_streak_length_ustk_5d_xmean21_jerk_v007_signal,
    f060stl_f060_streak_length_ustk_5d_xmean21_jerk_v008_signal,
    f060stl_f060_streak_length_ustk_5d_xmean21_jerk_v009_signal,
    f060stl_f060_streak_length_ustk_5d_xmean21_jerk_v010_signal,
    f060stl_f060_streak_length_ustk_5d_xmean21_jerk_v011_signal,
    f060stl_f060_streak_length_ustk_5d_xmean21_jerk_v012_signal,
    f060stl_f060_streak_length_ustk_5d_xmean63_jerk_v013_signal,
    f060stl_f060_streak_length_ustk_5d_xmean63_jerk_v014_signal,
    f060stl_f060_streak_length_ustk_5d_xmean63_jerk_v015_signal,
    f060stl_f060_streak_length_ustk_5d_xmean63_jerk_v016_signal,
    f060stl_f060_streak_length_ustk_5d_xmean63_jerk_v017_signal,
    f060stl_f060_streak_length_ustk_5d_xmean63_jerk_v018_signal,
    f060stl_f060_streak_length_ustk_5d_xstd63_jerk_v019_signal,
    f060stl_f060_streak_length_ustk_5d_xstd63_jerk_v020_signal,
    f060stl_f060_streak_length_ustk_5d_xstd63_jerk_v021_signal,
    f060stl_f060_streak_length_ustk_5d_xstd63_jerk_v022_signal,
    f060stl_f060_streak_length_ustk_5d_xstd63_jerk_v023_signal,
    f060stl_f060_streak_length_ustk_5d_xstd63_jerk_v024_signal,
    f060stl_f060_streak_length_ustk_5d_xclosesq_jerk_v025_signal,
    f060stl_f060_streak_length_ustk_5d_xclosesq_jerk_v026_signal,
    f060stl_f060_streak_length_ustk_5d_xclosesq_jerk_v027_signal,
    f060stl_f060_streak_length_ustk_5d_xclosesq_jerk_v028_signal,
    f060stl_f060_streak_length_ustk_5d_xclosesq_jerk_v029_signal,
    f060stl_f060_streak_length_ustk_5d_xclosesq_jerk_v030_signal,
    f060stl_f060_streak_length_ustk_5d_xclose2_jerk_v031_signal,
    f060stl_f060_streak_length_ustk_5d_xclose2_jerk_v032_signal,
    f060stl_f060_streak_length_ustk_5d_xclose2_jerk_v033_signal,
    f060stl_f060_streak_length_ustk_5d_xclose2_jerk_v034_signal,
    f060stl_f060_streak_length_ustk_5d_xclose2_jerk_v035_signal,
    f060stl_f060_streak_length_ustk_5d_xclose2_jerk_v036_signal,
    f060stl_f060_streak_length_ustk_5d_xema21_jerk_v037_signal,
    f060stl_f060_streak_length_ustk_5d_xema21_jerk_v038_signal,
    f060stl_f060_streak_length_ustk_5d_xema21_jerk_v039_signal,
    f060stl_f060_streak_length_ustk_5d_xema21_jerk_v040_signal,
    f060stl_f060_streak_length_ustk_5d_xema21_jerk_v041_signal,
    f060stl_f060_streak_length_ustk_5d_xema21_jerk_v042_signal,
    f060stl_f060_streak_length_ustk_5d_xema63_jerk_v043_signal,
    f060stl_f060_streak_length_ustk_5d_xema63_jerk_v044_signal,
    f060stl_f060_streak_length_ustk_5d_xema63_jerk_v045_signal,
    f060stl_f060_streak_length_ustk_5d_xema63_jerk_v046_signal,
    f060stl_f060_streak_length_ustk_5d_xema63_jerk_v047_signal,
    f060stl_f060_streak_length_ustk_5d_xema63_jerk_v048_signal,
    f060stl_f060_streak_length_ustk_5d_xmix_jerk_v049_signal,
    f060stl_f060_streak_length_ustk_5d_xmix_jerk_v050_signal,
    f060stl_f060_streak_length_ustk_5d_xmix_jerk_v051_signal,
    f060stl_f060_streak_length_ustk_5d_xmix_jerk_v052_signal,
    f060stl_f060_streak_length_ustk_5d_xmix_jerk_v053_signal,
    f060stl_f060_streak_length_ustk_5d_xmix_jerk_v054_signal,
    f060stl_f060_streak_length_ustk_5d_xmix2_jerk_v055_signal,
    f060stl_f060_streak_length_ustk_5d_xmix2_jerk_v056_signal,
    f060stl_f060_streak_length_ustk_5d_xmix2_jerk_v057_signal,
    f060stl_f060_streak_length_ustk_5d_xmix2_jerk_v058_signal,
    f060stl_f060_streak_length_ustk_5d_xmix2_jerk_v059_signal,
    f060stl_f060_streak_length_ustk_5d_xmix2_jerk_v060_signal,
    f060stl_f060_streak_length_ustk_10d_xclose_jerk_v061_signal,
    f060stl_f060_streak_length_ustk_10d_xclose_jerk_v062_signal,
    f060stl_f060_streak_length_ustk_10d_xclose_jerk_v063_signal,
    f060stl_f060_streak_length_ustk_10d_xclose_jerk_v064_signal,
    f060stl_f060_streak_length_ustk_10d_xclose_jerk_v065_signal,
    f060stl_f060_streak_length_ustk_10d_xclose_jerk_v066_signal,
    f060stl_f060_streak_length_ustk_10d_xmean21_jerk_v067_signal,
    f060stl_f060_streak_length_ustk_10d_xmean21_jerk_v068_signal,
    f060stl_f060_streak_length_ustk_10d_xmean21_jerk_v069_signal,
    f060stl_f060_streak_length_ustk_10d_xmean21_jerk_v070_signal,
    f060stl_f060_streak_length_ustk_10d_xmean21_jerk_v071_signal,
    f060stl_f060_streak_length_ustk_10d_xmean21_jerk_v072_signal,
    f060stl_f060_streak_length_ustk_10d_xmean63_jerk_v073_signal,
    f060stl_f060_streak_length_ustk_10d_xmean63_jerk_v074_signal,
    f060stl_f060_streak_length_ustk_10d_xmean63_jerk_v075_signal,
    f060stl_f060_streak_length_ustk_10d_xmean63_jerk_v076_signal,
    f060stl_f060_streak_length_ustk_10d_xmean63_jerk_v077_signal,
    f060stl_f060_streak_length_ustk_10d_xmean63_jerk_v078_signal,
    f060stl_f060_streak_length_ustk_10d_xstd63_jerk_v079_signal,
    f060stl_f060_streak_length_ustk_10d_xstd63_jerk_v080_signal,
    f060stl_f060_streak_length_ustk_10d_xstd63_jerk_v081_signal,
    f060stl_f060_streak_length_ustk_10d_xstd63_jerk_v082_signal,
    f060stl_f060_streak_length_ustk_10d_xstd63_jerk_v083_signal,
    f060stl_f060_streak_length_ustk_10d_xstd63_jerk_v084_signal,
    f060stl_f060_streak_length_ustk_10d_xclosesq_jerk_v085_signal,
    f060stl_f060_streak_length_ustk_10d_xclosesq_jerk_v086_signal,
    f060stl_f060_streak_length_ustk_10d_xclosesq_jerk_v087_signal,
    f060stl_f060_streak_length_ustk_10d_xclosesq_jerk_v088_signal,
    f060stl_f060_streak_length_ustk_10d_xclosesq_jerk_v089_signal,
    f060stl_f060_streak_length_ustk_10d_xclosesq_jerk_v090_signal,
    f060stl_f060_streak_length_ustk_10d_xclose2_jerk_v091_signal,
    f060stl_f060_streak_length_ustk_10d_xclose2_jerk_v092_signal,
    f060stl_f060_streak_length_ustk_10d_xclose2_jerk_v093_signal,
    f060stl_f060_streak_length_ustk_10d_xclose2_jerk_v094_signal,
    f060stl_f060_streak_length_ustk_10d_xclose2_jerk_v095_signal,
    f060stl_f060_streak_length_ustk_10d_xclose2_jerk_v096_signal,
    f060stl_f060_streak_length_ustk_10d_xema21_jerk_v097_signal,
    f060stl_f060_streak_length_ustk_10d_xema21_jerk_v098_signal,
    f060stl_f060_streak_length_ustk_10d_xema21_jerk_v099_signal,
    f060stl_f060_streak_length_ustk_10d_xema21_jerk_v100_signal,
    f060stl_f060_streak_length_ustk_10d_xema21_jerk_v101_signal,
    f060stl_f060_streak_length_ustk_10d_xema21_jerk_v102_signal,
    f060stl_f060_streak_length_ustk_10d_xema63_jerk_v103_signal,
    f060stl_f060_streak_length_ustk_10d_xema63_jerk_v104_signal,
    f060stl_f060_streak_length_ustk_10d_xema63_jerk_v105_signal,
    f060stl_f060_streak_length_ustk_10d_xema63_jerk_v106_signal,
    f060stl_f060_streak_length_ustk_10d_xema63_jerk_v107_signal,
    f060stl_f060_streak_length_ustk_10d_xema63_jerk_v108_signal,
    f060stl_f060_streak_length_ustk_10d_xmix_jerk_v109_signal,
    f060stl_f060_streak_length_ustk_10d_xmix_jerk_v110_signal,
    f060stl_f060_streak_length_ustk_10d_xmix_jerk_v111_signal,
    f060stl_f060_streak_length_ustk_10d_xmix_jerk_v112_signal,
    f060stl_f060_streak_length_ustk_10d_xmix_jerk_v113_signal,
    f060stl_f060_streak_length_ustk_10d_xmix_jerk_v114_signal,
    f060stl_f060_streak_length_ustk_10d_xmix2_jerk_v115_signal,
    f060stl_f060_streak_length_ustk_10d_xmix2_jerk_v116_signal,
    f060stl_f060_streak_length_ustk_10d_xmix2_jerk_v117_signal,
    f060stl_f060_streak_length_ustk_10d_xmix2_jerk_v118_signal,
    f060stl_f060_streak_length_ustk_10d_xmix2_jerk_v119_signal,
    f060stl_f060_streak_length_ustk_10d_xmix2_jerk_v120_signal,
    f060stl_f060_streak_length_ustk_21d_xclose_jerk_v121_signal,
    f060stl_f060_streak_length_ustk_21d_xclose_jerk_v122_signal,
    f060stl_f060_streak_length_ustk_21d_xclose_jerk_v123_signal,
    f060stl_f060_streak_length_ustk_21d_xclose_jerk_v124_signal,
    f060stl_f060_streak_length_ustk_21d_xclose_jerk_v125_signal,
    f060stl_f060_streak_length_ustk_21d_xclose_jerk_v126_signal,
    f060stl_f060_streak_length_ustk_21d_xmean21_jerk_v127_signal,
    f060stl_f060_streak_length_ustk_21d_xmean21_jerk_v128_signal,
    f060stl_f060_streak_length_ustk_21d_xmean21_jerk_v129_signal,
    f060stl_f060_streak_length_ustk_21d_xmean21_jerk_v130_signal,
    f060stl_f060_streak_length_ustk_21d_xmean21_jerk_v131_signal,
    f060stl_f060_streak_length_ustk_21d_xmean21_jerk_v132_signal,
    f060stl_f060_streak_length_ustk_21d_xmean63_jerk_v133_signal,
    f060stl_f060_streak_length_ustk_21d_xmean63_jerk_v134_signal,
    f060stl_f060_streak_length_ustk_21d_xmean63_jerk_v135_signal,
    f060stl_f060_streak_length_ustk_21d_xmean63_jerk_v136_signal,
    f060stl_f060_streak_length_ustk_21d_xmean63_jerk_v137_signal,
    f060stl_f060_streak_length_ustk_21d_xmean63_jerk_v138_signal,
    f060stl_f060_streak_length_ustk_21d_xstd63_jerk_v139_signal,
    f060stl_f060_streak_length_ustk_21d_xstd63_jerk_v140_signal,
    f060stl_f060_streak_length_ustk_21d_xstd63_jerk_v141_signal,
    f060stl_f060_streak_length_ustk_21d_xstd63_jerk_v142_signal,
    f060stl_f060_streak_length_ustk_21d_xstd63_jerk_v143_signal,
    f060stl_f060_streak_length_ustk_21d_xstd63_jerk_v144_signal,
    f060stl_f060_streak_length_ustk_21d_xclosesq_jerk_v145_signal,
    f060stl_f060_streak_length_ustk_21d_xclosesq_jerk_v146_signal,
    f060stl_f060_streak_length_ustk_21d_xclosesq_jerk_v147_signal,
    f060stl_f060_streak_length_ustk_21d_xclosesq_jerk_v148_signal,
    f060stl_f060_streak_length_ustk_21d_xclosesq_jerk_v149_signal,
    f060stl_f060_streak_length_ustk_21d_xclosesq_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F060_STREAK_LENGTH_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f060_up_streak", "_f060_streak_length", "_f060_streak_intensity",)
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
    print(f"OK f060_streak_length_3rd_derivatives_001_150_claude: {n_features} features pass")
