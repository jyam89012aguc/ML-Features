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
def _f49_self_baseline(closeadj, w):
    return closeadj.rolling(w, min_periods=max(1, w // 2)).mean()


def _f49_excess_momentum(closeadj, w):
    base = closeadj.rolling(w, min_periods=max(1, w // 2)).mean()
    return closeadj / base.replace(0, np.nan) - 1.0


def _f49_momentum_persistence(closeadj, volume, w):
    r = closeadj.pct_change()
    sign = r.rolling(w, min_periods=max(1, w // 2)).apply(lambda x: (x > 0).mean(), raw=True)
    vol = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    return sign * vol


def fsr_f49_financial_sector_relative_sb_close_raw_5d_jw5_jerk_v001_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 5)) * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_raw_5d_jw21_jerk_v002_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 5)) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_raw_5d_jw63_jerk_v003_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 5)) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_raw_10d_jw5_jerk_v004_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 10)) * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_raw_10d_jw21_jerk_v005_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 10)) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_raw_10d_jw63_jerk_v006_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 10)) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_raw_21d_jw5_jerk_v007_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 21)) * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_raw_21d_jw21_jerk_v008_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 21)) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_raw_21d_jw63_jerk_v009_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 21)) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_raw_42d_jw5_jerk_v010_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 42)) * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_raw_42d_jw21_jerk_v011_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 42)) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_raw_42d_jw63_jerk_v012_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 42)) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_raw_63d_jw5_jerk_v013_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 63)) * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_raw_63d_jw21_jerk_v014_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 63)) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_raw_63d_jw63_jerk_v015_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 63)) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_raw_126d_jw5_jerk_v016_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 126)) * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_raw_126d_jw21_jerk_v017_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 126)) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_raw_126d_jw63_jerk_v018_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 126)) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_raw_189d_jw5_jerk_v019_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 189)) * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_raw_189d_jw21_jerk_v020_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 189)) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_raw_189d_jw63_jerk_v021_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 189)) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_raw_252d_jw5_jerk_v022_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 252)) * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_raw_252d_jw21_jerk_v023_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 252)) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_raw_252d_jw63_jerk_v024_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 252)) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_raw_378d_jw5_jerk_v025_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 378)) * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_raw_378d_jw21_jerk_v026_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 378)) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_raw_378d_jw63_jerk_v027_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 378)) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_raw_504d_jw5_jerk_v028_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 504)) * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_raw_504d_jw21_jerk_v029_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 504)) * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_raw_504d_jw63_jerk_v030_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 504)) * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_sq_raw_5d_jw5_jerk_v031_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 5)) * closeadj * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_sq_raw_5d_jw21_jerk_v032_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 5)) * closeadj * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_sq_raw_5d_jw63_jerk_v033_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 5)) * closeadj * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_sq_raw_10d_jw5_jerk_v034_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 10)) * closeadj * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_sq_raw_10d_jw21_jerk_v035_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 10)) * closeadj * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_sq_raw_10d_jw63_jerk_v036_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 10)) * closeadj * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_sq_raw_21d_jw5_jerk_v037_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 21)) * closeadj * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_sq_raw_21d_jw21_jerk_v038_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 21)) * closeadj * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_sq_raw_21d_jw63_jerk_v039_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 21)) * closeadj * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_sq_raw_42d_jw5_jerk_v040_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 42)) * closeadj * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_sq_raw_42d_jw21_jerk_v041_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 42)) * closeadj * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_sq_raw_42d_jw63_jerk_v042_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 42)) * closeadj * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_sq_raw_63d_jw5_jerk_v043_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 63)) * closeadj * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_sq_raw_63d_jw21_jerk_v044_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 63)) * closeadj * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_sq_raw_63d_jw63_jerk_v045_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 63)) * closeadj * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_sq_raw_126d_jw5_jerk_v046_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 126)) * closeadj * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_sq_raw_126d_jw21_jerk_v047_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 126)) * closeadj * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_sq_raw_126d_jw63_jerk_v048_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 126)) * closeadj * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_sq_raw_189d_jw5_jerk_v049_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 189)) * closeadj * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_sq_raw_189d_jw21_jerk_v050_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 189)) * closeadj * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_sq_raw_189d_jw63_jerk_v051_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 189)) * closeadj * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_sq_raw_252d_jw5_jerk_v052_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 252)) * closeadj * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_sq_raw_252d_jw21_jerk_v053_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 252)) * closeadj * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_sq_raw_252d_jw63_jerk_v054_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 252)) * closeadj * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_sq_raw_378d_jw5_jerk_v055_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 378)) * closeadj * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_sq_raw_378d_jw21_jerk_v056_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 378)) * closeadj * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_sq_raw_378d_jw63_jerk_v057_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 378)) * closeadj * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_sq_raw_504d_jw5_jerk_v058_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 504)) * closeadj * closeadj
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_sq_raw_504d_jw21_jerk_v059_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 504)) * closeadj * closeadj
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_sq_raw_504d_jw63_jerk_v060_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 504)) * closeadj * closeadj
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_log_raw_5d_jw5_jerk_v061_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 5)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_log_raw_5d_jw21_jerk_v062_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 5)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_log_raw_5d_jw63_jerk_v063_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 5)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_log_raw_10d_jw5_jerk_v064_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 10)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_log_raw_10d_jw21_jerk_v065_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 10)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_log_raw_10d_jw63_jerk_v066_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 10)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_log_raw_21d_jw5_jerk_v067_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 21)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_log_raw_21d_jw21_jerk_v068_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 21)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_log_raw_21d_jw63_jerk_v069_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 21)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_log_raw_42d_jw5_jerk_v070_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 42)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_log_raw_42d_jw21_jerk_v071_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 42)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_log_raw_42d_jw63_jerk_v072_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 42)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_log_raw_63d_jw5_jerk_v073_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 63)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_log_raw_63d_jw21_jerk_v074_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 63)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_log_raw_63d_jw63_jerk_v075_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 63)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_log_raw_126d_jw5_jerk_v076_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 126)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_log_raw_126d_jw21_jerk_v077_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 126)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_log_raw_126d_jw63_jerk_v078_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 126)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_log_raw_189d_jw5_jerk_v079_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 189)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_log_raw_189d_jw21_jerk_v080_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 189)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_log_raw_189d_jw63_jerk_v081_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 189)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_log_raw_252d_jw5_jerk_v082_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 252)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_log_raw_252d_jw21_jerk_v083_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 252)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_log_raw_252d_jw63_jerk_v084_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 252)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_log_raw_378d_jw5_jerk_v085_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 378)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_log_raw_378d_jw21_jerk_v086_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 378)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_log_raw_378d_jw63_jerk_v087_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 378)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_log_raw_504d_jw5_jerk_v088_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 504)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_log_raw_504d_jw21_jerk_v089_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 504)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_log_raw_504d_jw63_jerk_v090_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 504)) * np.log(closeadj.abs() + 1.0)
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_mean21_raw_5d_jw5_jerk_v091_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 5)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_mean21_raw_5d_jw21_jerk_v092_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 5)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_mean21_raw_5d_jw63_jerk_v093_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 5)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_mean21_raw_10d_jw5_jerk_v094_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 10)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_mean21_raw_10d_jw21_jerk_v095_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 10)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_mean21_raw_10d_jw63_jerk_v096_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 10)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_mean21_raw_21d_jw5_jerk_v097_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 21)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_mean21_raw_21d_jw21_jerk_v098_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 21)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_mean21_raw_21d_jw63_jerk_v099_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 21)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_mean21_raw_42d_jw5_jerk_v100_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 42)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_mean21_raw_42d_jw21_jerk_v101_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 42)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_mean21_raw_42d_jw63_jerk_v102_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 42)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_mean21_raw_63d_jw5_jerk_v103_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 63)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_mean21_raw_63d_jw21_jerk_v104_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 63)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_mean21_raw_63d_jw63_jerk_v105_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 63)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_mean21_raw_126d_jw5_jerk_v106_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 126)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_mean21_raw_126d_jw21_jerk_v107_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 126)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_mean21_raw_126d_jw63_jerk_v108_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 126)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_mean21_raw_189d_jw5_jerk_v109_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 189)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_mean21_raw_189d_jw21_jerk_v110_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 189)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_mean21_raw_189d_jw63_jerk_v111_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 189)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_mean21_raw_252d_jw5_jerk_v112_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 252)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_mean21_raw_252d_jw21_jerk_v113_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 252)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_mean21_raw_252d_jw63_jerk_v114_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 252)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_mean21_raw_378d_jw5_jerk_v115_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 378)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_mean21_raw_378d_jw21_jerk_v116_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 378)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_mean21_raw_378d_jw63_jerk_v117_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 378)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_mean21_raw_504d_jw5_jerk_v118_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 504)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_mean21_raw_504d_jw21_jerk_v119_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 504)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_mean21_raw_504d_jw63_jerk_v120_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 504)) * closeadj.rolling(21, min_periods=10).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_mean63_raw_5d_jw5_jerk_v121_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 5)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_mean63_raw_5d_jw21_jerk_v122_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 5)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_mean63_raw_5d_jw63_jerk_v123_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 5)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_mean63_raw_10d_jw5_jerk_v124_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 10)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_mean63_raw_10d_jw21_jerk_v125_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 10)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_mean63_raw_10d_jw63_jerk_v126_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 10)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_mean63_raw_21d_jw5_jerk_v127_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 21)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_mean63_raw_21d_jw21_jerk_v128_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 21)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_mean63_raw_21d_jw63_jerk_v129_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 21)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_mean63_raw_42d_jw5_jerk_v130_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 42)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_mean63_raw_42d_jw21_jerk_v131_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 42)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_mean63_raw_42d_jw63_jerk_v132_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 42)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_mean63_raw_63d_jw5_jerk_v133_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 63)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_mean63_raw_63d_jw21_jerk_v134_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 63)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_mean63_raw_63d_jw63_jerk_v135_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 63)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_mean63_raw_126d_jw5_jerk_v136_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 126)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_mean63_raw_126d_jw21_jerk_v137_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 126)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_mean63_raw_126d_jw63_jerk_v138_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 126)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_mean63_raw_189d_jw5_jerk_v139_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 189)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_mean63_raw_189d_jw21_jerk_v140_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 189)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_mean63_raw_189d_jw63_jerk_v141_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 189)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_mean63_raw_252d_jw5_jerk_v142_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 252)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_mean63_raw_252d_jw21_jerk_v143_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 252)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_mean63_raw_252d_jw63_jerk_v144_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 252)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_mean63_raw_378d_jw5_jerk_v145_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 378)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_mean63_raw_378d_jw21_jerk_v146_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 378)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_mean63_raw_378d_jw63_jerk_v147_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 378)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_sb_close_mean63_raw_504d_jw5_jerk_v148_signal(closeadj):
    _b = (_f49_self_baseline(closeadj, 504)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_em_close_mean63_raw_504d_jw21_jerk_v149_signal(closeadj):
    _b = (_f49_excess_momentum(closeadj, 504)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def fsr_f49_financial_sector_relative_mp_close_mean63_raw_504d_jw63_jerk_v150_signal(closeadj, volume):
    _b = (_f49_momentum_persistence(closeadj, volume, 504)) * closeadj.rolling(63, min_periods=21).mean()
    result = _jerk(_b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    fsr_f49_financial_sector_relative_sb_close_raw_5d_jw5_jerk_v001_signal,
    fsr_f49_financial_sector_relative_em_close_raw_5d_jw21_jerk_v002_signal,
    fsr_f49_financial_sector_relative_mp_close_raw_5d_jw63_jerk_v003_signal,
    fsr_f49_financial_sector_relative_sb_close_raw_10d_jw5_jerk_v004_signal,
    fsr_f49_financial_sector_relative_em_close_raw_10d_jw21_jerk_v005_signal,
    fsr_f49_financial_sector_relative_mp_close_raw_10d_jw63_jerk_v006_signal,
    fsr_f49_financial_sector_relative_sb_close_raw_21d_jw5_jerk_v007_signal,
    fsr_f49_financial_sector_relative_em_close_raw_21d_jw21_jerk_v008_signal,
    fsr_f49_financial_sector_relative_mp_close_raw_21d_jw63_jerk_v009_signal,
    fsr_f49_financial_sector_relative_sb_close_raw_42d_jw5_jerk_v010_signal,
    fsr_f49_financial_sector_relative_em_close_raw_42d_jw21_jerk_v011_signal,
    fsr_f49_financial_sector_relative_mp_close_raw_42d_jw63_jerk_v012_signal,
    fsr_f49_financial_sector_relative_sb_close_raw_63d_jw5_jerk_v013_signal,
    fsr_f49_financial_sector_relative_em_close_raw_63d_jw21_jerk_v014_signal,
    fsr_f49_financial_sector_relative_mp_close_raw_63d_jw63_jerk_v015_signal,
    fsr_f49_financial_sector_relative_sb_close_raw_126d_jw5_jerk_v016_signal,
    fsr_f49_financial_sector_relative_em_close_raw_126d_jw21_jerk_v017_signal,
    fsr_f49_financial_sector_relative_mp_close_raw_126d_jw63_jerk_v018_signal,
    fsr_f49_financial_sector_relative_sb_close_raw_189d_jw5_jerk_v019_signal,
    fsr_f49_financial_sector_relative_em_close_raw_189d_jw21_jerk_v020_signal,
    fsr_f49_financial_sector_relative_mp_close_raw_189d_jw63_jerk_v021_signal,
    fsr_f49_financial_sector_relative_sb_close_raw_252d_jw5_jerk_v022_signal,
    fsr_f49_financial_sector_relative_em_close_raw_252d_jw21_jerk_v023_signal,
    fsr_f49_financial_sector_relative_mp_close_raw_252d_jw63_jerk_v024_signal,
    fsr_f49_financial_sector_relative_sb_close_raw_378d_jw5_jerk_v025_signal,
    fsr_f49_financial_sector_relative_em_close_raw_378d_jw21_jerk_v026_signal,
    fsr_f49_financial_sector_relative_mp_close_raw_378d_jw63_jerk_v027_signal,
    fsr_f49_financial_sector_relative_sb_close_raw_504d_jw5_jerk_v028_signal,
    fsr_f49_financial_sector_relative_em_close_raw_504d_jw21_jerk_v029_signal,
    fsr_f49_financial_sector_relative_mp_close_raw_504d_jw63_jerk_v030_signal,
    fsr_f49_financial_sector_relative_sb_close_sq_raw_5d_jw5_jerk_v031_signal,
    fsr_f49_financial_sector_relative_em_close_sq_raw_5d_jw21_jerk_v032_signal,
    fsr_f49_financial_sector_relative_mp_close_sq_raw_5d_jw63_jerk_v033_signal,
    fsr_f49_financial_sector_relative_sb_close_sq_raw_10d_jw5_jerk_v034_signal,
    fsr_f49_financial_sector_relative_em_close_sq_raw_10d_jw21_jerk_v035_signal,
    fsr_f49_financial_sector_relative_mp_close_sq_raw_10d_jw63_jerk_v036_signal,
    fsr_f49_financial_sector_relative_sb_close_sq_raw_21d_jw5_jerk_v037_signal,
    fsr_f49_financial_sector_relative_em_close_sq_raw_21d_jw21_jerk_v038_signal,
    fsr_f49_financial_sector_relative_mp_close_sq_raw_21d_jw63_jerk_v039_signal,
    fsr_f49_financial_sector_relative_sb_close_sq_raw_42d_jw5_jerk_v040_signal,
    fsr_f49_financial_sector_relative_em_close_sq_raw_42d_jw21_jerk_v041_signal,
    fsr_f49_financial_sector_relative_mp_close_sq_raw_42d_jw63_jerk_v042_signal,
    fsr_f49_financial_sector_relative_sb_close_sq_raw_63d_jw5_jerk_v043_signal,
    fsr_f49_financial_sector_relative_em_close_sq_raw_63d_jw21_jerk_v044_signal,
    fsr_f49_financial_sector_relative_mp_close_sq_raw_63d_jw63_jerk_v045_signal,
    fsr_f49_financial_sector_relative_sb_close_sq_raw_126d_jw5_jerk_v046_signal,
    fsr_f49_financial_sector_relative_em_close_sq_raw_126d_jw21_jerk_v047_signal,
    fsr_f49_financial_sector_relative_mp_close_sq_raw_126d_jw63_jerk_v048_signal,
    fsr_f49_financial_sector_relative_sb_close_sq_raw_189d_jw5_jerk_v049_signal,
    fsr_f49_financial_sector_relative_em_close_sq_raw_189d_jw21_jerk_v050_signal,
    fsr_f49_financial_sector_relative_mp_close_sq_raw_189d_jw63_jerk_v051_signal,
    fsr_f49_financial_sector_relative_sb_close_sq_raw_252d_jw5_jerk_v052_signal,
    fsr_f49_financial_sector_relative_em_close_sq_raw_252d_jw21_jerk_v053_signal,
    fsr_f49_financial_sector_relative_mp_close_sq_raw_252d_jw63_jerk_v054_signal,
    fsr_f49_financial_sector_relative_sb_close_sq_raw_378d_jw5_jerk_v055_signal,
    fsr_f49_financial_sector_relative_em_close_sq_raw_378d_jw21_jerk_v056_signal,
    fsr_f49_financial_sector_relative_mp_close_sq_raw_378d_jw63_jerk_v057_signal,
    fsr_f49_financial_sector_relative_sb_close_sq_raw_504d_jw5_jerk_v058_signal,
    fsr_f49_financial_sector_relative_em_close_sq_raw_504d_jw21_jerk_v059_signal,
    fsr_f49_financial_sector_relative_mp_close_sq_raw_504d_jw63_jerk_v060_signal,
    fsr_f49_financial_sector_relative_sb_close_log_raw_5d_jw5_jerk_v061_signal,
    fsr_f49_financial_sector_relative_em_close_log_raw_5d_jw21_jerk_v062_signal,
    fsr_f49_financial_sector_relative_mp_close_log_raw_5d_jw63_jerk_v063_signal,
    fsr_f49_financial_sector_relative_sb_close_log_raw_10d_jw5_jerk_v064_signal,
    fsr_f49_financial_sector_relative_em_close_log_raw_10d_jw21_jerk_v065_signal,
    fsr_f49_financial_sector_relative_mp_close_log_raw_10d_jw63_jerk_v066_signal,
    fsr_f49_financial_sector_relative_sb_close_log_raw_21d_jw5_jerk_v067_signal,
    fsr_f49_financial_sector_relative_em_close_log_raw_21d_jw21_jerk_v068_signal,
    fsr_f49_financial_sector_relative_mp_close_log_raw_21d_jw63_jerk_v069_signal,
    fsr_f49_financial_sector_relative_sb_close_log_raw_42d_jw5_jerk_v070_signal,
    fsr_f49_financial_sector_relative_em_close_log_raw_42d_jw21_jerk_v071_signal,
    fsr_f49_financial_sector_relative_mp_close_log_raw_42d_jw63_jerk_v072_signal,
    fsr_f49_financial_sector_relative_sb_close_log_raw_63d_jw5_jerk_v073_signal,
    fsr_f49_financial_sector_relative_em_close_log_raw_63d_jw21_jerk_v074_signal,
    fsr_f49_financial_sector_relative_mp_close_log_raw_63d_jw63_jerk_v075_signal,
    fsr_f49_financial_sector_relative_sb_close_log_raw_126d_jw5_jerk_v076_signal,
    fsr_f49_financial_sector_relative_em_close_log_raw_126d_jw21_jerk_v077_signal,
    fsr_f49_financial_sector_relative_mp_close_log_raw_126d_jw63_jerk_v078_signal,
    fsr_f49_financial_sector_relative_sb_close_log_raw_189d_jw5_jerk_v079_signal,
    fsr_f49_financial_sector_relative_em_close_log_raw_189d_jw21_jerk_v080_signal,
    fsr_f49_financial_sector_relative_mp_close_log_raw_189d_jw63_jerk_v081_signal,
    fsr_f49_financial_sector_relative_sb_close_log_raw_252d_jw5_jerk_v082_signal,
    fsr_f49_financial_sector_relative_em_close_log_raw_252d_jw21_jerk_v083_signal,
    fsr_f49_financial_sector_relative_mp_close_log_raw_252d_jw63_jerk_v084_signal,
    fsr_f49_financial_sector_relative_sb_close_log_raw_378d_jw5_jerk_v085_signal,
    fsr_f49_financial_sector_relative_em_close_log_raw_378d_jw21_jerk_v086_signal,
    fsr_f49_financial_sector_relative_mp_close_log_raw_378d_jw63_jerk_v087_signal,
    fsr_f49_financial_sector_relative_sb_close_log_raw_504d_jw5_jerk_v088_signal,
    fsr_f49_financial_sector_relative_em_close_log_raw_504d_jw21_jerk_v089_signal,
    fsr_f49_financial_sector_relative_mp_close_log_raw_504d_jw63_jerk_v090_signal,
    fsr_f49_financial_sector_relative_sb_close_mean21_raw_5d_jw5_jerk_v091_signal,
    fsr_f49_financial_sector_relative_em_close_mean21_raw_5d_jw21_jerk_v092_signal,
    fsr_f49_financial_sector_relative_mp_close_mean21_raw_5d_jw63_jerk_v093_signal,
    fsr_f49_financial_sector_relative_sb_close_mean21_raw_10d_jw5_jerk_v094_signal,
    fsr_f49_financial_sector_relative_em_close_mean21_raw_10d_jw21_jerk_v095_signal,
    fsr_f49_financial_sector_relative_mp_close_mean21_raw_10d_jw63_jerk_v096_signal,
    fsr_f49_financial_sector_relative_sb_close_mean21_raw_21d_jw5_jerk_v097_signal,
    fsr_f49_financial_sector_relative_em_close_mean21_raw_21d_jw21_jerk_v098_signal,
    fsr_f49_financial_sector_relative_mp_close_mean21_raw_21d_jw63_jerk_v099_signal,
    fsr_f49_financial_sector_relative_sb_close_mean21_raw_42d_jw5_jerk_v100_signal,
    fsr_f49_financial_sector_relative_em_close_mean21_raw_42d_jw21_jerk_v101_signal,
    fsr_f49_financial_sector_relative_mp_close_mean21_raw_42d_jw63_jerk_v102_signal,
    fsr_f49_financial_sector_relative_sb_close_mean21_raw_63d_jw5_jerk_v103_signal,
    fsr_f49_financial_sector_relative_em_close_mean21_raw_63d_jw21_jerk_v104_signal,
    fsr_f49_financial_sector_relative_mp_close_mean21_raw_63d_jw63_jerk_v105_signal,
    fsr_f49_financial_sector_relative_sb_close_mean21_raw_126d_jw5_jerk_v106_signal,
    fsr_f49_financial_sector_relative_em_close_mean21_raw_126d_jw21_jerk_v107_signal,
    fsr_f49_financial_sector_relative_mp_close_mean21_raw_126d_jw63_jerk_v108_signal,
    fsr_f49_financial_sector_relative_sb_close_mean21_raw_189d_jw5_jerk_v109_signal,
    fsr_f49_financial_sector_relative_em_close_mean21_raw_189d_jw21_jerk_v110_signal,
    fsr_f49_financial_sector_relative_mp_close_mean21_raw_189d_jw63_jerk_v111_signal,
    fsr_f49_financial_sector_relative_sb_close_mean21_raw_252d_jw5_jerk_v112_signal,
    fsr_f49_financial_sector_relative_em_close_mean21_raw_252d_jw21_jerk_v113_signal,
    fsr_f49_financial_sector_relative_mp_close_mean21_raw_252d_jw63_jerk_v114_signal,
    fsr_f49_financial_sector_relative_sb_close_mean21_raw_378d_jw5_jerk_v115_signal,
    fsr_f49_financial_sector_relative_em_close_mean21_raw_378d_jw21_jerk_v116_signal,
    fsr_f49_financial_sector_relative_mp_close_mean21_raw_378d_jw63_jerk_v117_signal,
    fsr_f49_financial_sector_relative_sb_close_mean21_raw_504d_jw5_jerk_v118_signal,
    fsr_f49_financial_sector_relative_em_close_mean21_raw_504d_jw21_jerk_v119_signal,
    fsr_f49_financial_sector_relative_mp_close_mean21_raw_504d_jw63_jerk_v120_signal,
    fsr_f49_financial_sector_relative_sb_close_mean63_raw_5d_jw5_jerk_v121_signal,
    fsr_f49_financial_sector_relative_em_close_mean63_raw_5d_jw21_jerk_v122_signal,
    fsr_f49_financial_sector_relative_mp_close_mean63_raw_5d_jw63_jerk_v123_signal,
    fsr_f49_financial_sector_relative_sb_close_mean63_raw_10d_jw5_jerk_v124_signal,
    fsr_f49_financial_sector_relative_em_close_mean63_raw_10d_jw21_jerk_v125_signal,
    fsr_f49_financial_sector_relative_mp_close_mean63_raw_10d_jw63_jerk_v126_signal,
    fsr_f49_financial_sector_relative_sb_close_mean63_raw_21d_jw5_jerk_v127_signal,
    fsr_f49_financial_sector_relative_em_close_mean63_raw_21d_jw21_jerk_v128_signal,
    fsr_f49_financial_sector_relative_mp_close_mean63_raw_21d_jw63_jerk_v129_signal,
    fsr_f49_financial_sector_relative_sb_close_mean63_raw_42d_jw5_jerk_v130_signal,
    fsr_f49_financial_sector_relative_em_close_mean63_raw_42d_jw21_jerk_v131_signal,
    fsr_f49_financial_sector_relative_mp_close_mean63_raw_42d_jw63_jerk_v132_signal,
    fsr_f49_financial_sector_relative_sb_close_mean63_raw_63d_jw5_jerk_v133_signal,
    fsr_f49_financial_sector_relative_em_close_mean63_raw_63d_jw21_jerk_v134_signal,
    fsr_f49_financial_sector_relative_mp_close_mean63_raw_63d_jw63_jerk_v135_signal,
    fsr_f49_financial_sector_relative_sb_close_mean63_raw_126d_jw5_jerk_v136_signal,
    fsr_f49_financial_sector_relative_em_close_mean63_raw_126d_jw21_jerk_v137_signal,
    fsr_f49_financial_sector_relative_mp_close_mean63_raw_126d_jw63_jerk_v138_signal,
    fsr_f49_financial_sector_relative_sb_close_mean63_raw_189d_jw5_jerk_v139_signal,
    fsr_f49_financial_sector_relative_em_close_mean63_raw_189d_jw21_jerk_v140_signal,
    fsr_f49_financial_sector_relative_mp_close_mean63_raw_189d_jw63_jerk_v141_signal,
    fsr_f49_financial_sector_relative_sb_close_mean63_raw_252d_jw5_jerk_v142_signal,
    fsr_f49_financial_sector_relative_em_close_mean63_raw_252d_jw21_jerk_v143_signal,
    fsr_f49_financial_sector_relative_mp_close_mean63_raw_252d_jw63_jerk_v144_signal,
    fsr_f49_financial_sector_relative_sb_close_mean63_raw_378d_jw5_jerk_v145_signal,
    fsr_f49_financial_sector_relative_em_close_mean63_raw_378d_jw21_jerk_v146_signal,
    fsr_f49_financial_sector_relative_mp_close_mean63_raw_378d_jw63_jerk_v147_signal,
    fsr_f49_financial_sector_relative_sb_close_mean63_raw_504d_jw5_jerk_v148_signal,
    fsr_f49_financial_sector_relative_em_close_mean63_raw_504d_jw21_jerk_v149_signal,
    fsr_f49_financial_sector_relative_mp_close_mean63_raw_504d_jw63_jerk_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F49_FINANCIAL_SECTOR_RELATIVE_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f49_self_baseline', '_f49_excess_momentum', '_f49_momentum_persistence')
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
    print(f"OK f49_financial_sector_relative_3rd_derivatives_001_150_claude: {n_features} features pass")
