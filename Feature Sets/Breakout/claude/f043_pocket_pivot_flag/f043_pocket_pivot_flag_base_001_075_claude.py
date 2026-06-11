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
def _f043_up_day_vol(closeadj, volume, w):
    r = closeadj.pct_change()
    up = volume.where(r > 0, 0.0)
    return up.rolling(w, min_periods=max(1, w // 2)).sum()


def _f043_max_down_vol(closeadj, volume, w):
    r = closeadj.pct_change()
    down = volume.where(r < 0, 0.0)
    return down.rolling(w, min_periods=max(1, w // 2)).max()


def _f043_pocket_pivot(closeadj, volume, w):
    r = closeadj.pct_change()
    up_today = volume.where(r > 0, 0.0)
    max_down_10 = volume.where(r < 0, 0.0).rolling(w, min_periods=max(1, w // 2)).max()
    return (up_today - max_down_10) * closeadj


def f043ppf_f043_pocket_pivot_flag_upvol10x_raw_base_v001_signal(closeadj, volume):
    result = _f043_up_day_vol(closeadj, volume, 10) * closeadj / 1e6
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol10x_ema5_base_v002_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 10) * closeadj / 1e6).ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol10x_ema21_base_v003_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 10) * closeadj / 1e6).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol21x_raw_base_v004_signal(closeadj, volume):
    result = _f043_up_day_vol(closeadj, volume, 21) * closeadj / 1e6
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol21x_ema5_base_v005_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 21) * closeadj / 1e6).ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol21x_ema21_base_v006_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 21) * closeadj / 1e6).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol63x_raw_base_v007_signal(closeadj, volume):
    result = _f043_up_day_vol(closeadj, volume, 63) * closeadj / 1e6
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol63x_ema5_base_v008_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 63) * closeadj / 1e6).ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol63x_ema21_base_v009_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 63) * closeadj / 1e6).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol126x_raw_base_v010_signal(closeadj, volume):
    result = _f043_up_day_vol(closeadj, volume, 126) * closeadj / 1e6
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol126x_ema5_base_v011_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 126) * closeadj / 1e6).ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol126x_ema21_base_v012_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 126) * closeadj / 1e6).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol252x_raw_base_v013_signal(closeadj, volume):
    result = _z(_f043_up_day_vol(closeadj, volume, 252), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol252x_ema5_base_v014_signal(closeadj, volume):
    result = (_z(_f043_up_day_vol(closeadj, volume, 252), 252) * _safe_div(closeadj, _mean(closeadj, 252))).ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_upvol252x_ema21_base_v015_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 252) * closeadj / 1e6).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol10x_raw_base_v016_signal(closeadj, volume):
    result = _f043_max_down_vol(closeadj, volume, 10) * closeadj / 1e6
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol10x_ema5_base_v017_signal(closeadj, volume):
    result = (_f043_max_down_vol(closeadj, volume, 10) * closeadj / 1e6).ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol10x_ema21_base_v018_signal(closeadj, volume):
    result = (_f043_max_down_vol(closeadj, volume, 10) * closeadj / 1e6).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol21x_raw_base_v019_signal(closeadj, volume):
    result = _f043_max_down_vol(closeadj, volume, 21) * closeadj / 1e6
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol21x_ema5_base_v020_signal(closeadj, volume):
    result = (_f043_max_down_vol(closeadj, volume, 21) * closeadj / 1e6).ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol21x_ema21_base_v021_signal(closeadj, volume):
    result = (_f043_max_down_vol(closeadj, volume, 21) * closeadj / 1e6).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol63x_raw_base_v022_signal(closeadj, volume):
    result = _f043_max_down_vol(closeadj, volume, 63) * closeadj / 1e6
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol63x_ema5_base_v023_signal(closeadj, volume):
    result = (_f043_max_down_vol(closeadj, volume, 63) * closeadj / 1e6).ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol63x_ema21_base_v024_signal(closeadj, volume):
    result = (_f043_max_down_vol(closeadj, volume, 63) * closeadj / 1e6).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol126x_raw_base_v025_signal(closeadj, volume):
    result = _f043_max_down_vol(closeadj, volume, 126) * closeadj / 1e6
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol126x_ema5_base_v026_signal(closeadj, volume):
    result = (_f043_max_down_vol(closeadj, volume, 126) * closeadj / 1e6).ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol126x_ema21_base_v027_signal(closeadj, volume):
    result = (_f043_max_down_vol(closeadj, volume, 126) * closeadj / 1e6).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol252x_raw_base_v028_signal(closeadj, volume):
    result = _z(_f043_max_down_vol(closeadj, volume, 252), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol252x_ema5_base_v029_signal(closeadj, volume):
    result = (_z(_f043_max_down_vol(closeadj, volume, 252), 252) * _safe_div(closeadj, _mean(closeadj, 252))).ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_maxdvol252x_ema21_base_v030_signal(closeadj, volume):
    result = (_f043_max_down_vol(closeadj, volume, 252) * closeadj / 1e6).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp10_raw_base_v031_signal(closeadj, volume):
    result = _f043_pocket_pivot(closeadj, volume, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp10_ema5_base_v032_signal(closeadj, volume):
    result = (_f043_pocket_pivot(closeadj, volume, 10)).ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp10_ema21_base_v033_signal(closeadj, volume):
    result = (_f043_pocket_pivot(closeadj, volume, 10)).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp21_raw_base_v034_signal(closeadj, volume):
    result = _f043_pocket_pivot(closeadj, volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp21_ema5_base_v035_signal(closeadj, volume):
    result = (_f043_pocket_pivot(closeadj, volume, 21)).ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp21_ema21_base_v036_signal(closeadj, volume):
    result = (_f043_pocket_pivot(closeadj, volume, 21)).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp63_raw_base_v037_signal(closeadj, volume):
    result = _f043_pocket_pivot(closeadj, volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp63_ema5_base_v038_signal(closeadj, volume):
    result = (_f043_pocket_pivot(closeadj, volume, 63)).ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp63_ema21_base_v039_signal(closeadj, volume):
    result = (_f043_pocket_pivot(closeadj, volume, 63)).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp126_raw_base_v040_signal(closeadj, volume):
    result = _f043_pocket_pivot(closeadj, volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp126_ema5_base_v041_signal(closeadj, volume):
    result = (_f043_pocket_pivot(closeadj, volume, 126)).ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp126_ema21_base_v042_signal(closeadj, volume):
    result = (_f043_pocket_pivot(closeadj, volume, 126)).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp252_raw_base_v043_signal(closeadj, volume):
    result = _f043_pocket_pivot(closeadj, volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp252_ema5_base_v044_signal(closeadj, volume):
    result = (_f043_pocket_pivot(closeadj, volume, 252)).ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_pp252_ema21_base_v045_signal(closeadj, volume):
    result = (_f043_pocket_pivot(closeadj, volume, 252)).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_uprat21_raw_base_v046_signal(closeadj, volume):
    result = _f043_up_day_vol(closeadj, volume, 21) / (_f043_max_down_vol(closeadj, volume, 21) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_uprat21_ema5_base_v047_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 21) / (_f043_max_down_vol(closeadj, volume, 21) + 1.0) * closeadj).ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_uprat21_ema21_base_v048_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 21) / (_f043_max_down_vol(closeadj, volume, 21) + 1.0) * closeadj).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_uprat63_raw_base_v049_signal(closeadj, volume):
    result = _f043_up_day_vol(closeadj, volume, 63) / (_f043_max_down_vol(closeadj, volume, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_uprat63_ema5_base_v050_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 63) / (_f043_max_down_vol(closeadj, volume, 63) + 1.0) * closeadj).ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_uprat63_ema21_base_v051_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 63) / (_f043_max_down_vol(closeadj, volume, 63) + 1.0) * closeadj).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_uprat126_raw_base_v052_signal(closeadj, volume):
    result = _f043_up_day_vol(closeadj, volume, 126) / (_f043_max_down_vol(closeadj, volume, 126) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_uprat126_ema5_base_v053_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 126) / (_f043_max_down_vol(closeadj, volume, 126) + 1.0) * closeadj).ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_uprat126_ema21_base_v054_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 126) / (_f043_max_down_vol(closeadj, volume, 126) + 1.0) * closeadj).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_uprat252_raw_base_v055_signal(closeadj, volume):
    result = _f043_up_day_vol(closeadj, volume, 252) / (_f043_max_down_vol(closeadj, volume, 252) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_uprat252_ema5_base_v056_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 252) / (_f043_max_down_vol(closeadj, volume, 252) + 1.0) * closeadj).ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_uprat252_ema21_base_v057_signal(closeadj, volume):
    result = (_f043_up_day_vol(closeadj, volume, 252) / (_f043_max_down_vol(closeadj, volume, 252) + 1.0) * closeadj).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_ppxlc21_raw_base_v058_signal(closeadj, volume):
    result = _f043_pocket_pivot(closeadj, volume, 21) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_ppxlc21_ema5_base_v059_signal(closeadj, volume):
    result = (_f043_pocket_pivot(closeadj, volume, 21) * np.log(closeadj.replace(0, np.nan).abs())).ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_ppxlc21_ema21_base_v060_signal(closeadj, volume):
    result = (_f043_pocket_pivot(closeadj, volume, 21) * np.log(closeadj.replace(0, np.nan).abs())).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_ppxlc63_raw_base_v061_signal(closeadj, volume):
    result = _f043_pocket_pivot(closeadj, volume, 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_ppxlc63_ema5_base_v062_signal(closeadj, volume):
    result = (_f043_pocket_pivot(closeadj, volume, 63) * np.log(closeadj.replace(0, np.nan).abs())).ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_ppxlc63_ema21_base_v063_signal(closeadj, volume):
    result = (_f043_pocket_pivot(closeadj, volume, 63) * np.log(closeadj.replace(0, np.nan).abs())).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_loguv21_raw_base_v064_signal(closeadj, volume):
    result = _z(np.log1p(_f043_up_day_vol(closeadj, volume, 21)), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_loguv21_ema5_base_v065_signal(closeadj, volume):
    result = (_z(np.log1p(_f043_up_day_vol(closeadj, volume, 21)), 252) * _safe_div(closeadj, _mean(closeadj, 252))).ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_loguv21_ema21_base_v066_signal(closeadj, volume):
    result = (np.log1p(_f043_up_day_vol(closeadj, volume, 21)) * closeadj).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_loguv63_raw_base_v067_signal(closeadj, volume):
    result = _z(np.log1p(_f043_up_day_vol(closeadj, volume, 63)), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_loguv63_ema5_base_v068_signal(closeadj, volume):
    result = (_z(np.log1p(_f043_up_day_vol(closeadj, volume, 63)), 252) * _safe_div(closeadj, _mean(closeadj, 252))).ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_loguv63_ema21_base_v069_signal(closeadj, volume):
    result = (np.log1p(_f043_up_day_vol(closeadj, volume, 63)) * closeadj).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_logmdv21_raw_base_v070_signal(closeadj, volume):
    result = _z(np.log1p(_f043_max_down_vol(closeadj, volume, 21)), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_logmdv21_ema5_base_v071_signal(closeadj, volume):
    result = (_z(np.log1p(_f043_max_down_vol(closeadj, volume, 21)), 252) * _safe_div(closeadj, _mean(closeadj, 252))).ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_logmdv21_ema21_base_v072_signal(closeadj, volume):
    result = (np.log1p(_f043_max_down_vol(closeadj, volume, 21)) * closeadj).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_logmdv63_raw_base_v073_signal(closeadj, volume):
    result = _z(np.log1p(_f043_max_down_vol(closeadj, volume, 63)), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_logmdv63_ema5_base_v074_signal(closeadj, volume):
    result = (_z(np.log1p(_f043_max_down_vol(closeadj, volume, 63)), 252) * _safe_div(closeadj, _mean(closeadj, 252))).ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f043ppf_f043_pocket_pivot_flag_logmdv63_ema21_base_v075_signal(closeadj, volume):
    result = (np.log1p(_f043_max_down_vol(closeadj, volume, 63)) * closeadj).ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f043ppf_f043_pocket_pivot_flag_upvol10x_raw_base_v001_signal,
    f043ppf_f043_pocket_pivot_flag_upvol10x_ema5_base_v002_signal,
    f043ppf_f043_pocket_pivot_flag_upvol10x_ema21_base_v003_signal,
    f043ppf_f043_pocket_pivot_flag_upvol21x_raw_base_v004_signal,
    f043ppf_f043_pocket_pivot_flag_upvol21x_ema5_base_v005_signal,
    f043ppf_f043_pocket_pivot_flag_upvol21x_ema21_base_v006_signal,
    f043ppf_f043_pocket_pivot_flag_upvol63x_raw_base_v007_signal,
    f043ppf_f043_pocket_pivot_flag_upvol63x_ema5_base_v008_signal,
    f043ppf_f043_pocket_pivot_flag_upvol63x_ema21_base_v009_signal,
    f043ppf_f043_pocket_pivot_flag_upvol126x_raw_base_v010_signal,
    f043ppf_f043_pocket_pivot_flag_upvol126x_ema5_base_v011_signal,
    f043ppf_f043_pocket_pivot_flag_upvol126x_ema21_base_v012_signal,
    f043ppf_f043_pocket_pivot_flag_upvol252x_raw_base_v013_signal,
    f043ppf_f043_pocket_pivot_flag_upvol252x_ema5_base_v014_signal,
    f043ppf_f043_pocket_pivot_flag_upvol252x_ema21_base_v015_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol10x_raw_base_v016_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol10x_ema5_base_v017_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol10x_ema21_base_v018_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol21x_raw_base_v019_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol21x_ema5_base_v020_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol21x_ema21_base_v021_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol63x_raw_base_v022_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol63x_ema5_base_v023_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol63x_ema21_base_v024_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol126x_raw_base_v025_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol126x_ema5_base_v026_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol126x_ema21_base_v027_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol252x_raw_base_v028_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol252x_ema5_base_v029_signal,
    f043ppf_f043_pocket_pivot_flag_maxdvol252x_ema21_base_v030_signal,
    f043ppf_f043_pocket_pivot_flag_pp10_raw_base_v031_signal,
    f043ppf_f043_pocket_pivot_flag_pp10_ema5_base_v032_signal,
    f043ppf_f043_pocket_pivot_flag_pp10_ema21_base_v033_signal,
    f043ppf_f043_pocket_pivot_flag_pp21_raw_base_v034_signal,
    f043ppf_f043_pocket_pivot_flag_pp21_ema5_base_v035_signal,
    f043ppf_f043_pocket_pivot_flag_pp21_ema21_base_v036_signal,
    f043ppf_f043_pocket_pivot_flag_pp63_raw_base_v037_signal,
    f043ppf_f043_pocket_pivot_flag_pp63_ema5_base_v038_signal,
    f043ppf_f043_pocket_pivot_flag_pp63_ema21_base_v039_signal,
    f043ppf_f043_pocket_pivot_flag_pp126_raw_base_v040_signal,
    f043ppf_f043_pocket_pivot_flag_pp126_ema5_base_v041_signal,
    f043ppf_f043_pocket_pivot_flag_pp126_ema21_base_v042_signal,
    f043ppf_f043_pocket_pivot_flag_pp252_raw_base_v043_signal,
    f043ppf_f043_pocket_pivot_flag_pp252_ema5_base_v044_signal,
    f043ppf_f043_pocket_pivot_flag_pp252_ema21_base_v045_signal,
    f043ppf_f043_pocket_pivot_flag_uprat21_raw_base_v046_signal,
    f043ppf_f043_pocket_pivot_flag_uprat21_ema5_base_v047_signal,
    f043ppf_f043_pocket_pivot_flag_uprat21_ema21_base_v048_signal,
    f043ppf_f043_pocket_pivot_flag_uprat63_raw_base_v049_signal,
    f043ppf_f043_pocket_pivot_flag_uprat63_ema5_base_v050_signal,
    f043ppf_f043_pocket_pivot_flag_uprat63_ema21_base_v051_signal,
    f043ppf_f043_pocket_pivot_flag_uprat126_raw_base_v052_signal,
    f043ppf_f043_pocket_pivot_flag_uprat126_ema5_base_v053_signal,
    f043ppf_f043_pocket_pivot_flag_uprat126_ema21_base_v054_signal,
    f043ppf_f043_pocket_pivot_flag_uprat252_raw_base_v055_signal,
    f043ppf_f043_pocket_pivot_flag_uprat252_ema5_base_v056_signal,
    f043ppf_f043_pocket_pivot_flag_uprat252_ema21_base_v057_signal,
    f043ppf_f043_pocket_pivot_flag_ppxlc21_raw_base_v058_signal,
    f043ppf_f043_pocket_pivot_flag_ppxlc21_ema5_base_v059_signal,
    f043ppf_f043_pocket_pivot_flag_ppxlc21_ema21_base_v060_signal,
    f043ppf_f043_pocket_pivot_flag_ppxlc63_raw_base_v061_signal,
    f043ppf_f043_pocket_pivot_flag_ppxlc63_ema5_base_v062_signal,
    f043ppf_f043_pocket_pivot_flag_ppxlc63_ema21_base_v063_signal,
    f043ppf_f043_pocket_pivot_flag_loguv21_raw_base_v064_signal,
    f043ppf_f043_pocket_pivot_flag_loguv21_ema5_base_v065_signal,
    f043ppf_f043_pocket_pivot_flag_loguv21_ema21_base_v066_signal,
    f043ppf_f043_pocket_pivot_flag_loguv63_raw_base_v067_signal,
    f043ppf_f043_pocket_pivot_flag_loguv63_ema5_base_v068_signal,
    f043ppf_f043_pocket_pivot_flag_loguv63_ema21_base_v069_signal,
    f043ppf_f043_pocket_pivot_flag_logmdv21_raw_base_v070_signal,
    f043ppf_f043_pocket_pivot_flag_logmdv21_ema5_base_v071_signal,
    f043ppf_f043_pocket_pivot_flag_logmdv21_ema21_base_v072_signal,
    f043ppf_f043_pocket_pivot_flag_logmdv63_raw_base_v073_signal,
    f043ppf_f043_pocket_pivot_flag_logmdv63_ema5_base_v074_signal,
    f043ppf_f043_pocket_pivot_flag_logmdv63_ema21_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F043_POCKET_PIVOT_FLAG_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f043_up_day_vol", "_f043_max_down_vol", "_f043_pocket_pivot")
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
